# Directory 

```bash
east-side-server/
├── server.py                         # Your Python HTTP server
├── requirements.txt                  # Python dependencies
├── 083025-east-side-index.html      # Your alternate dashboard
├── index.html                        # Default homepage (optional, could point to above)
├── templates/
│   └── success.html                  # Upload confirmation page (used in POST response)
├── static/
│   ├── success.png                   # Image shown after upload
│   └── css/                          # (optional) stylesheets if modularized
│       └── styles.css
├── orchids/                          # Uploaded orchid files
├── docs/                             # Uploaded documentation
├── after-work/                       # After-work content
├── assignments/                      # Student assignment files
├── uploads/                          # Temporary upload staging
├── logs/                             # (optional) custom server logs
└── scripts/
    └── setup.sh                      # (optional) startup automation, service scripts
```

# Setup .sh script

```bash
#!/bin/bash

echo "Setting up East Side Server directories..."

mkdir -p orchids
mkdir -p docs
mkdir -p after-work
mkdir -p assignments
mkdir -p uploads
mkdir -p logs
mkdir -p templates
mkdir -p static/css
mkdir -p scripts

touch logs/server.log

echo "Folders created:"
echo "  orchids/ docs/ after-work/ assignments/ uploads/ logs/ templates/ static/css/ scripts/"

# Optional: copy placeholder success image. Using Capt Clip for now
if [[ -f success.png ]]; then
    mv success.png static/
    echo "Moved success.png into static/"
fi

echo "Setup complete!"
```

```python
import os
import re
import json
import shutil
import logging
import requests
import feedparser
import yaml

from http.server import SimpleHTTPRequestHandler, HTTPServer

# === Logger Setup ===
logger = logging.getLogger('east-side-server')
logger.setLevel(logging.INFO)
stream = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream.setFormatter(formatter)
logger.addHandler(stream)

# === Load Routing Rules from YAML ===
def load_routing_config():
    default = {
        "orchid_": "orchids",
        "doc_": "docs",
        "after_": "after-work",
        "assign_": "assignments"
    }
    try:
        with open("config.yaml", "r") as f:
            return yaml.safe_load(f)["routing_rules"]
    except Exception as e:
        logger.warning(f"Could not load config.yaml, using defaults. Reason: {e}")
        return default

# === Custom Request Handler ===
class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path in ('/', '/index.html'):
            self.path = '/083025-east-side-index.html'

        elif self.path == '/success.png':
            image_path = 'static/success.png'
            if os.path.exists(image_path):
                with open(image_path, 'rb') as f:
                    self.send_response(200)
                    self.send_header('Content-type', 'image/png')
                    self.end_headers()
                    self.wfile.write(f.read())
                return
            else:
                self.send_error(404, 'success.png not found')
                return

        elif self.path == '/fetch_rss':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            feed = self.fetch_rss_feed()
            self.wfile.write(json.dumps(feed).encode())
            return

        else:
            super().do_GET()

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        content_type = self.headers.get('Content-Type', '')

        if "boundary=" not in content_type:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid Content-Type")
            return

        boundary = content_type.split("boundary=")[1].encode()
        body = self.rfile.read(content_length)

        try:
            parts = self.parse_multipart(body, boundary)
            for part in parts:
                disposition = part['headers'].get('Content-Disposition', '')
                if 'filename=' in disposition:
                    filename = disposition.split('filename=')[1].strip('"')
                    sanitized = self.sanitize_filename(filename)

                    if sanitized == 'fake_passwd':
                        self.send_response(200)
                        self.end_headers()
                        self.wfile.write(b"root:x:0:0:root:/root:/bin/bash\n")
                        return

                    upload_path = os.path.join('uploads', sanitized)
                    self.ensure_directory('uploads')

                    with open(upload_path, 'wb') as f:
                        f.write(part['body'])

                    self.move_file(upload_path)

                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()

                    with open("templates/success.html", "r") as success:
                        self.wfile.write(success.read().encode())
                    return

            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"No file found in upload")
        except Exception as e:
            logger.error(f"Upload failed: {e}")
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Internal Server Error")

    def fetch_rss_feed(self):
        url = "https://www.securityweek.com/feed/"
        headers = {'User-Agent': 'Mozilla/5.0'}

        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                parsed = feedparser.parse(response.content)
                return [
                    {
                        "title": e.title,
                        "link": e.link,
                        "published": e.published
                    }
                    for e in parsed.entries[:5]
                ]
            else:
                logger.warning(f"RSS feed returned HTTP {response.status_code}")
                return []
        except Exception as e:
            logger.error(f"Failed to fetch RSS: {e}")
            return []

    def move_file(self, filepath):
        rules = load_routing_config()
        filename = os.path.basename(filepath).lower()

        for prefix, folder in rules.items():
            if filename.startswith(prefix):
                self.ensure_directory(folder)
                shutil.move(filepath, os.path.join(folder, os.path.basename(filepath)))
                logger.info(f"Moved file {filename} to {folder}/")
                return

        # Default
        self.ensure_directory('assignments')
        shutil.move(filepath, os.path.join('assignments', os.path.basename(filepath)))
        logger.info(f"Moved file {filename} to assignments/ (default)")

    def parse_multipart(self, body, boundary):
        parts = []
        boundary = b'--' + boundary
        for part in body.split(boundary):
            if part and part != b'--\r\n':
                part = part.strip(b'\r\n')
                headers_raw, content = part.split(b'\r\n\r\n', 1)
                headers = self.parse_headers(headers_raw.decode())
                parts.append({'headers': headers, 'body': content})
        return parts

    def parse_headers(self, raw):
        headers = {}
        for line in raw.split('\r\n'):
            if ': ' in line:
                key, value = line.split(': ', 1)
                headers[key] = value
        return headers

    def sanitize_filename(self, filename):
        filename = os.path.basename(filename)
        if '..' in filename or filename.startswith('/'):
            return 'fake_passwd'
        return re.sub(r'[^a-zA-Z0-9._-]', '_', filename)

    def ensure_directory(self, path):
        os.makedirs(path, exist_ok=True)

# === Run Server ===
def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logger.info(f"Serving on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
```

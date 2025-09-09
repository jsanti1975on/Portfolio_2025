🌱 Directory Layout for Your IoT Subnet Dashboard

```Bash
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

## index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>East Side Server | IoT Subnet Dashboard</title>
  <style>
    body {
      background-color: #1e1e2e;
      color: #8aff80;
      font-family: 'Segoe UI', sans-serif;
      padding: 20px;
      margin: 0;
    }

    h1 {
      text-align: center;
      margin-bottom: 40px;
      border-bottom: 2px solid #8aff80;
      padding-bottom: 10px;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 15px;
    }

    .panel-container {
      position: relative;
    }

    .panel {
      background-color: #2a2a3d;
      padding: 20px;
      border-radius: 10px;
      border: 1px solid #8aff80;
      position: relative;
    }

    .hover-image {
      display: none;
      position: absolute;
      bottom: 110%;
      left: 50%;
      transform: translateX(-50%);
      z-index: 10;
      width: 300px;
      border: 2px solid #8aff80;
      border-radius: 10px;
      background: rgba(30, 30, 46, 0.95);
      padding: 5px;
      box-shadow: 0 4px 10px rgba(0, 255, 100, 0.3);
    }

    .panel-container:hover .hover-image {
      display: block;
      animation: floatIn 0.3s ease-out;
    }

    @keyframes floatIn {
      from {
        opacity: 0;
        transform: translateX(-50%) translateY(10px);
      }
      to {
        opacity: 1;
        transform: translateX(-50%) translateY(0);
      }
    }

    .panel h2 {
      margin-top: 0;
      font-size: 1.2em;
    }

    a.button {
      display: inline-block;
      margin-top: 10px;
      padding: 10px 15px;
      background-color: #8aff80;
      color: #1e1e2e;
      text-decoration: none;
      font-weight: bold;
      border-radius: 6px;
      transition: background-color 0.3s, transform 0.3s;
    }

    a.button:hover {
      background-color: #b6ffb3;
      transform: scale(1.1);
    }

    footer {
      text-align: center;
      margin-top: 40px;
      font-size: 0.9em;
      color: #6aff6a;
    }

    .rss-box {
      margin-top: 50px;
      padding: 30px;
      background-color: #2a2a3d;
      border: 2px solid #8aff80;
      border-radius: 10px;
    }

    .rss-box h2 {
      color: #8aff80;
    }

    .rss-entry {
      margin-bottom: 15px;
    }

    .rss-entry a {
      color: #b6ffb3;
    }

    hr {
      border: 1px solid #555;
    }
  </style>
</head>
<body>
  <div class="badge-container" style="text-align:center; margin-bottom: 10px;">
    <iframe src="https://tryhackme.com/api/v2/badges/public-profile?userPublicId=3596940" style="height:150px;width:300px;"></iframe>
    <br />
    <img src="https://tryhackme-badges.s3.amazonaws.com/Orkid1975.png" alt="Badge" style="margin-top:10px; height:30px;" />
  </div>

  <h1>East Side Server (IoT Subnet)</h1>

  <div class="grid">

    <!-- Orchid Collection -->
    <div class="panel-container">
      <div class="panel">
        <h2>Orchid Collection</h2>
        <p>Photos and documentation of orchids, greenhouse logs, and plant care notes.</p>
        <a href="/orchids/" class="button">View Orchids</a>
      </div>
      <img src="images/orchid.png" alt="Orchid Flower" class="hover-image" />
    </div>

    <!-- Docs -->
    <div class="panel-container">
      <div class="panel">
        <h2>Docs</h2>
        <p>General documentation, research notes, and useful references.</p>
        <a href="/docs/" class="button">Open Docs</a>
      </div>
      <img src="images/docs.png" alt="Docs Icon" class="hover-image" />
    </div>

    <!-- After Work -->
    <div class="panel-container">
      <div class="panel">
        <h2>After Work</h2>
        <p>Personal content, general interests, and IoT subnet sandbox experiments.</p>
        <a href="/after-work/" class="button">Browse</a>
      </div>
      <img src="images/after-work.png" alt="After Work" class="hover-image" />
    </div>

    <!-- Assignments -->
    <div class="panel-container">
      <div class="panel">
        <h2>Assignments</h2>
        <p>Dedicated space for my son’s college assignments and uploads.</p>
        <form enctype="multipart/form-data" method="post" action="/assignments/upload">
          <input type="file" name="file" required />
          <br><br>
          <input type="submit" value="Upload Assignment" style="background:#8aff80;color:#1e1e2e;padding:8px 16px;border:none;border-radius:5px;">
        </form>
        <br/>
        <a href="/assignments/" class="button">View Assignments</a>
      </div>
      <img src="images/assignments.png" alt="Assignments Icon" class="hover-image" />
    </div>

  </div>

  <div class="rss-box">
    <h2>Cybersecurity News Feed</h2>
    <div id="rss-feed" style="font-size: 0.95em; color: #b6ffb3;"></div>
  </div>

  <footer>
    &copy; 2025 East Side IoT Server | Orchids. Docs. Assignments. | jas.digital.tools (c) 2025
  </footer>

  <script>
    fetch('/fetch_rss')
      .then(res => res.json())
      .then(data => {
        const container = document.getElementById('rss-feed');
        if (data.length === 0) {
          container.innerHTML = '<p>No news available right now.</p>';
        } else {
          container.innerHTML = data.map(item => `
            <div class="rss-entry">
              <strong>${item.title}</strong><br>
              <a href="${item.link}" target="_blank">Read more</a><br>
              <small>${item.published}</small>
            </div>
          `).join('<hr>');
        }
      })
      .catch(() => {
        document.getElementById('rss-feed').innerHTML = '<p>Failed to load news feed.</p>';
      });
  </script>
</body>
</html>
```

```Python
import logging
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
import shutil
import re
import json
import requests
import feedparser

# Create a custom logger
logger = logging.getLogger('server_logger')
logger.setLevel(logging.INFO)

# Create handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# Add handler to the logger
logger.addHandler(ch)

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        content_type = self.headers.get('Content-Type', '')

        # Validate Content-Type header
        if "boundary=" not in content_type:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid Content-Type header")
            return

        # Extract boundary
        boundary = content_type.split("boundary=")[1].encode()
        body = self.rfile.read(content_length)

        try:
            parts = self.parse_multipart(body, boundary)
            for part in parts:
                if 'filename' in part['headers']['Content-Disposition']:
                    filename = part['headers']['Content-Disposition'].split('filename=')[1].strip('"')
                    sanitized_filename = self.sanitize_filename(filename)

                    # Security check: prevent malicious filename usage
                    if sanitized_filename == 'fake_passwd':
                        self.send_response(200)
                        self.send_header('Content-type', 'text/plain')
                        self.end_headers()
                        self.wfile.write(b"root:x:0:0:root:/root:/bin/bash\n")
                        return

                    upload_path = os.path.join('uploads', sanitized_filename)
                    self.ensure_directory('uploads')

                    with open(upload_path, 'wb') as f:
                        f.write(part['body'])

                    self.move_file(upload_path)

                    # Send success page with a redirect option
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()

                    success_message = f"""
                    <html>
                    <head>
                        <title>Upload Successful</title>
                        <script>
                            function redirectToUpload() {{
                                window.location.href = '/upload';
                            }}
                        </script>
                    </head>
                    <body style="text-align:center; background-color: black; color: green;">
                        <h2> File Uploaded Successfully!</h2>
                        <p>File: {sanitized_filename}</p>
                        <img src='/success.png' alt='Success Image' width='300'>
                        <br><br>
                        <button onclick="redirectToUpload()" style="font-size:18px; padding:10px; background-color:#34ac44; color:white; border:none; border-radius:5px; cursor:pointer;">
                            ⬅ Upload Another File
                        </button>
                    </body>
                    </html>
                    """

                    self.wfile.write(success_message.encode())
                    return

            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"File upload failed")
        except Exception as e:
            logger.error(f"Error during file upload: {e}")
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Internal server error")

    def do_GET(self):
        if self.path == '/success.png':
            if os.path.exists('success.png'):
                with open('success.png', 'rb') as f:
                    self.send_response(200)
                    self.send_header('Content-type', 'image/png')
                    self.end_headers()
                    self.wfile.write(f.read())
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<h2>Image Not Found</h2><p>Please upload success.png.</p>")
        elif self.path == '/fetch_rss':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            rss_content = self.fetch_rss_feed()
            self.wfile.write(json.dumps(rss_content).encode())
        else:
            super().do_GET()

    def fetch_rss_feed(self):
        url = "https://www.securityweek.com/feed/"
        headers = {'User-Agent': 'Mozilla/5.0'}

        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                feed = feedparser.parse(response.content)
                rss_content = []

                for entry in feed.entries[:5]:  # Limit to 5 articles
                    rss_content.append({
                        "title": entry.title,
                        "link": entry.link,
                        "published": entry.published
                    })
                return rss_content
            else:
                logger.error(f"RSS feed returned status code {response.status_code}")
                return []
        except Exception as e:
            logger.error(f"Error fetching RSS feed: {e}")
            return []

    def parse_multipart(self, body, boundary):
        parts = []
        boundary = b'--' + boundary
        for part in body.split(boundary):
            if part and part != b'--\r\n':
                part = part.strip(b'\r\n')
                try:
                    headers, body = part.split(b'\r\n\r\n', 1)
                    headers = self.parse_headers(headers.decode())
                    parts.append({'headers': headers, 'body': body})
                except ValueError as ve:
                    logger.error(f"Error parsing part: {ve}")
                    logger.debug(f"Part content: {part[:100]}...")
        return parts

    def parse_headers(self, headers):
        header_dict = {}
        for line in headers.split('\r\n'):
            try:
                key, value = line.split(': ', 1)
                header_dict[key] = value
            except ValueError:
                logger.error(f"Error parsing header line: {line}")
        return header_dict

    def ensure_directory(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def sanitize_filename(self, filename):
        filename = os.path.basename(filename)
        sanitized = re.sub(r'[^a-zA-Z0-9._-]', '_', filename)
        if '..' in filename or filename.startswith('/'):
            return 'fake_passwd'
        return sanitized

    # East Side Server File Rules
    def move_file(self, filepath):
        filename = os.path.basename(filepath).lower()

        if filename.startswith('orchid_'):
            self.move_orchid_files(filepath)
        elif filename.startswith('doc_'):
            self.move_doc_files(filepath)
        elif filename.startswith('after_'):
            self.move_afterwork_files(filepath)
        elif filename.startswith('assign_'):
            self.move_assignment_files(filepath)
        else:
            # Default: all untagged files go into assignments
            self.move_assignment_files(filepath)

    def move_orchid_files(self, filepath):
        self.ensure_directory('orchids')
        shutil.move(filepath, os.path.join('orchids', os.path.basename(filepath)))

    def move_doc_files(self, filepath):
        self.ensure_directory('docs')
        shutil.move(filepath, os.path.join('docs', os.path.basename(filepath)))

    def move_afterwork_files(self, filepath):
        self.ensure_directory('after-work')
        shutil.move(filepath, os.path.join('after-work', os.path.basename(filepath)))

    def move_assignment_files(self, filepath):
        self.ensure_directory('assignments')
        shutil.move(filepath, os.path.join('assignments', os.path.basename(filepath)))

def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logger.info(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
```




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
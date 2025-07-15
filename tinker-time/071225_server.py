from http.server import SimpleHTTPRequestHandler, HTTPServer
import cgi
import os
import html
import json
import logging

UPLOAD_DIR = 'uploads'

# Setup logger
logger = logging.getLogger('upload_server')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/upload':
            content_type, pdict = cgi.parse_header(self.headers.get('Content-Type'))
            if content_type == 'multipart/form-data':
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={
                        'REQUEST_METHOD': 'POST',
                        'CONTENT_TYPE': self.headers.get('Content-Type'),
                        'CONTENT_LENGTH': self.headers.get('Content-Length')
                    }
                )
                file_item = form['file']
                if file_item.filename:
                    filename = os.path.basename(file_item.filename)
                    os.makedirs(UPLOAD_DIR, exist_ok=True)
                    filepath = os.path.join(UPLOAD_DIR, filename)
                    with open(filepath, 'wb') as f:
                        f.write(file_item.file.read())

                    self.send_response(200)
                    self.send_header("Content-type", "text/html; charset=utf-8")
                    self.end_headers()

                    # File list display
                    file_list = os.listdir(UPLOAD_DIR)
                    file_links = "<ul>" + "".join(
                        f"<li><a href='/{UPLOAD_DIR}/{html.escape(f)}'>{html.escape(f)}</a></li>" for f in file_list
                    ) + "</ul>"

                    self.wfile.write(f"""
                        <html>
                        <body style='font-family:sans-serif;text-align:center;margin-top:50px;'>
                            <h2>✅ Upload successful: {html.escape(filename)}</h2>
                            <button onclick="window.location.href='/'">🔙 Back to Dashboard</button>
                            <h3>📂 Uploaded Files</h3>
                            {file_links}
                        </body>
                        </html>
                    """.encode('utf-8'))
                    return
        self.send_error(400, "Invalid Request")

    def do_GET(self):
        if self.path.startswith('/uploads/'):
            return super().do_GET()
        elif self.path == '/fetch_weather':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(self.fetch_current_weather()).encode())
        elif self.path == '/fetch_orchid_rss':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(self.fetch_orchid_rss()).encode())
        else:
            super().do_GET()

    def fetch_current_weather(self):
        return {
            "location": "Simulated Lab",
            "temperature_f": "72.0 F",
            "weather": "Clear",
            "wind": "None",
            "observation_time": "Simulated"
        }

    def fetch_orchid_rss(self):
        return [
            {"title": "Orchid Care Tip 1", "link": "#"},
            {"title": "Orchid News Update", "link": "#"}
        ]

def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler, port=8080):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logger.info(f"🛡️ TryHackMe Server Running: http://0.0.0.0:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()

from http.server import HTTPServer, SimpleHTTPRequestHandler
import cgi, os
from datetime import datetime

UPLOAD_DIR = "uploads"
REPORT_DIR = "reports"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

class AuditHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/submit":
            ctype, pdict = cgi.parse_header(self.headers.get('Content-Type'))
            if ctype == 'multipart/form-data':
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={
                        'REQUEST_METHOD': 'POST',
                        'CONTENT_TYPE': self.headers.get('Content-Type')
                    }
                )

                username = form.getvalue("username", "anonymous").strip().replace(" ", "_")
                summary = form.getvalue("summary", "").strip()
                timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                base_filename = f"{username}_{timestamp}"

                # Save summary
                with open(os.path.join(REPORT_DIR, base_filename + ".txt"), "w") as f:
                    f.write(summary)

                # Save photo
                if "photo" in form and form["photo"].filename:
                    photo_data = form["photo"].file.read()
                    with open(os.path.join(UPLOAD_DIR, base_filename + ".jpg"), "wb") as f:
                        f.write(photo_data)

                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f"""
                <html><body style="font-family:sans-serif;text-align:center;margin-top:50px;">
                <h2>✅ Audit Received, {username}!</h2>
                <p><a href="/">Submit Another</a></p>
                </body></html>
                """.encode())
            else:
                self.send_error(400, "Bad Request")

def run():
    os.chdir(os.path.dirname(__file__))
    print("🔐 Audit server running at http://localhost:8000")
    HTTPServer(("", 8000), AuditHandler).serve_forever()

if __name__ == "__main__":
    run()

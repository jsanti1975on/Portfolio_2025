# Generate the certs=> 
# openssl req -new -x509 -keyout key.pem -out cert.pem -days 365 -nodes

# Depricated
import http.server, ssl

server_address = ('0.0.0.0', 8443)

httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               certfile="key.pem",
                               ssl_version=ssl.PROTOCOL_TLS)
print("Serving HTTPS on poert 8443")
httpd.serve_forever()


# RHEL
#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl, os

# ---- settings ----
HOST = "0.0.0.0"
PORT = 8443
CERT = "cert.pem"
KEY  = "key.pem"
SERVE_DIR = os.path.abspath(".")   # or set to a specific folder

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Python 3.8+: 'directory' sets the doc root
        super().__init__(*args, directory=SERVE_DIR, **kwargs)

if __name__ == "__main__":
    httpd = HTTPServer((HOST, PORT), Handler)

    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.minimum_version = ssl.TLSVersion.TLSv1_2
    ctx.load_cert_chain(certfile=CERT, keyfile=KEY)

    httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
    print(f"Serving HTTPS from {SERVE_DIR} at https://{HOST}:{PORT}/")
    httpd.serve_forever()






# Generate the certs=> 
# openssl req -new -x509 -keyout key.pem -out cert.pem -days 365 -nodes


import http.server, ssl

server_address = ('0.0.0.0', 8443)

httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               certfile="key.pem",
                               ssl_version=ssl.PROTOCOL_TLS)
print("Serving HTTPS on poert 8443")
httpd.serve_forever()




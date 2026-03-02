from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from API server!")

server = HTTPServer(("127.0.0.1", 9000), Handler)
print("API running on port 9000...")
server.serve_forever()

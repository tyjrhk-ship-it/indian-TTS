from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response = {
            "status": "success",
            "message": "Indian TTS backend is working!"
        }

        self.wfile.write(json.dumps(response).encode())

server = HTTPServer(("0.0.0.0", 8000), Handler)
print("Server running on http://0.0.0.0:8000")
server.serve_forever()

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SecurityHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/login'):
            logging.warning("401 Unauthorized: Failed login attempt for user 'admin'")
            self.send_response(401)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<h2 style='color:red;'>Access Denied. Bad Password.</h2>")
        
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<h2>Welcome to the Secure Portal. Please go to /login</h2>")

# Start the secure server
server = HTTPServer(('0.0.0.0', 8000), SecurityHandler)
logging.info("Security Login Portal Booted Successfully on port 8000.")
server.serve_forever()
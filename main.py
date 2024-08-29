import http.server
import socketserver

PORT = 8000

# Create a handler that serves files from the current directory
Handler = http.server.SimpleHTTPRequestHandler

# Create a TCP server at the given port
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
  




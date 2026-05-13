#!/usr/bin/env python3
import http.server
import socketserver
import socket
import sys
import os

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def log_message(self, format, *args):
        pass  # suppress request logs

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "localhost"

os.chdir(os.path.dirname(os.path.abspath(__file__)))
ip = get_ip()

print(f"\nAlla Bitar — lokal server")
print(f"─────────────────────────────")
print(f"  Sajt:    http://{ip}:{PORT}/index.html")
print(f"  Editor:  http://{ip}:{PORT}/editor.html")
print(f"\n  Ctrl+C för att stoppa\n")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server stoppad.")
        sys.exit(0)

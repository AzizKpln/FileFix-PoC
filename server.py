from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

PORT = 5000
DIRECTORY = "files"

class CustomHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run_server():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    httpd = HTTPServer(("0.0.0.0", PORT), CustomHandler)
    print(f"Sunucu başlatıldı: http://localhost:{PORT}/poc.bat")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()

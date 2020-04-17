from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    queryString = self.path.split('webscrape?')
    if(len(queryString) > 1 and 'url=' in queryString[1]):
        query = parse_qs(queryString[1])
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str(query['url'][0]).encode())
    else:
        self.send_response(500)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Missing url parameter'.encode())

    return

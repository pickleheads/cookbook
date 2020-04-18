from http.server import BaseHTTPRequestHandler
import urllib.request as request
import re
from urllib import parse
from bs4 import BeautifulSoup

class handler(BaseHTTPRequestHandler):
  whitelisted_url_regexes = [
    re.compile("^https:\/\/www\.bonappetit\.com")
  ]
  def do_GET(self):
    url = parse.parse_qs(parse.urlsplit(self.path).query)['url'][0]
    url_in_whitelist = any(regex.match(url) for regex in self.whitelisted_url_regexes)
    if(not url_in_whitelist):
      self.send_response(500)
      self.send_header('Content-type', 'text/plain')
      self.end_headers()
      self.wfile.write('Unsupported recipe site'.encode())
      return

    file_pointer = request.urlopen(url)
    html_bytes = file_pointer.read()
    html_doc = html_bytes.decode("utf8")
    file_pointer.close()

    soup = BeautifulSoup(html_doc, 'html.parser')
    ingredients = soup.find("div", "ingredients")
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(str(ingredients.prettify()).encode())
    return

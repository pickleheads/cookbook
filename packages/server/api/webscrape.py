from http.server import BaseHTTPRequestHandler
import urllib.request as request
import re
from urllib.parse import parse_qs
from selenium import webdriver
from bs4 import BeautifulSoup

class handler(BaseHTTPRequestHandler):
  whitelisted_url_regexes = [
    re.compile("^https:\/\/www.bonappetit.com")
  ]
  def do_GET(self):
    queryString = self.path.split('webscrape?')
    if(len(queryString) > 1 and 'url=' in queryString[1]):
      query = parse_qs(queryString[1])
      url = query['url'][0]

      if(not any(regex.match(url) for regex in self.whitelisted_url_regexes)):
        self.send_response(500)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Unsupported recipe site'.encode())
        return

      fp = request.urlopen(url)
      mybytes = fp.read()
      html_doc = mybytes.decode("utf8")
      fp.close()

      soup = BeautifulSoup(html_doc, 'html.parser')
      ingredients = soup.find("div", "ingredients")
      self.send_response(200)
      self.send_header('Content-type', 'text/plain')
      self.end_headers()
      self.wfile.write(str(ingredients.prettify()).encode())
    else:
        self.send_response(500)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Missing url parameter'.encode())
    return

import re
from bs4 import BeautifulSoup
from flask import Flask, Response, request

app = Flask(__name__)

WHITELISTED_URL_REGEXES = [re.compile("^https://www\.bonappetit\.com")]


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def parse_recipe(path):
    print("<h1>Flask</h1><p>You visited: /%s</p>" % (path))
    url = request.args.get("url")
    url_in_whitelist = any(regex.match(url) for regex in WHITELISTED_URL_REGEXES)

    if not url_in_whitelist:
        return Response(
            "Unsupported recipe site", content_type="text/plain", status=500
        )

    file_pointer = request.urlopen(url)
    html_bytes = file_pointer.read()
    html_doc = html_bytes.decode("utf8")
    file_pointer.close()
    html_parsed = BeautifulSoup(html_doc, "html.parser")
    ingredients = html_parsed.find("div", "ingredients")

    return Response(str(ingredients.prettify()), status=200, content_type="text/plain")

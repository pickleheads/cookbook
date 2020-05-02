import re
from bs4 import BeautifulSoup
from flask import Flask, Response, request
import json
import urllib.request

app = Flask(__name__)

bonappetit_regex = re.compile("^https://www\.bonappetit\.com")

WHITELISTED_URL_REGEXES = [bonappetit_regex]

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def parse_recipe(path):
    url = request.args.get("url")
    print("<h1>Flask</h1><p>You visited: %s</p>" % (url))

    url_in_whitelist = any(regex.match(url) for regex in WHITELISTED_URL_REGEXES)

    if not url_in_whitelist:
        return Response(
            "Unsupported recipe site", content_type="text/plain", status=500
        )
    try: 
        file_pointer = urllib.request.urlopen(url)
        html_bytes = file_pointer.read()
        html_doc = html_bytes.decode("utf8")
        file_pointer.close()
        html_parsed = BeautifulSoup(html_doc, "html.parser")
    except:
        return Response(
            "HTML could not be parsed", content_type="text/plain", status=500
        )
    try: 
        if(bonappetit_regex.match(url)): 
            recipe_object = format_recipe_bonappetit(html_parsed, url)
    except:
        return Response(
            "Recipe object could not be parsed", content_type="text/plain", status=500
        )

    return Response(json.dumps(recipe_object).encode(), status=200, content_type="text/plain")

## Recipe Formatter Utils ##
def format_recipe_bonappetit(html_parsed, url):
	recipe_object = {}
	recipe_object['name'] = html_parsed.find('a', 'top-anchor').text
	recipe_object['servings'] = html_parsed.find('span', 'recipe__header__servings recipe__header__servings--basically').span.text
	ingredients = html_parsed.find_all('div', 'ingredients__text')
	ingredients_array = list(map(lambda ingredient : ingredient.text, ingredients))
	recipe_object['ingredients'] = ingredients_array
	steps = html_parsed.find_all('li', 'step')
	steps_array = list(map(lambda step : step.div.p.text, steps))
	recipe_object['steps'] = steps_array
	recipe_object['link'] = url
	return recipe_object
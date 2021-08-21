import urllib,json
from app import app





base_url=app.config['QUOTES_URL']
def get_quotes():
    quotes_url='base_url'
    with urllib.request.urlopen(quotes_url) as url:
        quotes_data=url.read()
        quotes_data_response=json.loads(quotes_data)
    return quotes_data_response

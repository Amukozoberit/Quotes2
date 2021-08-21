import urllib,json
def get_quotes():
    quotes_url='http://quotes.stormconsultancy.co.uk/random.json'
    with urllib.request.urlopen(quotes_url) as url:
        quotes_data=url.read()
        quotes_data_response=json.loads(quotes_data)
    return quotes_data_response

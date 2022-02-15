import urllib.request,json
def get_quote():
    '''
    Function that gets the random quotes
    '''
    get_article_details_url = 'http://quotes.stormconsultancy.co.uk/random.json'.format()
    with urllib.request.urlopen(get_article_details_url)as url:
        quote_data = url.read()
        quote_response = json.loads(quote_data)
        print(quote_response)
    return quote_response
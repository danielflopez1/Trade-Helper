from requests_html import HTMLSession

### Enter a session of the marketwatch for a specific stock symbol and scrape the news
def get_symbol_news(symbol):
    url = "https://www.marketwatch.com/investing/stock/"+symbol
    session = HTMLSession()
    r = session.get(url)
    links = list(r.html.absolute_links)
    true_links = []
    wanted_links = ['https://www.marketwatch.com/press-release','https://www.marketwatch.com/articles/', 'https://www.marketwatch.com/story/','https://investorplace.com/']
    for i,text in enumerate(links):
        for w_link in wanted_links:
            if(w_link in text):
                true_links.append(text)
    session.close()
    return true_links

### Parse the html text into the real meat of the news (it get extra unnecessary texts from javascript)
def get_news_text(link):
    session = HTMLSession()
    r = session.get(link)
    text = str(r.html.text)
    start=text.find('Published:')                               #get the date of the published article to associate later on with sentiment analysis and market behavior
    am, pm = text.find('a.m.',start), text.find('p.m',start)
    if(am!=1):
        date_end = am+4
    else:
        date_end = pm+4
    end = text.find('Most Popular')                 #end text at end of article usually at ads
    date = text[start:date_end]
    information = text[start:end]
    information = information.replace('\n',' ')

    return information, date[len('Published'):]     #return news text and date of publication




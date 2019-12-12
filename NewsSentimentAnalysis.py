import Scrapper as sc
from sentiment_mod import VoteClassifier

vc = VoteClassifier()
symbols =['ba','ibm','zg']
for symbol in symbols:
    print("Symbol:", symbol)
    links = sc.get_symbol_news(symbol)
    for link in links[:5]:
        print(link)
        text = str(sc.get_news_text(link))
        print(vc.get_sentiment(text))



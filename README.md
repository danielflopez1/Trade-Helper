# Trade Helper
Made a web scraper for news in MarketWatch and used a sentiment analysis algorithm to check for how positive or negative they are. 

## Prerequisites
```
numpy
pip
nltk
matplotlib
scikit-learn
scipy
plotly
pandas
requests_html
smtplibaio
pickle
```

## Usage
Each program is independent of each other. Here you can find:
* Scrapper.py - Finds all the articles from MarketWatch and selects the main text
* [Sentiment Analysis](https://github.com/PythonProgramming/NLTK-3----Natural-Language-Processing-with-Python-series.git) - is used to train the sentiment analysis of the text. It can be tested using sentiment_mod.py
* TradingMaxMins - obtains data from alphavantage.co and analyzes when a stock is going up or down with some certainty.
* SendNotification- envía emails desde una cuenta a cualquier otra cuenta (se puede usar para notificaciónes de acciónes en bajada o subida)

## Resources

[Sentiment Analysis Tutorial](https://pythonprogramming.net/tokenizing-words-sentences-nltk-tutorial/)


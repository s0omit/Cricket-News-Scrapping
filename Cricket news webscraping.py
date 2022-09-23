# -*- coding: utf-8 -*-

# -- Sheet --

#importing necessary libraries
from bs4 import BeautifulSoup
import requests, openpyxl
import pandas as pd
from random import randint

#header declaration
headers = {"Accept-Language": "en-US,en;q=0.5"}

##declaring an empty variables, So that we can append the data in this
news_headline = []

#connecting to desired url
url = "https://www.icc-cricket.com/news"
page = requests.get(url)

#need html parser to parse html code
soup= BeautifulSoup(page.content, 'html.parser')

#extracting required info according to necessity, code depends upon where your info contains
infos = soup.findAll('figcaption', class_="thumbnail__caption")

#iteration
for info in infos:
    news = info.find('h5', class_="thumbnail__title").text
    print(news)
    news_headline.append(news)

cric_news = pd.DataFrame({ "News Headline ": news_headline})

cric_news.head(5)

cric_news.to_excel("Cricket News.xlsx")




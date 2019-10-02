# ------------------------------------ #
# Universidad del Valle de Guatemala   #
# Autores:                             #
#   Andrea Cordón, 16076               #
#   Cristopher Recinos, 16005          #
#   Pablo Lopez, 14509                 #
# lab5.py                              #
# ------------------------------------ #

import string
import re
from nltk.tokenize import word_tokenize
import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
from nltk.corpus import stopwords

#Impor Data
twitter = open("en_US.twitter.txt", "r", encoding="utf8").read()
news = open("en_US.news.txt", "r", encoding="utf8").read()
blogs = open("en_US.blogs.txt", "r", encoding="utf8").read()

print(len(twitter))
#print(len(news))
#print(len(blogs))

#Clean Twitter
twitter = twitter.lower()
twitter = re.sub(r'\d+', '', twitter)
twitter = twitter.translate(str.maketrans("","", string.punctuation))
twitter = twitter.encode('ascii', 'ignore').decode('ascii')

stop_words = set(stopwords.words('english'))
tokens = word_tokenize(twitter)
twitter = [i for i in tokens if not i in stop_words]

with open("twitter_new.txt", "w") as f:
    for item in twitter:
        f.write("%s," % item)

#Clean News
news = news.lower()
news = re.sub(r'\d+', '', news)
news = news.translate(str.maketrans("","", string.punctuation))
news = news.encode('ascii', 'ignore').decode('ascii')

stop_words = set(stopwords.words('english'))
tokens = word_tokenize(news)
news = [i for i in tokens if not i in stop_words]

with open("news_new.txt", "w") as f:
    for item in news:
        f.write("%s," % item)

#Clean Blogs
blogs = blogs.lower()
blogs = re.sub(r'\d+', '', blogs)
blogs = blogs.translate(str.maketrans("","", string.punctuation))
blogs = blogs.encode('ascii', 'ignore').decode('ascii')

stop_words = set(stopwords.words('english'))
tokens = word_tokenize(blogs)
blogs = [i for i in tokens if not i in stop_words]

with open("blogs_new.txt", "w") as f:
    for item in blogs:
        f.write("%s," % item)

print(len(twitter))
#print(len(news))
#print(len(blogs))

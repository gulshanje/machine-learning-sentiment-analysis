# -*- coding: utf-8 -*-
"""Flipkart-ML

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yoCbZdMiSfiAy84VuzRnla82LT45Y4HP
"""



"""## Import packages"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
import re
import string

from nltk.sentiment.vader import SentimentIntensityAnalyzer

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

nltk.download('stopwords')

from nltk.corpus import stopwords

stopword = set(stopwords.words('english'))



"""## Read/Import Data"""

data = pd.read_csv('/content/drive/MyDrive/machine-learning-data/flipkart_reviews.csv')

print(data.head(10))

print(data.isnull().sum())

stemmer = nltk.SnowballStemmer("english")

def clean(text):
  text=str(text).lower()
  text=re.sub('\[.*?]','',text)
  text=re.sub('https?://\S+|WWW.\S+','',text)
  text=re.sub('<.*?>+','',text)
  text=re.sub('n','',text)
  text=re.sub('\W*d\W*','',text)
  #text=re.sub('[%%S]' %% re.escape(string.string.punctuation), '', text)

  text=[word for word in text.split(' ') ]
  text="".join(text)
  text=[stemmer.stem(word) for word in text.split(' ')]
  text="".join(text)
  return text

data["Review"] = data["Review"].apply(clean)

"""## **Visualize the Data - Pie Chart**"""

ratings = data["Rating"].value_counts()
numbers = ratings.index
quantity = ratings.values

import plotly.express as px
figure = px.pie(data, values=quantity, names=numbers, hole=0.5)
figure.show()

"""## **Sentiment Intensity Analyzer**"""

nltk.download('vader_lexicon')
sentiments= SentimentIntensityAnalyzer()
data['Positive']= [sentiments.polarity_scores(i)["pos"] for i in data["Review"]]
data['Negative']= [sentiments.polarity_scores(i)["neg"] for i in data["Review"]]
data['Neutral']= [sentiments.polarity_scores(i)["neu"] for i in data["Review"]]

data = data[["Review", "Positive", "Negative", "Neutral"]]

print(data.head(10))

"""## **Overall Sentiment Score**"""

x=sum(data["Positive"])
y=sum(data["Negative"])
z=sum(data["Neutral"])

def sentimentScore(a,b,c):
  if(a >b) and (a > c):
    print("Positive")
  elif (b >1) and (b > c):
    print("Negative")
  else:
    print("Neutral")

sentimentScore(x,y,z)

"""## **Reason**"""

print("Positve: ", x)
print("Negative: ", y)
print("Neutral: ", z)
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Wczytaj dane z pliku CSV
data = pd.read_csv('chatgpt.csv', nrows=10000)

# Przetwarzanie tweetów i analiza nastroju
sentiments = []
for tweet in data['tweet']:
    # Wykonaj analizę nastroju przy użyciu TextBlob
    blob = TextBlob(tweet)
    sentiment = blob.sentiment.polarity
    sentiments.append(sentiment)

# Dodaj kolumnę z analizowanymi nastrojami do danych
data['sentiment'] = sentiments

# Przyporządkuj tweety do kategorii
data['category'] = data['sentiment'].apply(lambda x: 'Positive' if x > 0.1 else 'Neutral' if -0.1 <= x <= 0.1 else 'Negative')

# wykres 1
# Wygeneruj wykres słupkowy pokazujący rozkład kategorii
category_counts = data['category'].value_counts()
plt.bar(category_counts.index, category_counts.values)
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Distribution of Tweet Categories')
plt.show()

# wykres 2
# Wygeneruj wykres słupkowy pokazujący rozkład nastrojów
plt.hist(sentiments, bins=10)
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.title('Distribution of Sentiments in ChatGPT Tweets')
plt.show()

# wykres 3
# Wygeneruj wykres liniowy pokazujący zmiany nastroju w czasie
data['created_at'] = pd.to_datetime(data['created_at'])
data.plot(x='created_at', y='sentiment')
plt.xlabel('Time')
plt.ylabel('Sentiment')
plt.title('Sentiment over Time in ChatGPT Tweets')
plt.show()

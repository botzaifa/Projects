import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Take input sentences from the user
text_data = []
num_sentences = int(input("Enter the number of sentences: "))
for i in range(num_sentences):
    sentence = input(f"Enter sentence {i+1}: ")
    text_data.append(sentence)

# Perform sentiment analysis on each text
for text in text_data:
    sentiment_scores = sia.polarity_scores(text)
    sentiment = sentiment_scores['compound']

    if sentiment >= 0.05:
        category = "Positive"
    elif sentiment <= -0.05:
        category = "Negative"
    else:
        category = "Neutral"

    print(f"Text: {text}")
    print(f"Sentiment: {sentiment}")
    print(f"Category: {category}")
    print()

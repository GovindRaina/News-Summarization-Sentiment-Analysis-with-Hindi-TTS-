from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

# Initialize VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """
    Perform sentiment analysis using both TextBlob and VADER.
    Returns sentiment label: Positive, Negative, or Neutral.
    """
    if not text:
        return "Neutral"

    # TextBlob sentiment analysis
    textblob_sentiment = TextBlob(text).sentiment.polarity  # Range: -1 to 1

    # VADER sentiment analysis
    vader_sentiment = sia.polarity_scores(text)['compound']  # Compound score: -1 to 1

    # Combine both scores (you can modify the weight if needed)
    final_score = (textblob_sentiment + vader_sentiment) / 2

    # Assign sentiment label based on score
    if final_score > 0.05:
        return "Positive"
    elif final_score < -0.05:
        return "Negative"
    else:
        return "Neutral"

# Example usage
if __name__ == "__main__":
    text = "Tesla is making great progress with its new EV models."
    sentiment = analyze_sentiment(text)
    print(f"Sentiment: {sentiment}")  # Output: Positive

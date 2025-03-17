from collections import Counter

def comparative_analysis(articles):
    """
    Compares sentiment across multiple news articles.
    Returns a structured analysis including sentiment distribution.
    """
    sentiments = [article["sentiment"] for article in articles]
    sentiment_distribution = Counter(sentiments)  # Count occurrences

    # Identify coverage differences
    comparisons = []
    if len(articles) >= 2:
        for i in range(len(articles) - 1):
            comparisons.append({
                "Comparison": f"Article {i+1} vs Article {i+2}",
                "Difference": f"'{articles[i]['title']}' is {articles[i]['sentiment']}, "
                              f"while '{articles[i+1]['title']}' is {articles[i+1]['sentiment']}."
            })

    return {
        "Sentiment Distribution": sentiment_distribution,
        "Comparative Insights": comparisons
    }

# Example usage
if __name__ == "__main__":
    sample_articles = [
        {"title": "Tesla Hits Record Sales", "sentiment": "Positive"},
        {"title": "Tesla Faces Regulatory Issues", "sentiment": "Negative"},
        {"title": "Mixed Reactions to Tesla’s New Model", "sentiment": "Neutral"}
    ]
    
    analysis = comparative_analysis(sample_articles)
    print(analysis)

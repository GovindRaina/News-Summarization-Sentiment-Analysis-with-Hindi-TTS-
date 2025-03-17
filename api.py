from fastapi import FastAPI
from news_extraction import fetch_news
from sentiment_analysis import analyze_sentiment
from comparative_analysis import comparative_analysis
from tts_generation import generate_hindi_audio

app = FastAPI()

@app.get("/news/{company_name}")
def get_news(company_name: str):
    """
    API Endpoint to fetch news, analyze sentiment, compare trends, and generate TTS.
    """
    # Step 1: Fetch news articles
    articles = fetch_news(company_name)
    
    # Step 2: Perform sentiment analysis
    for article in articles:
        article["sentiment"] = analyze_sentiment(article["summary"])

    # Step 3: Comparative sentiment analysis
    analysis = comparative_analysis(articles)

    # Step 4: Convert final sentiment report into Hindi speech
    final_text = f"{company_name} की हाल की खबरें ज्यादातर {analysis['Sentiment Distribution']} दिखाती हैं।"
    audio_file = generate_hindi_audio(final_text)

    # Step 5: Return the structured response with audio
    return {
        "Company": company_name,
        "Articles": articles,
        "Comparative Analysis": analysis,
        "Audio File": audio_file  # Path to the generated TTS file
    }

# Run API with: uvicorn api:app --reload

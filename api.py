from fastapi import FastAPI
import gradio as gr
from news_extraction import fetch_news
from sentiment_analysis import analyze_sentiment
from comparative_analysis import comparative_analysis
from tts_generation import generate_hindi_audio

app = FastAPI()

@app.get("/news/{company_name}")
def get_news(company_name: str):
    articles = fetch_news(company_name)
    
    for article in articles:
        article["sentiment"] = analyze_sentiment(article["summary"])

    analysis = comparative_analysis(articles)

    final_text = f"{company_name} की हाल की खबरें ज्यादातर {analysis['Sentiment Distribution']} दिखाती हैं।"
    audio_file = generate_hindi_audio(final_text)

    return {
        "Company": company_name,
        "Articles": articles,
        "Comparative Analysis": analysis,
        "Audio File": audio_file
    }

# Gradio Wrapper to Keep API Running on Hugging Face
def start_fastapi():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)

gr.Interface(fn=start_fastapi, inputs=[], outputs=[]).launch()

from fastapi import FastAPI
import gradio as gr
from news_extraction import fetch_news
from sentiment_analysis import analyze_sentiment
from comparative_analysis import comparative_analysis
from tts_generation import generate_hindi_audio

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is running!"}

@app.get("/news/{company_name}")
def get_news(company_name: str):
    print(f"✅ Received API request for: {company_name}")  # Debugging

    articles = fetch_news(company_name)
    print(f"✅ Extracted {len(articles)} articles")  # Debugging

    for article in articles:
        article["sentiment"] = analyze_sentiment(article["summary"])

    analysis = comparative_analysis(articles)

    final_text = f"{company_name} की हाल की खबरें ज्यादातर {analysis['Sentiment Distribution']} दिखाती हैं।"
    audio_file = generate_hindi_audio(final_text)

    print(f"✅ Returning API response for {company_name}")  # Debugging
    return {
        "Company": company_name,
        "Articles": articles,
        "Comparative Analysis": analysis,
        "Audio File": audio_file
    }

# Run FastAPI in a separate thread so Gradio doesn’t interfere
import threading
def run_fastapi():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

threading.Thread(target=run_fastapi).start()

# Gradio UI to confirm API is running
with gr.Blocks() as demo:
    gr.Markdown("# ✅ FastAPI is Running at http://127.0.0.1:8000")

demo.launch()

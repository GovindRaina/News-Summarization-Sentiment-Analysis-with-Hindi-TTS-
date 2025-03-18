import streamlit as st
import requests

# Replace with your Hugging Face API URL
API_BASE_URL = "https://your-username-news-summarization-api.hf.space"

st.title("News Summarization & Sentiment Analysis")

company_name = st.text_input("Enter Company Name:")

if st.button("Analyze"):
    api_url = f"{API_BASE_URL}/news/{company_name}"
    
    st.write(f"🔄 Fetching news for: {company_name}...")  # Debugging output

    try:
        response = requests.get(api_url)
        st.write(f"✅ API Status Code: {response.status_code}")  # Show API status

        if response.status_code == 200:
            data = response.json()
            st.write("### News Analysis")

            if not data["Articles"]:
                st.warning("⚠️ No articles found for this company. Try another name.")
            else:
                for article in data["Articles"]:
                    st.write(f"**Title:** {article['title']}")
                    st.write(f"**Summary:** {article['summary']}")
                    st.write(f"**Sentiment:** {article['sentiment']}")
                    st.write("---")

                st.write("### Comparative Analysis")
                st.json(data["Comparative Analysis"])

                if "Audio File" in data:
                    st.audio(data["Audio File"], format="audio/mp3")
        else:
            st.error(f"❌ API request failed! Status Code: {response.status_code}")
    
    except Exception as e:
        st.error(f"🚨 Error fetching data from API: {e}")

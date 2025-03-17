import streamlit as st
import requests

st.title("News Summarization & Sentiment Analysis")

company_name = st.text_input("Enter Company Name:")

if st.button("Analyze"):
    api_url = f"http://127.0.0.1:8000/news/{company_name}"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            
            st.write("### News Analysis")
            for article in data["Articles"]:
                st.write(f"**Title:** {article['title']}")
                st.write(f"**Summary:** {article['summary']}")
                st.write(f"**Sentiment:** {article['sentiment']}")
                st.write("---")  # Adds a separator

            st.write("### Comparative Analysis")
            st.json(data["Comparative Analysis"])

            if "Audio File" in data:
                st.audio(data["Audio File"], format="audio/mp3")
        
        else:
            st.error(f"API request failed! Status Code: {response.status_code}")
    
    except Exception as e:
        st.error(f"Error fetching data from API: {e}")

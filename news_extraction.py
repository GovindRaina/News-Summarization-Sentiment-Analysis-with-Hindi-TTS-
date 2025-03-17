import requests
from bs4 import BeautifulSoup
from newspaper import Article
import time

def fetch_news(company_name):
    """
    Fetches news articles related to the given company from Bing News instead of Google.
    """
    base_url = "https://www.bing.com/news/search?q="
    search_url = base_url + company_name.replace(" ", "+")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch news articles. Status Code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    articles = []
    
    # Extract news links
    news_links = []
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if "http" in href and "bing.com" not in href:
            news_links.append(href)

    # Print extracted news URLs for debugging
    print(f"Extracted {len(news_links)} news URLs: {news_links}")

    # Limit to 10 articles
    news_links = list(set(news_links))[:10]

    for url in news_links:
        try:
            article = Article(url)
            article.download()
            article.parse()
            article.nlp()
            
            articles.append({
                "title": article.title,
                "summary": article.summary,
                "content": article.text,
                "url": url
            })
            print(f"Successfully extracted: {article.title}")

            time.sleep(1)
        except Exception as e:
            print(f"Skipping {url} due to an error: {e}")

    return articles

# Test the function
if __name__ == "__main__":
    test_articles = fetch_news("Tesla")
    print(test_articles)

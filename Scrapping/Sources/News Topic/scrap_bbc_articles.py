import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from datetime import datetime

filename = "BBC_articles_China News.csv"
df = pd.read_csv(filename)

topic = input("Enter topic: ")

article_links = np.array(df["Link"])


article_contents = []
authors = []

i = 1
print("Links...")
for link in article_links:
    try:
        response = requests.get(link)
        print(f"{i} Getting article from link: {link}")
        i += 1
        soup = BeautifulSoup(response.text, "html.parser")

        article_tag = soup.find("article")
        if article_tag:
            paragraphs = article_tag.find_all("p")
            if paragraphs:
                article_text = " ".join([para.get_text() for para in paragraphs])
            else:
                article_text = "No article content found"
        else:
            article_text = "No article tag found"

        article_contents.append(article_text)

        author_element = soup.find("span", class_="sc-2b5e3b35-7 bZCrck")
        if author_element:
            author = author_element.get_text().strip()
        else:
            author = "BBC"
            print("Author not found")

        authors.append(author)

    except Exception as e:
        print(f"Failed to scrape content for {link}: {e}")
        article_contents.append("Content could not be scraped")
        authors.append("BBC")


df["Article_Content"] = article_contents
df["Author"] = authors


output_filename = f"bbc_articles_{topic}.csv"
df.to_csv(output_filename, index=False)

print(f"Updated file saved to {output_filename}")

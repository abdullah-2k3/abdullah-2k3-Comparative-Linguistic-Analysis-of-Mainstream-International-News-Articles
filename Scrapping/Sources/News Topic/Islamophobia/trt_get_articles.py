import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from datetime import datetime

filename = "trt_links.txt"

with open(filename, "r") as file:
    links = file.readlines()

    print(links)

topic = "Islamophobia"

df = pd.read_csv("trt_articles_Islamophobia.csv")

article_contents = []
authors = []

i = 1
for link in links:
    try:
        response = requests.get(link)
        print(f"{i} Getting article from link: {link}")
        i += 1
        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")

        article_text = None
        if paragraphs:
            article_text = " ".join([para.get_text() for para in paragraphs])
        else:
            print("Article not found")

        article_contents.append(article_text)

        author = "TRT World"

        authors.append(author)
        df.loc[df["Link"] == link, "Article"] = article_text

    except Exception as e:
        print(f"Failed to scrape content for {link}: {e}")
        article_contents.append("Content could not be scraped")
        authors.append("Unknown")
        df.loc[df["Link"] == link, "Article"] = article_text


df.to_csv(filename, index=False)

print(f"Updated file saved to {filename}")

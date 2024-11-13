import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

filename = "Dawn_links_merged.csv"
df = pd.read_csv(filename)

article_links = np.array(df["Link"])

article_contents = []
authors = []

i = 1
for link in article_links:
    try:
        response = requests.get(link)
        print(f"{i}. Getting article from link: {link}")
        i += 1

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        article = soup.find("div", class_="story__content")

        paragraphs = article.find_all("p")

        article_text = "\n".join([p.get_text(strip=True) for p in paragraphs])
        if article_text:
            print("Article fetched")
        else:
            print("Could not fetch article text (empty content)")

        article_contents.append(
            article_text if article_text else "No content available"
        )
        authors.append("Dawn News")

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred for {link}: {http_err}")
        article_contents.append("")
    except Exception as e:
        print(f"Failed to scrape content for {link}: {e}")
        article_contents.append("")
        authors.append("Dawn News")


df["Article_Content"] = article_contents


df["Author"] = authors

output_filename = "Dawn_articles.csv"
df.to_csv(output_filename, index=False)

print(f"Updated file saved to {output_filename}")

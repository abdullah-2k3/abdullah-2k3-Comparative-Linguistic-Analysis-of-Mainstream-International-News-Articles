from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from datetime import datetime

url = input("Enter url: ")
topic = input("Enter topic: ")
region = input("Enter region: ")
source = "BBC"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument("--disable-media-session")
chrome_options.add_argument("--disable-extensions")


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=chrome_options
)


driver.get(url)
time.sleep(3)

data = {
    "Source": [],
    "Link": [],
    "Headline": [],
    "Description": [],
    "Date": [],
    "Timestamp": [],
    "Topic": [],
    "Author": [],
    "Region": [],
    "Article_Content": [],
}


def scrape_articles():

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (
                By.CSS_SELECTOR,
                'div[data-testid="liverpool-card"]',
            )
        )
    )

    articles = driver.find_elements(
        By.CSS_SELECTOR, 'div[data-testid="liverpool-card"]'
    )

    for article in articles:
        try:

            link_element = article.find_element(
                By.CSS_SELECTOR, "a[data-testid='internal-link']"
            )
            link = link_element.get_attribute("href")

            headline_element = article.find_element(
                By.CSS_SELECTOR, "h2[data-testid='card-headline']"
            )
            headline = headline_element.text if headline_element else None

            description_element = article.find_element(
                By.CSS_SELECTOR, "p[data-testid='card-description']"
            )
            description = description_element.text if description_element else None

            date_element = article.find_element(
                By.CSS_SELECTOR, "span[data-testid='card-metadata-lastupdated']"
            )
            date = date_element.text if date_element else "Unknown"

            data["Source"].append(source)
            data["Link"].append(link)
            data["Headline"].append(headline)
            data["Description"].append(description)
            data["Date"].append(date)
            data["Timestamp"].append(datetime.now())
            data["Region"].append(region)
            data["Topic"].append(topic)
            data["Article_Content"].append("-")
            data["Author"].append("-")

        except Exception as e:
            print(f"Error scraping article: {e}")


scrape_articles()

for i in range(50):
    try:
        print(f"Page {i+1}...")

        next_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button[data-testid="pagination-next-button"]')
            )
        )

        next_button.click()
        time.sleep(2)

        scrape_articles()

        if (i + 1) % 5 == 0:
            df = pd.DataFrame(data)

            df.to_csv(f"scraped_articles_batch_{i+1}.csv", index=False, mode="a")
            print(f"Data saved to file after {i+1} iterations.")

    except Exception as e:
        print(f"No more pages to scrape or unable to click the next button: {e}")
        break


df = pd.DataFrame(data)
df.to_csv(f"{source}_articles_{topic}.csv", index=False)
print("Articles scraped successfully!")


driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

url = "https://www.aljazeera.com/search/israel"

# Data storage
data = {
    "Source": [],
    "Link": [],
    "Headline": [],
    "Description": [],
    "Timestamp": [],
    "Date": [],
    "Topic": [],
    "Article_content": [],
    "Author": [],
    "Region": [],
}


# Function to scrape articles
def scrape_articles():
    articles = driver.find_elements(By.CLASS_NAME, "gc__content")

    for article in articles:
        try:
            source = "Al Jazeera"

            link_tag = article.find_element(By.CSS_SELECTOR, "h3.gc__title a")
            link = link_tag.get_attribute("href") if link_tag else None

            headline = link_tag.text if link_tag else None

            description_tag = article.find_element(By.CSS_SELECTOR, "div.gc__excerpt p")
            description = description_tag.text if description_tag else None

            timestamp, description = description.split("...")

            date = None

            topic = "General News"
            article_content = "-"
            author = "Al Jazeera"
            region = "Middle East"

            # Append data to the dictionary
            data["Source"].append(source)
            data["Link"].append(link)
            data["Headline"].append(headline)
            data["Description"].append(description)
            data["Timestamp"].append(timestamp)
            data["Date"].append(date)
            data["Topic"].append(topic)
            data["Article_content"].append(article_content)
            data["Author"].append(author)
            data["Region"].append(region)

        except Exception as e:
            print(f"An error occurred while extracting an article: {e}")


# Load the initial page
driver.get(url)

# Wait for the articles to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gc__content"))
)

# Dismiss cookie banner if present
try:
    cookie_banner = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
    )
    cookie_banner.click()
    print("Cookie banner dismissed.")
except Exception as e:
    print(f"No cookie banner found or could not dismiss: {e}")

# Scrape initial set of articles
scrape_articles()


# Function to click the "Show More" button using JavaScript
def click_show_more():
    try:
        print("Trying 'Show More' button...")

        # Scroll to the "Show More" button and ensure it's visible
        show_more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "show-more-button"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", show_more_button)

        # Use JavaScript to click the button (in case Selenium click is blocked)
        driver.execute_script("arguments[0].click();", show_more_button)

        # Wait for new articles to load
        time.sleep(3)  # Adjust this if needed
        scrape_articles()

    except Exception as e:
        print(f"An error occurred while loading more articles: {e}")


# Click "Show More" multiple times to load more articles
try:
    for _ in range(
        5
    ):  # Adjust the range based on how many times you need to load more articles
        click_show_more()
except Exception as e:
    print(f"An error occurred during the 'Show More' process: {e}")

# Save data to CSV
df = pd.DataFrame(data)
filename = "al_jazeera_articles_israel_12_10_24.csv"
df.to_csv(filename, index=False)

print(f"Saved to {filename}")

# Close the WebDriver
driver.quit()

print(df.head())

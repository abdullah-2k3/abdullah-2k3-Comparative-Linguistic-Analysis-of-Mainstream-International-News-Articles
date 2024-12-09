# Linguistic Analysis of News Articles

This project aims to analyze linguistic patterns, sentiment biases, and keyword trends in news articles from mainstream international news sources on selected global topics. It combines web scraping, data analysis, machine learning, and visualization to uncover insights about media coverage and biases.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Dataset](#dataset)  
3. [Methodology](#methodology)  
4. [Features](#features)  
5. [Visualizations](#visualizations)  
6. [Dependencies](#dependencies)  
7. [How to Run the Project](#how-to-run-the-project)  
8. [Results and Insights](#results-and-insights)  
9. [Future Work](#future-work)  

---

## Project Overview

This project investigates sentiment bias and keyword usage across news articles from five prominent sources (BBC, CNN, Al Jazeera, Fox, TRT) on global topics such as:
- Israel War
- Ukraine War
- Islamophobia
- US Elections
- China News

The analysis spans over 5,000 scraped articles, assessing sentiment biases and extracting key insights using advanced machine learning models and visualization techniques.

---

## Dataset

### Sources
- **News Outlets:** BBC, CNN, Al Jazeera, Fox, TRT  
- **Topics:** Israel War, Ukraine War, Islamophobia, US Elections, China News  

### Features
The dataset contains the following fields:
- `Source`: The news outlet publishing the article (e.g., BBC, CNN).  
- `Link`: The URL to the original article.  
- `Headline`: The headline of the article.  
- `Description`: A brief summary of the article.  
- `Timestamp`: Publication date and time of the article.  
- `Region`: Geographic region related to the news.  
- `Author`: The author(s) of the article.  
- `Article_Content`: Full text content of the article.  
- `Sentiment_Bias`: Sentiment classification of the article, derived using fine-tuned transformer models.  
- `Keywords`: Key terms extracted using SHAP for interpretability.

---

## Methodology

1. **Web Scraping**  
   Articles were scraped from the selected sources using **Selenium** and **BeautifulSoup**.  

2. **Data Cleaning**  
   The scraped data was cleaned and formatted to ensure consistency and accuracy.  

3. **Sentiment Bias Classification**  
   - Fine-tuned transformer models (based on Twitter data) were used for sentiment analysis.  
   - Sentiments were categorized as Positive, Neutral, or Negative.  

4. **Keyword Extraction**  
   - Keywords were extracted using **SHAP** (SHapley Additive exPlanations) to understand important terms contributing to sentiment predictions.  

5. **Visualization**  
   - Various visualizations were created to analyze and present trends and biases effectively.

---

## Visualizations

The following visualizations were used to explore and present the data:
- **Bar Charts**: Displaying sentiment bias distribution by source, topic, and region.  
- **Pie Charts**: Representing proportions of sentiment categories (Positive, Neutral, Negative).  
- **Line Charts**: Analyzing temporal trends in sentiment across topics.  
- **Map Charts**: Visualizing regional coverage of news articles.  
- **Word Clouds**: Highlighting frequent keywords for each topic and source.  
- **Bivariate Analysis**: Exploring correlations between different dataset features.

---

## Dependencies

The project requires the following libraries and tools:
- **Web Scraping**: `Selenium`, `BeautifulSoup4`  
- **Data Manipulation**: `pandas`, `numpy`  
- **Machine Learning**: `transformers`, `scikit-learn`, `SHAP`  
- **Visualization**: `matplotlib`, `seaborn`, `wordcloud`, `plotly`  
- **Other**: `nltk`

---

## How to Run the Project

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/linguistic-analysis-news.git
   cd linguistic-analysis-news

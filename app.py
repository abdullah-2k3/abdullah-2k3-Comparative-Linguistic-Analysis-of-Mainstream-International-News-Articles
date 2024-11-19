import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud
from collections import Counter
import os

# Set page configuration
st.set_page_config(page_title="Sentiment Analysis Dashboard", layout="wide")

# Automatically detect the dataset file
for file in os.listdir():
    if file.endswith(".csv"):
        dataset_file = file
        break
else:
    st.error("No CSV file found in the current directory.")
    st.stop()

# Load the dataset
df = pd.read_csv(dataset_file)

# Sidebar for navigation
st.sidebar.title("Dashboard Navigation")
st.sidebar.write("Select a section to view:")

# Dashboard header
st.title("Sentiment Analysis Dashboard")
st.write(f"Using dataset: **{dataset_file}**")

# Dataset preview
st.sidebar.subheader("Dataset Overview")
with st.sidebar.expander("Preview Dataset"):
    st.sidebar.write(df.head())

# Layout
tab1, tab2, tab3 = st.tabs(["Overview Charts", "Detailed Analysis", "Word Cloud"])

# Tab 1: Overview Charts
with tab1:
    st.header("Overview Charts")

    # Use columns to display multiple charts side-by-side
    col1, col2 = st.columns(2)

    with col1:
        # Visualization 1: Overall Bias Distribution (Pie Chart)
        st.subheader("Overall Bias Distribution (Pie Chart)")
        if "Sentiment_Bias" in df.columns:
            colors = ["#66FF66", "#FF3333", "#66B3FF"]
            bias_counts = df["Sentiment_Bias"].value_counts()
            fig, ax = plt.subplots(figsize=(6, 6))
            ax.pie(
                bias_counts,
                labels=bias_counts.index,
                autopct="%1.1f%%",
                startangle=140,
                colors=colors,
            )
            plt.title("Overall Bias Distribution")
            st.pyplot(fig)

    with col2:
        # Visualization 2: Bias by Source
        st.subheader("Bias Distribution by Source")
        if "Source" in df.columns and "Sentiment_Bias" in df.columns:
            bias_source = (
                df.groupby(["Source", "Sentiment_Bias"]).size().unstack(fill_value=0)
            )
            fig, ax = plt.subplots(figsize=(10, 6))
            bias_source.plot(kind="bar", ax=ax)
            plt.title("Bias Distribution by Source")
            plt.ylabel("Number of Articles")
            plt.xlabel("Source")
            st.pyplot(fig)

# Tab 2: Detailed Analysis
with tab2:
    st.header("Detailed Analysis")

    # Use wide layout for heatmap and scatter plots
    st.subheader("Heatmap: Topics vs Sources")
    if (
        "Topic" in df.columns
        and "Source" in df.columns
        and "Sentiment_Bias" in df.columns
    ):
        heatmap_data = df.pivot_table(
            index="Topic",
            columns="Source",
            values="Sentiment_Bias",
            aggfunc="count",
            fill_value=0,
        )
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(heatmap_data, annot=True, cmap="RdBu", linewidths=0.5, ax=ax)
        plt.title("Heatmap: Topics vs Sources")
        st.pyplot(fig)

    # Interactive Scatter Plot
    st.subheader("Scatter Plot: Topics vs Sources by Bias")
    if (
        "Topic" in df.columns
        and "Source" in df.columns
        and "Sentiment_Bias" in df.columns
    ):
        fig = px.scatter(
            df,
            x="Topic",
            y="Source",
            color="Sentiment_Bias",
            title="Topics vs Sources by Bias",
            hover_data=["Region"] if "Region" in df.columns else None,
        )
        st.plotly_chart(fig, use_container_width=True)

    # Choropleth Map
    st.subheader("Choropleth Map: Bias Distribution by Region")
    if "Region" in df.columns and "Sentiment_Bias" in df.columns:
        fig = px.choropleth(
            df,
            locations="Region",
            locationmode="country names",
            color="Sentiment_Bias",
            title="Bias Distribution by Region",
        )
        st.plotly_chart(fig, use_container_width=True)

# Tab 3: Word Cloud and Topic Analysis
with tab3:
    st.header("Word Cloud and Topic Analysis")

    # Use columns for word cloud and topic-specific bias distribution
    col1, col2 = st.columns([2, 1])

    with col1:
        # Word Cloud
        st.subheader("Word Cloud of Article Keywords")
        if "Keywords" in df.columns:
            text = " ".join(df["Keywords"])
            words = text.split()
            word_counts = Counter(words)
            wordcloud = WordCloud(
                width=800,
                height=400,
                background_color="white",
                colormap="Dark2",
                max_words=200,
            ).generate_from_frequencies(word_counts)
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.imshow(wordcloud, interpolation="bilinear")
            ax.axis("off")
            plt.title("Word Cloud of Articles Keywords", fontsize=20)
            st.pyplot(fig)

    with col2:
        # Topic-Specific Bias Analysis
        st.subheader("Topic-Specific Bias Analysis")
        if (
            "Topic" in df.columns
            and "Source" in df.columns
            and "Sentiment_Bias" in df.columns
        ):
            topics = df["Topic"].unique()
            selected_topic = st.selectbox("Select a Topic", topics)
            topic_data = df[df["Topic"] == selected_topic]
            bias_source = (
                topic_data.groupby(["Source", "Sentiment_Bias"])
                .size()
                .unstack(fill_value=0)
            )
            fig, ax = plt.subplots(figsize=(7, 4))
            bias_source.plot(kind="bar", ax=ax)
            plt.title(f"Bias Distribution by Source for Topic: {selected_topic}")
            plt.ylabel("Number of Articles")
            plt.xlabel("Source")
            plt.xticks(rotation=45)
            st.pyplot(fig)

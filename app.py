import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
from collections import Counter
import os

st.set_page_config(page_title="Sentiment Analysis Dashboard", layout="wide")

for file in os.listdir():
    if file.endswith(".csv"):
        dataset_file = file
        break
else:
    st.error("No CSV file found in the current directory.")
    st.stop()

df = pd.read_csv(dataset_file)

st.sidebar.title("Dashboard Navigation")
st.sidebar.write("Select a section to view:")

st.title("Sentiment Analysis Dashboard")
st.write(f"Using dataset: **{dataset_file}**")

st.sidebar.subheader("Dataset Overview")
with st.sidebar.expander("Preview Dataset"):

    rows_per_page = st.sidebar.number_input(
        "Rows per page", min_value=5, max_value=100, value=25, step=5
    )

    if "page" not in st.session_state:
        st.session_state.page = 1

    total_rows = len(df)
    total_pages = (total_rows + rows_per_page - 1) // rows_per_page

    start_idx = (st.session_state.page - 1) * rows_per_page
    end_idx = start_idx + rows_per_page
    st.write(df.iloc[start_idx:end_idx])

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.button("<"):
            st.session_state.page = max(1, st.session_state.page - 1)

    with col3:
        if st.button(">"):
            st.session_state.page = min(total_pages, st.session_state.page + 1)

    with col2:
        st.write(f"Page {st.session_state.page} of {total_pages}")

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
            fig = px.pie(
                names=bias_counts.index,
                values=bias_counts.values,
                color_discrete_sequence=colors,
                title="Overall Bias Distribution",
            )
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Visualization 2: Bias by Source
        st.subheader("Bias Distribution by Source")
        if "Source" in df.columns and "Sentiment_Bias" in df.columns:
            bias_source = (
                df.groupby(["Source", "Sentiment_Bias"])
                .size()
                .reset_index(name="Count")
            )
            fig = px.bar(
                bias_source,
                x="Source",
                y="Count",
                color="Sentiment_Bias",
                title="Bias Distribution by Source",
                barmode="group",
            )
            st.plotly_chart(fig, use_container_width=True)

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
        ).reset_index()
        fig = px.imshow(
            heatmap_data.iloc[:, 1:],
            labels=dict(x="Source", y="Topic", color="Count"),
            x=heatmap_data.columns[1:],
            y=heatmap_data["Topic"],
            title="Heatmap: Topics vs Sources",
            color_continuous_scale="RdBu",
        )
        st.plotly_chart(fig, use_container_width=True)

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
            st.image(wordcloud.to_array(), caption="Word Cloud of Articles Keywords")

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
                .reset_index(name="Count")
            )
            fig = px.bar(
                bias_source,
                x="Source",
                y="Count",
                color="Sentiment_Bias",
                title=f"Bias Distribution by Source for Topic: {selected_topic}",
                barmode="group",
            )
            st.plotly_chart(fig, use_container_width=True)

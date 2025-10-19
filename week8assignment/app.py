import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.title("CORD-19 Research Analysis")

#load the data
@st.cache_data
def load_data():
    df = pd.read_csv("data/metadata.csv", low_memory=False)
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df.dropna(subset=['title', 'publish_time'])

df = load_data()

st.sidebar.header("Filters")
year = st.sidebar.slider("Select Year", int(df['year'].min()), int(df['year'].max()), int(df['year'].max()))
filtered_df = df[df['year'] == year]

st.write(f"### Number of Papers Published in {year}: {filtered_df.shape[0]}")


#below are visualizations
#publications per year
st.subheader("Publications Over Time")
papers_per_year = df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=papers_per_year.index, y=papers_per_year.values, ax=ax)
st.pyplot(fig)

# top Journals
st.subheader("Top 10 Journals")
top_journals = df['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax)
st.pyplot(fig)

# word Cloud
st.subheader("Word Cloud of Titles")
text = ' '.join(df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)
plt.show()

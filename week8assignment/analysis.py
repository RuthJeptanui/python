import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import streamlit as st






#loading data
df=pd.read_csv('data/metadata.csv')

#display data
print(df.head())
print(df.info())
print(df.shape)


#checking dataframe dimensions
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

#check data types
print("\nData types of each column:")
print(df.dtypes)

#checking missing values
important_columns = ['title', 'abstract', 'authors', 'publish_time', 'journal']
print("\nMissing values in important columns:")
print(df[important_columns].isnull().sum())

#basic statistics
print("\nBasic statistics for numerical columns:")
print(df.describe())

#handling missing values
df_cleaned = df.copy()
df_cleaned = df_cleaned.dropna(subset=['title', 'publish_time'])

#convert date columns
df_cleaned['publish_time'] = pd.to_datetime(df_cleaned['publish_time'], errors='coerce')
df_cleaned['year'] = df_cleaned['publish_time'].dt.year

#create new columns
df_cleaned['abstract_word_count'] = df_cleaned['abstract'].fillna('').apply(lambda x: len(x.split()))

#visualizations
papers_per_year = df_cleaned['year'].value_counts().sort_index()
sns.barplot(x=papers_per_year.index, y=papers_per_year.values)
plt.title('Number of Publications Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Papers')
plt.show()


# Top journals
top_journals = df_cleaned['journal'].value_counts().head(10)
sns.barplot(y=top_journals.index, x=top_journals.values)
plt.title('Top 10 Journals Publishing COVID-19 Research')
plt.xlabel('Number of Papers')
plt.ylabel('Journal')
plt.show()

text = ' '.join(df_cleaned['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Most Common Words in Paper Titles')
plt.show()


#paper sources
source_counts = df_cleaned['source_x'].value_counts().head(10)
sns.barplot(y=source_counts.index, x=source_counts.values)
plt.title('Top Sources in the Dataset')
plt.xlabel('Number of Papers')
plt.ylabel('Source')
plt.show()
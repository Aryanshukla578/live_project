import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px

# Function to scrape data from multiple websites
def scrape_data(urls):
    all_data = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        headlines = soup.find_all('h2')  # Adjust according to website's structure
        data = [headline.get_text() for headline in headlines]
        all_data.extend(data)
    return pd.DataFrame(all_data, columns=['Headline'])

# List of URLs
urls = [
    'https://edmonton.ctvnews.ca/',
    'https://vancouver.ctvnews.ca/',
    # Add more URLs as needed
]

# Scrape data from the provided URLs
df = scrape_data(urls)

# Function to visualize data using Plotly
def visualize_data(df):
    fig = px.histogram(df, x='Headline', title='News Headlines Frequency', width=800, height=400)
    fig.update_xaxes(title_text='Headlines')
    fig.update_yaxes(title_text='Frequency')
    fig.show()

# Visualize the data
visualize_data(df)

import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Load data (replace 'Hindi_TV_Serials.csv' with your CSV file containing TV serial data)
df = pd.read_csv('Hindi_TV_Serials.csv')

# Function to search TV shows using the TVMaze API
def search_tv_shows(query):
    url = f"http://api.tvmaze.com/search/shows?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data  # Return JSON data containing search results
    else:
        return None

# Streamlit app
def main():
    st.title('TV Serial Recommender with TVMaze API')

    # Dropdown widget for selecting TV serial
    tv_serial_name = st.selectbox('Select TV Serial', df['Name'])

    if st.button('Search'):
        if tv_serial_name:
            # Search for TV shows based on the selected name
            search_results = search_tv_shows(tv_serial_name)

            if search_results:
                st.subheader(f'Search Results for "{tv_serial_name}":')

                for result in search_results:
                    show = result.get('show', {})
                    show_name = show.get('name', 'Unknown')
                    show_summary = show.get('summary', 'No summary available')
                    show_image = show.get('image', {}).get('medium', None)

                    st.subheader(show_name)
                    st.write(show_summary)

                    if show_image:
                        st.image(show_image, caption=show_name, width=200)
                    else:
                        st.write('No image available')
            else:
                st.write(f"No results found for '{tv_serial_name}'")
        else:
            st.warning('Please select a TV Serial')

if __name__ == '__main__':
    main()

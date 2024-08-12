from bs4 import BeautifulSoup
import requests
import streamlit as st
import toml
import os

def load_theme_config():
    #Loads theme configuration from the config.toml file.
    config_file_path = os.path.join(os.path.dirname(__file__), ".streamlit", "config.toml")
    if os.path.exists(config_file_path):
        with open(config_file_path, "r") as f:
            return toml.load(f)
    return None

def main(location, doctor):
    url = f'https://www.practo.com/search/doctors?results_type=doctor&q=%5B%7B%22word%22%3A%22{doctor}%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%5D&city={location}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    try:
        heading = soup.find('h1', class_='u-xx-large-font u-bold')
        return heading.text, url
    except:
        heading = 'No results found!'

    return heading, url

def gui():
    st.set_page_config(page_title='Practo.com', page_icon='⭐')
    st.title('✨Web Scraping - Practo.com✨')
    st.write('')
    location = st.text_input('Enter your location:')
    
    doctor = st.selectbox('Doctor Type:', ['Dentist', 'General Physician', 'Gynecologist', 'Dermatologist', 'Homeopath', 'Ayurveda'])

    st.write('')
    if st.button('Search'):
        heading, url = main(location, doctor)
        st.subheader(heading)
        # st.write('You can find the details of doctors here: ', url)

if __name__ == '__main__':
    gui()
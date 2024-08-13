# Practo Scraper using Streamlit

This project is a web application built using the Streamlit framework to scrape and display the number of doctors available on [Practo.com](https://www.practo.com) based on user input. The user can enter a location and choose a doctor specialization from a dropdown menu. Upon clicking the search button, the application scrapes the Practo website and returns the number of doctors available for the specified location and specialization.

![image](https://github.com/user-attachments/assets/cb106e22-d330-405d-8d87-d663874314c6)

## Project Structure:

`main.py` : The main Streamlit application which contains web scraping logic as well.
`requirements.txt` : List the python dependencies for the project.

## Dependencies
`Streamlit`: For building the web interface.
`BeautifulSoup`: For scraping HTML data from Practo.
`Requests`: For making HTTP requests to Practo.

## Features:

- **Location Input**: Users can enter the desired location (e.g., city, region) where they want to search for doctors.
- **Doctor Specialization Dropdown**: A dropdown menu allows users to select the type of doctor or specialization (e.g., Cardiologist, Dermatologist).
- **Search Functionality**: After entering the location and selecting a doctor type, the user can click the search button to retrieve the number of doctors available on Practo for that location and specialization.
- **Real-time Data**: The application fetches data in real-time from Practo, ensuring the information is up-to-date.

## Installation:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/practo-scraper.git
   cd practo-scraper

2. **Install dependencies:**
  pipenv install -r requirements.txt

## Run the Application:

streamlit run main.py

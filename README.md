# CIS1051's Final Project: Python Weather App

A simple and interactive web application that retrieves real-time weather information and displays a dynamic map for any searched location.

## Description

This project is a Flask-based Python Weather App that uses the OpenWeatherMap API to deliver up-to-date weather conditions for any city in the world. Users can view key information such as temperature, “feels like” temperature, humidity, wind speed, and visibility. Alongside the weather details, the application also generates an interactive map of the selected location using the Folium library.

I chose this project because weather applications combine real-time data retrieval, API integration, and visual presentation, allowing me to practice working with external data sources, environment variables, and web frameworks. Building this app strengthened my understanding of full-stack Python development while creating something practical and visually engaging.

### Dependencies

Before running the program, ensure you have the following:
- Python libraries (also listed in the "requirements.txt"):
  - requests
  - python-dotenv
  - os (built-in)
  - dataclasses
  - flask
  - folium
- An OpenWeatherMap API key
- A .env file stored locally with your key

### Installing

1. Download the project files
2. Create a .env file in the project folder with the following format:
```
API_KEY=your_openweathermap_api_key_here
```
3. Install the required libraries

### Executing program

To run the application:
1. Open your terminal or command prompt.
2. Navigate to the project folder.
3. Run the file "app.py".
4. Follow the link to open your browser.
From here, enter any city name to view its real-time weather and corresponding map.

## Acknowledgments

Inspiration: https://www.youtube.com/watch?v=JCD7YdOSsWI

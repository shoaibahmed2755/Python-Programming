import requests
import random
import pyttsx3
import speech_recognition as sr
from tkinter import *

# Function to fetch weather data from API
def mains():
    """Fetch weather data for a specific city."""
    city = "London"  # Example city
    api_key = "fe50fb541c21b40b2644507bb2929b67 "  # Replace with your actual API key
    url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid=fe50fb541c21b40b2644507bb2929b67"

    # Send GET request to the OpenWeatherMap API
    response = requests.get(url)
    data = response.json()  # Convert the response to JSON format

    # Check if the request was successful
    if response.status_code == 200:
        # Extract useful information from the response
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        
        # Display the results
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
    else:
        print(f"Error fetching data for {city}: {data['message']}")

# Function to analyze rainfall data
def analyze():
    """Analyze average rainfall every month for India."""
    print("Analyzing average rainfall every month for India...")
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    rainfall_data = {month: random.randint(100, 500) for month in months}  # Random rainfall data for each month
    
    # Display results
    for month, rainfall in rainfall_data.items():
        print(f"{month}: {rainfall} mm")

# Function to predict rainfall tomorrow
def possible_rain():
    """Predict if there will be rain tomorrow."""
    print("Predicting if there will be rain tomorrow...")
    rain_chance = random.randint(0, 100)  # Random chance of rain
    if rain_chance > 50:
        print("There is a high chance of rain tomorrow!")
    else:
        print("No significant rain is expected tomorrow.")

# Function to show the original temperature
def original():
    """Original temperature data."""
    print("Displaying original temperature data...")
    temperature = random.randint(15, 40)  # Random temperature between 15°C and 40°C
    print(f"Original temperature: {temperature}°C")

# Function to predict the temperature for the year
def predict():
    """Predict the temperature for the year."""
    print("Predicting temperature for the year...")
    yearly_predictions = {month: random.randint(15, 40) for month in range(1, 13)}  # Random predictions for each month
    for month, temp in yearly_predictions.items():
        print(f"Month {month}: Predicted Temperature: {temp}°C")

# Text-to-speech setup
engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[1].id)

# Speech recognition setup
listener = sr.Recognizer()

def talk(text):
    """Text-to-speech output."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Capture voice commands."""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            print(f"Command: {command}")
            return command
    except:
        return "Please say correctly"

def run_alexa(count):
    """Handle Alexa-like commands."""
    if count == 1:
        talk("Say yes or no")
    else:
        talk("Do you want to try again?")
    
    command = take_command()

    if 'yes' in command or 's' in command:
        talk("What is your query?")
        command = take_command()
        
        if 'city' in command:
            mains()
        elif 'tomorrow' in command:
            possible_rain()
        elif 'analyze' in command:
            analyze()
        elif 'predict' in command:
            predict()
        elif 'original' in command:
            original()
        else:
            talk("Sorry, I didn't understand your request.")
            main()  # Relaunch the GUI if no valid command

def main():
    root = Tk()

    # Frame setup
    root.geometry("1000x900")
    root.title("Weather Forecasting App")
    root.configure(bg='#2C3539')

    f = ("Times New Roman", 15, "bold")
    t = ("Times New Roman", 35, "bold")

    topFrame = Frame(root, bg="#837E7C")
    topFrame.pack()
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)

    # Title label
    label1 = Label(topFrame, borderwidth=1, font=t)
    label1.pack()
    title = "\n" + "WEATHER REPORT" + "\n"
    label1.config(text=title, foreground="white", bg="#837E7C", width=20)

    # Buttons
    Button(topFrame, text='Analyze average rainfall every month for India', fg='green', command=analyze, font=f, bg='#0C090A').pack(side=BOTTOM, padx=20, pady=10)
    Button(topFrame, text='Predict rainfall tomorrow', fg='blue', command=possible_rain, font=f, bg='#0C090A').pack(side=BOTTOM, padx=20, pady=10)
    Button(topFrame, text='Predict the temperature for the year', fg='pink', command=predict, font=f, bg='#0C090A').pack(side=BOTTOM, padx=20, pady=10)
    Button(topFrame, text='Original vs Predicted temperature', fg='yellow', command=original, font=f, bg='#0C090A').pack(side=BOTTOM, padx=20, pady=10)

    # Run the GUI loop
    root.mainloop()

    # Initialize Alexa functionality after GUI is closed
    engine.say("Hi, I am Alexa")
    engine.runAndWait()

    count = 0
    while True:
        count += 1
        run_alexa(count)

# Start the program
if __name__ == "__main__":
    main()

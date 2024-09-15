import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime

api_key = "00ee7d7ade9e948cb8cdf771e9528d49"

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            raise Exception(data["message"])

        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        return temperature, weather_description, humidity, wind_speed
    except Exception:
        raise Exception(f"Error retrieving weather data: ")

def update_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    
    try:
        temperature, weather_description, humidity, wind_speed = get_weather(city)
        result = (f"City: {city}\n"
                  f"Temperature: {temperature} °C\n"
                  f"Weather: {weather_description.capitalize()}\n"
                  f"Humidity: {humidity}%\n"
                  f"Wind Speed: {wind_speed} m/s")
        
        weather_label.config(text=result)
    except Exception as e:
        messagebox.showerror("Error", str(e))
root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter city:")
city_label.pack(pady=5)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", command=update_weather)
get_weather_button.pack(pady=5)

weather_label = tk.Label(root, text="", font=("Helvetica", 12))
weather_label.pack(pady=10)

root.geometry("400x300")
root.resizable(True, True)

root.mainloop()

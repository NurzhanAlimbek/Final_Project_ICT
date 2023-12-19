import requests
import tkinter as tk


def get_weather():
    city = city_entry.get()
    api_key = "b89ad9533279fd96d15eaba13dbc7eec"  
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)
    data = response.json()

    weather_desc = data["weather"][0]["description"]
    temperature = data["main"]["temp"]

    result_label.config(text=f"Погода: {weather_desc}\nТемпература: {temperature} °C")


app = tk.Tk()
app.title("Погодное приложение")

city_label = tk.Label(app, text="Введите город:")
city_entry = tk.Entry(app)
get_weather_button = tk.Button(app, text="Узнать погоду", command=get_weather)
result_label = tk.Label(app, text="")

city_label.pack(pady=10)
city_entry.pack(pady=10)
get_weather_button.pack(pady=10)
result_label.pack(pady=10)

app.mainloop()
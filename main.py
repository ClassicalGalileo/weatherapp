import tkinter as tk
import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        result = {}
        result['city'] = city
        result['description'] = weather['description']
        result['temperature'] = main['temp']
        result['humidity'] = main['humidity']
        result['pressure'] = main['pressure']
        result['weather_main'] = weather['main']
        return result
    else:
        return f"Error fetching data. Status code: {response.status_code}"

def show_weather(event=None):
    city = city_entry.get()
    api_key = "you_api_key"
    weather_info = get_weather(city, api_key)
    if isinstance(weather_info, dict):
        city_label.config(text=weather_info['city'])
        weather_text = f"Weather: {weather_info['description']}\n"
        weather_text += f"Temperature: {weather_info['temperature']}°C\n"
        weather_text += f"Humidity: {weather_info['humidity']}%\n"
        weather_text += f"Pressure: {weather_info['pressure']} hPa\n"
        weather_label.config(text=weather_text)
        
        if weather_info['weather_main'] == "Clear":
            bg_color = '#0066cc'
        elif weather_info['weather_main'] == "Clouds":
            if 'few' in weather_info['description'].lower():
                bg_color = '#aec2e0'
            else:
                bg_color = 'grey'
        elif weather_info['weather_main'] == "Rain":
            bg_color = 'dark grey'
        else:
            bg_color = 'light grey'
        
        root.config(bg=bg_color)
        city_label.config(bg=bg_color)
        weather_label.config(bg=bg_color)
        submit_button.config(bg=bg_color, activebackground=bg_color)
    else:
        messagebox.showerror("Error", weather_info)

root = tk.Tk()
root.title("Weather App")
root.geometry("250x300")

city_label = tk.Label(root, font=("Courier", 20, 'bold'), fg='white')
city_label.pack()
city_label.place(relx=0.5, y=18, anchor='n')

city_entry = tk.Entry(root, font=("Courier", 14))
city_entry.pack()
city_entry.place(relx=0.5, rely=0.4, anchor='center')
city_entry.bind('<Return>', show_weather)

submit_button = tk.Button(root, text="Get Weather", font=("Courier", 10), command=show_weather)
submit_button.pack()
submit_button.place(relx=0.5, rely=0.5, anchor='center')

weather_label = tk.Label(root, font=("Courier", 14), fg='white')
weather_label.pack()
weather_label.place(relx=0.5, rely=0.8, anchor='center')

root.mainloop()

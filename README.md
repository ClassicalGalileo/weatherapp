# Weather App
Weather app is a simple python Weather App for your desktop that I have written, where the script creates a simple graphical user interface (GUI) for a weather application using Tkinter, a Python library for creating GUIs. It fetches weather data for a specific city from the OpenWeatherMap API and displays it on the GUI.

The script is structured into several sections:

  #**Imports:** The script imports the necessary modules tkinter and requests. The tkinter module is used to create the GUI, while the requests module is used to send HTTP requests to the OpenWeatherMap API.

 #**get_weather Function:** This function sends a GET request to the OpenWeatherMap API with the city name and API key as parameters. The API responds with a JSON object that includes various weather data for the city. The function parses this data and returns it as a dictionary. If there's an error in the request, it returns an error message instead.

  #**show_weather Function:** This function takes an optional event argument. It is invoked when the user presses the Enter key in the input field or clicks the "Get Weather" button. The function fetches the weather data by calling get_weather with the city entered by the user. It then updates the GUI with this data, changing the text of several labels and the background color of the window, labels, and button depending on the weather conditions.

  #**Tkinter GUI Setup:** This section sets up the main elements of the GUI. It creates a window with a Canvas for drawing, an Entry for the user to input the city name, a Button to fetch the weather data, and several Labels to display the city name and weather data. The button and entry are bound to the show_weather function, so that when the user interacts with them, it triggers the function.

  #**Main Event Loop:** The call to root.mainloop() at the end of the script starts the Tkinter event loop, which waits for user interaction and responds to events like button clicks and key presses.

  This script provides a simple yet interactive way to fetch and display weather data for any city. The changing colors and font styles in response to the weather conditions make it a dynamic and visually appealing tool for checking the weather.

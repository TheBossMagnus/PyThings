import requests
location = input("Enter the city name: ")

def GetWeather(location):
    # Set the URL for the API endpoint
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&APPID=c2c9eba87cb102eaba0a32b117cc7a68"

    # Make the request to the API and convert the response to JSON
    response = requests.get(url)
    response = response.json()

    if response["cod"] != "404":

        #extract data from the response
        temperature = response["main"]["temp"]
        pressure = response["main"]["pressure"]
        humidity = response["main"]["humidity"]
        weather_description = response["weather"][0]["description"]

        #print the data
        print(f"temperature:{temperature}")
        print(f"pressure:{pressure}")
        print(f"humidity:{humidity}")
        print(f"weather:{weather_description}")

    else:
        print(" City Not Found ")
GetWeather(location)
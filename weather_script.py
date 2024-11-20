import requests

# Replace with your own API key
API_KEY = '4bcafd8945f202afd375949c7ef1'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    # Construct the final URL
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        
        # Extract and print the relevant information
        print(f"City: {data['name']}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Weather: {weather['description']}")
        print(f"Humidity: {main['humidity']}%")
        print(f"Pressure: {main['pressure']} hPa")
    else:
        print("Error in the HTTP request")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
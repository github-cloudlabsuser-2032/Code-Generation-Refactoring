from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

#4bcafd8945f202afd375949c7ef1 Replace with your own API key
API_KEY = '4bcafd8945f202afd375949c7ef1'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch weather data'}), response.status_code

    data = response.json()
    return jsonify({
        'city': data['name'],
        'temperature': data['main']['temp'],
        'weather': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'pressure': data['main']['pressure']
    })

if __name__ == '__main__':
    app.run(debug=True)
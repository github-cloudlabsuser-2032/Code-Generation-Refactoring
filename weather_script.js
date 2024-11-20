// Replace with your own API key
const API_KEY = 'your_api_key_here';
const BASE_URL = 'http://api.openweathermap.org/data/2.5/weather';

async function getWeather(city) {
    const url = `${BASE_URL}?q=${city}&appid=${API_KEY}&units=metric`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        const main = data.main;
        const weather = data.weather[0];

        console.log(`City: ${data.name}`);
        console.log(`Temperature: ${main.temp}°C`);
        console.log(`Weather: ${weather.description}`);
        console.log(`Humidity: ${main.humidity}%`);
        console.log(`Pressure: ${main.pressure} hPa`);
    } catch (error) {
        console.error('There has been a problem with your fetch operation:', error);
    }
}

const city = prompt("Enter city name: ");
getWeather(city);
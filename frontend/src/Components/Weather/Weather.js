import './Weather.css';
import React, { useState } from 'react';
const api = {
  key: "63500e07fa46d117e3af8e5b01ba213f",
  base: "https://api.openweathermap.org/data/2.5/"
}

function Weather() {
  const [query, setQuery] = useState('');
  const [weather, setWeather] = useState({}); 

  const search = evt => {
    if (evt.key === "Enter") {
      fetch(`${api.base}weather?q=${query}&units=metric&APPID=${api.key}`)
        .then(res => res.json())
        .then(result => {
          setWeather(result);
          setQuery('');
          console.log(result);
        });
    }
  }

  const dateBuilder = (d) => {
    let months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    let days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

    let day = days[d.getDay()];
    let date = d.getDate();
    let month = months[d.getMonth()];
    let year = d.getFullYear();

    return `${day} ${date} ${month} ${year}`
  }

  return (
    <div className="app">
      <main>
        <div className="search-box">
          <input 
            type="text"
            className="search-bar"
            placeholder="Search..."
            onChange={e => setQuery(e.target.value)}
            value={query}
            onKeyPress={search}
          />
        </div>
        
        {(typeof weather.main != "undefined") ? (
        <div>
          <div className="location-box">
            <div className="location">{weather.name}, {weather.sys.country}</div>
            <div className="date">{dateBuilder(new Date())}</div>
          </div>
          <div className="weather-box">
            <div className="temp">
              {Math.round(weather.main.temp)}°c
            </div>
            <div className="weather">{weather.weather[0].main}</div>
          </div>

          <div className="bottom-box">
          <div className="MaxTmp">
              <p className='bold'>{Math.round(weather.main.temp_max)}°C</p>
              <p>Max temp</p>
            </div>
            <div className="MinTemp">
              <p className='bold'>{Math.round(weather.main.temp_min)}°C</p>
              <p>Min temp</p>
            </div>
            <div className="humidity">
              <p className='bold'>{weather.main.humidity}%</p>
              <p>Humidity</p>
            </div>
            <div className="wind">
               <p className='bold'>{Math.round(weather.wind.speed)} MPH</p>
               <p>Wind Speed</p>
            </div>
          </div>
      </div>
        ) : ('')}
      </main>
    </div>
  );
}

export default Weather;

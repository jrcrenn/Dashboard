function weather() {
    var apiKey = 'cc7c753a9a8f1cb76abaf5628b753512';
    var city = document.getElementById("city").value;
    $.ajax({
        url: 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=' + apiKey,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            currentWeather = {
                'main': {
                    'humidity': data.main.humidity,
                    'temp': data.main.temp,
                    'temp_min': data.main.temp_min,
                    'temp_max': data.main.temp_max
                },
                'wind': { 
                    'speed': data.wind.speed
                },
                'weather': {
                    'description': data.weather[0].description
                },
                'name': data.name
            }
            if (currentWeather.main != undefined) {
                let strCity = `City : ${currentWeather.name}`;
                let strTemp = `Current temperature : ${currentWeather.main.temp}`;
                let strMinMax = `Temp min : ${currentWeather.main.temp_min} <br\>
                                                                Temp max : ${currentWeather.main.temp_max}`;
                let strWind = `Wind speed : ${currentWeather.wind.speed}`;
                let strDesc = `Description : ${currentWeather.weather.description}`;
                document.getElementById("weatherCity").innerHTML = strCity;
                document.getElementById("temp").innerHTML = strTemp;
                document.getElementById("tempMinMax").innerHTML = strMinMax;
                document.getElementById("wind").innerHTML = strWind;
                document.getElementById("desc").innerHTML = strDesc;
            } else {
                document.getElementById("weatherDisplay").innerHTML = 'City doesn\'t exist';
            }
        }
    })
}
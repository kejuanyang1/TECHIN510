import requests
from datetime import datetime

# Use OpenStreeetMap API to get (lat, lon) based on location name
def get_lat_lon(location):
    query_params = {
        "q": location,
        "format": "jsonv2"
    }
    response = requests.get("https://nominatim.openstreetmap.org/search.php", params=query_params)
    data = response.json()
    if data:  # Check if data is not empty
        return data[0]['lat'], data[0]['lon']
    else:
        print(f"No data found for location: {location}")
        return None, None

# Loop up the weather
def get_weather(lat, lon, date):
    weather_dict = {
        "condition": None,
        "temperature": None,
        "wind": None
    }
    try:
        target_date = datetime.strptime(date.split('T')[0], '%Y-%m-%d')

        # Get the API URL for the specific point
        url = f"https://api.weather.gov/points/{lat},{lon}"
        res = requests.get(url)
        point_dict = res.json()

        # Check if 'properties' key is present
        if 'properties' in point_dict:
            forecast_url = point_dict['properties']['forecast']
            res = requests.get(forecast_url)
            forecast_data = res.json()

            # Search for the weather on the target date
            if 'properties' in forecast_data and 'periods' in forecast_data['properties']:
                for period in forecast_data['properties']['periods']:
                    period_start = datetime.strptime(period['startTime'].split('T')[0], '%Y-%m-%d')
                    if period_start.date() == target_date.date():
                        weather_dict['condition'] = period['shortForecast']
                        weather_dict['temperature'] = period['temperature']
                        weather_dict['wind'] = period['windSpeed'] + ' ' + period['windDirection']
                        return weather_dict
            else:
                print("Weather data not available for the specified date.")
        else:
            print("Failed to retrieve forecast URL.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_location(loc):
    # Update the 'Region' value
    if loc == 'Downtown':
        loc = 'Seattle Downtown'
    elif loc == 'South':
        loc = 'South Seattle'
    elif loc == 'North':
        loc = 'North Seattle'
    elif loc == 'West':
        loc = 'West Seattle'
    return loc

if __name__ == '__main__':
    ## for test
    lat, lon = get_lat_lon("Seattle Downtown")
    weather_data = get_weather(lat, lon, "2024-03-19T00:00:00-08:00")
    print(weather_data)
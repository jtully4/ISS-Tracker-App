import requests
import time

def get_isslocation():

    req = requests.get("http://api.open-notify.org/iss-now.json")
    data = req.json()

    
    lat = float(data['iss_position']['latitude'])
    lon = float(data['iss_position']['longitude'])
    return lat,lon


def get_userlocation(city):
    api_key = """users API KEY"""

    base_url = ("http://api.openweathermap.org/geo/1.0/direct?")

    params = {"q":city, "appid":api_key}

    response = requests.get(base_url, params = params)
    data = response.json()

    country = data[0]['country']
    my_lat = data[0]['lat']
    my_lon = data[0]['lon']

    print(city_input, country)
    return my_lat, my_lon

def compare_isslocation(lat, lon, my_lat, my_lon):
    
    if (abs(my_lat - lat) <= 5 and abs(my_lon - lon) <= 5):
        
        return True

city_input = input("Please enter your City: ")    
lat, lon = get_isslocation()
my_lat, my_lon = get_userlocation(city_input)



while True:
    time.sleep(60)
    lat, lon = get_isslocation()
    if compare_isslocation(lat, lon, my_lat, my_lon):
        print(my_lat, my_lon)
        print(lat, lon)
        print("The ISS is overhead!")
    else:
        print("The ISS is out of range")
        print(my_lat, my_lon)
        print(lat, lon)


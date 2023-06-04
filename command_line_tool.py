##import libraries
import requests
import argparse
##add error handling
import sys  ##system error

##add OS system variables
import os

##write sample function to get user data from sample api endpoint /api/users/{user_id} with error handling and json data parsing
# def get_user(user_id):
#     ##get OS system variables
#     OS = os.environ.get("OS")
    
#     url = "https://reqres.in/api/users/{}".format(user_id)
#     ##try and catch error
#     try:
#         r = requests.get(url)
#         if r.status_code == 200:
#             return r.json()
#         else:
#             print("Error: {}".format(r.status_code))
#             sys.exit(1)
#     except requests.exceptions.RequestException as e:
#         print(e)
#         sys.exit(1)
#     except KeyboardInterrupt:
#         print("Keyboard interrupt")
#         sys.exit(1)
#     except:
#         print("Unknown error")
#         sys.exit(1)

## call openweather api to get weather data for city with error handling
def get_weather(city):  

    ## get OS system variables
    OS = os.environ.get("OS")
    
    api_key = "08254dd5b04494349bfe5194d7f1f3ee"
    
    
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)
    ##try and catch error
    
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        else:
            print("Error: {}".format(r.status_code))
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        sys.exit(1)
    except:
        print("Unknown error")
        sys.exit(1)
        
## print weather data
def print_weather(weather):
    
    print("City: {}".format(weather["name"]))
    print("Weather: {}".format(weather["weather"][0]["main"]))
    print("Description: {}".format(weather["weather"][0]["description"]))
    print("Temperature: {}°C".format(weather["main"]["temp"] - 273.15))
    print("Pressure: {}".format(weather["main"]["pressure"]))
    print("Humidity: {}".format(weather["main"]["humidity"]))
    print("Wind speed: {}".format(weather["wind"]["speed"]))
    print("Wind direction: {}".format(weather["wind"]["deg"]))
    print("Clouds: {}".format(weather["clouds"]["all"]))
    print("Country: {}".format(weather["sys"]["country"]))
    print("Sunrise: {}".format(weather["sys"]["sunrise"]))
    print("Sunset: {}".format(weather["sys"]["sunset"]))
    
## get weather data for city and print it
def get_weather_and_print(city):
    weather = get_weather(city)
    print_weather(weather)
    
    


## command line tool

def main(): 
    parser = argparse.ArgumentParser()
    parser.add_argument("city", help="City name")
    args = parser.parse_args()
    get_weather_and_print(args.city)
    
if __name__ == "__main__":
    main()
    
## run command line tool
## python command_line_tool.py "city name"
## python command_line_tool.py "London"
## python command_line_tool.py "New York"
## python command_line_tool.py "Tokyo"
## python command_line_tool.py "Sydney"
## python command_line_tool.py "Paris"
## python command_line_tool.py "Berlin"
## python command_line_tool.py "Madrid"
import requests

city = input("Enter city name: ")


url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url)
    data = response.json()

 
    temp = data["current_condition"][0]["temp_C"]
    humidity = data["current_condition"][0]["humidity"]
    weather_desc = data["current_condition"][0]["weatherDesc"][0]["value"]

    print("\n--- Weather Information ---")
    print("City:", city)
    print("Temperature:", temp, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", weather_desc)

except Exception as e:
    print("Error fetching data:", e)

import requests

stop = False
key = 'key'
temperature_units = 'metric'
language = 'en'

while stop == False:
    
    print('1 - Check weather')
    print('2 - Settings')
    print('3 - Exit')
    
    action = int(input('Enter number: '))

    if action == 1:
        city = input('Enter city: ')
        resp = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units={temperature_units}')
        data = resp.json()
        print(f"Weather description: {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']}")
        print(f"Windiness: {data['wind']['speed']}")
        print(f"Humidity: {data['main']['humidity']}")

    elif action == 2:
        print('1 - Set temperature')
        print('2 - Set language')
        action_settings = int(input("Enter number: "))
        if action_settings == 1:
            print('1 - celsius')
            print('2 - kelvin')
            print('3 - fahrenheit')
            num = int(input('Enter num: '))
            if num == 1:
                temperature_units = 'metric'
            elif num == 2:
                temperature_units = 'standard'
            elif num == 3:
                temperature_units = 'imperial'

        elif action_settings == 2:
            print('1 - English')
            print('2 - Russian')
            print('3 - Polish')
            num = int(input('Enter num: '))
            if num == 1:
                language = 'en'
            elif num == 2:
                language = 'ru'
            elif num == 3:
                language = 'pl'

    elif action == 3:
        stop = True

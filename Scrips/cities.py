import json 
with open('users.json') as file:
    data = json.load(file)
    file.close
    for address in data:
        city = address['address']
        print('City:', city['city'])
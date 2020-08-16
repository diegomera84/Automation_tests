#!/usr/bin/python3
"""Script to create a json file from appropriate wikipedia pages"""
from urllib.request import urlopen
from html2json import collect
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              


page = str(input("Search en Wikipedia: "))
response = urlopen("https://en.wikipedia.org/wiki/Organism")
data = str(response.read(), 'utf-8')
data_json = collect(data, ())
#with open('data.txt', 'w') as outfile:
 #   json.dump(data, outfile)
new_file = open("new_file.json", 'w')
new_file.write(data_json)
new_file.close()
print(data)
LLLñWK                                                                                                                                                                                                                                                                                


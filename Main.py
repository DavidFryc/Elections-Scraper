"""
Main.py: Treti projekt do Engeto Online Python Akademie
author: David Fryc
email: df@emd.dk
discord: David F.#2019
"""

import requests
import bs4
import sys
#from pprint import pprint
import os
import re
import pprint

os.system('cls')

print(sys.argv)

#if len(sys.argv) != 3:
#    print("Zadej tri argumenty")

# DEFINE VARIABLES
cities_dict = {}
cities_list = []
urls_list = []

clean_urls1 = []
cleaning1 = []
cleaning2 = []

clean_urls3 = []
cleaning3 = []
cleaning4 = []
cleaning5 = []

responses = []

url = "https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
url_two = "https://www.volby.cz/pls/ps2017nss/"
abroad = "https://www.volby.cz/pls/ps2017nss/ps36?xjazyk=CZ"
brno_city = "https://www.volby.cz/pls/ps2017nss/ps34?xjazyk=CZ&xkraj=11&xobec=582786"

def call_link(link, link_position, step, str1, str2, str3):
    cities_list.clear()
    urls_list.clear()
    cities_dict.clear()
    get_reply = requests.get(link)
    soup = bs4.BeautifulSoup(get_reply.text, "html.parser")
    #find_soup = soup.find("div", {"class": "topline"})
    find_soup = soup.find(str(str1), {"class": str(str2)})
    find_cities = find_soup.find_all(str(str3))
    cities_index = list(range(1, len(find_cities), step))
    for city in cities_index:
        cities_list.append(find_cities[city].text)
    urls_index = list(range(link_position, len(find_cities), step))
    for urls in urls_index:
        urls_list.append(find_cities[urls])
    return (cities_list, urls_list)

call_link (url, 3, 4, "div", "topline", "td")

urls_index2 = range(0,int(len(urls_list)))
for urls_cleaning in urls_index2:
    string = str(urls_list[urls_cleaning])
    left = '><a href="'
    right = '">X</a></td>'
    cleaning1.append(string[string.index(left)+len(left):string.index(right)])
    cleaning2.append(str(cleaning1[urls_cleaning]).replace('amp;','').replace('"',''))
    clean_urls1.append(url_two+cleaning2[urls_cleaning])

cities_dict = dict(zip(cities_list, clean_urls1))
print (cities_list)

cityname = input("Zadej jmeno obce: ")
print(cities_dict[cityname])

def clean_urls (str4):
    urls_index2 = range(0,int(len(urls_list)))
    for urls_cleaning2 in urls_index2:
        split_strings = str(urls_list[urls_cleaning2]).split('">')
        split_strings2 = str(split_strings[0]).split('href="')
        cleaning3.append(url_two+split_strings2[1].replace('amp;',''))
        if str(str4) in cleaning3[urls_cleaning2]:
            cleaning4.append(cleaning3[urls_cleaning2])
        #clean_urls2 = set(cleaning4)
    return(cleaning4)
    #return(clean_urls2)

def resp ():
    urls_index3 = range(0, int(len(clean_urls2)))
    for resp in urls_index3:
        responses.append(requests.get(clean_urls2[resp]).status_code)
    return (responses)


if cityname == "Zahraničí":
    print ("Vyresit zahranici")
    call_link(abroad, 1, 1, "table", "table", "a")
    #print (urls_list)
    clean_urls ("okrsek")
    clean_urls2 = list(set(cleaning4))
    print(clean_urls2)
    resp()
    print(responses)


elif cityname == "Brno-město":
    print ("Vyresit Brno")
    call_link(brno_city, 0, 1, "div", "topline", "a")
    #print (urls_list)
    clean_urls ("ps311?")
    clean_urls2 = list(set(cleaning4))
    print(clean_urls2)
    resp()
    print(responses)


elif cityname in cities_dict:
    print("to pujde")
    call_link(cities_dict[cityname], 0, 1, "div", "topline", "a")
    #print (urls_list)
    #print (clean_urls2)
    clean_urls ("ps311?")
    #print(set(cleaning4))
    clean_urls2 = list(set(cleaning4))
    print(clean_urls2)
    resp()
    print(responses)
    
else:
    print("to nepujde")


print ("-----------------------")


#get_reply = requests.get(url)
#print (get_reply.status_code)


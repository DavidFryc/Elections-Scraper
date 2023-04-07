"""
Main.py: Treti projekt do Engeto Online Python Akademie
author: David Fryc
email: df@emd.dk
discord: David F.#2019
"""

import requests
import bs4
import sys
import os
import download_data
import csv

os.system('cls')

print(sys.argv)

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
responses = []      #FOR TESTING ONLY, NOT USED

url = 'https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ'
url_two = 'https://www.volby.cz/pls/ps2017nss/'
abroad = 'https://www.volby.cz/pls/ps2017nss/ps36?xjazyk=CZ'
brno_city = 'https://www.volby.cz/pls/ps2017nss/ps34?xjazyk=CZ&xkraj=11&xobec=582786'

# 3 ARGUMENTS RULE FULFILLED?
if len(sys.argv) != 3:
    print('''Sorry, three inputs are required.
    1) "Filename".py
    2) Name of selected city
    3) "Name of output file ''')
    quit()

# OUTPUT FILE LOCATION
script_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
csv_file = os.path.join(script_dir,sys.argv[2])

# FUNCTION THAT COLLECTS NAMES OF FINAL CITIES & AND THEIR LINKS FROM CITY-LINKS
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

# CLEANS LINKS FOUND BY "call_link" FUNCTION AND SAVES BOTH AS DICT.
urls_index2 = range(0,int(len(urls_list)))
for urls_cleaning in urls_index2:
    string = str(urls_list[urls_cleaning])
    left = '><a href="'
    right = '">X</a></td>'
    cleaning1.append(string[string.index(left)+len(left):string.index(right)])
    cleaning2.append(str(cleaning1[urls_cleaning]).replace('amp;','').replace('"',''))
    clean_urls1.append(url_two+cleaning2[urls_cleaning])
cities_dict = dict(zip(cities_list, clean_urls1))

#cityname = input("Zadej jmeno obce: ")
cityname = sys.argv[1]

# FUNCTION FOR SUB-LINKS CLEANING
def clean_urls (str4):
    urls_index2 = range(0,int(len(urls_list)))
    for urls_cleaning2 in urls_index2:
        split_strings = str(urls_list[urls_cleaning2]).split('">')
        split_strings2 = str(split_strings[0]).split('href="')
        cleaning3.append(url_two+split_strings2[1].replace('amp;',''))
        if str(str4) in cleaning3[urls_cleaning2]:
            cleaning4.append(cleaning3[urls_cleaning2])
    return(cleaning4)

def resp ():                   # FOR TESTING ONLY, NOT USED
    urls_index3 = range(0, int(len(clean_urls2)))
    for resp in urls_index3:
        responses.append(requests.get(clean_urls2[resp]).status_code)
    return (responses)

# USER-FUNCTION BASED CALL OF CITIES & LINKS (+CLEANING) AND WRITING OF RESULTS
if cityname == "Zahraničí":
    call_link(abroad, 1, 1, "table", "table", "a")
    clean_urls ("okrsek")
    clean_urls2 = list(set(cleaning4))
    clean_urls2_index = range(0, int(len(clean_urls2)))
    berlin_sample = ("https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=999997&xsvetadil=EV&xzeme=276&xokrsek=12")
    header = download_data.get_headers(berlin_sample, "Země", "Okrsek", 7, 137)
    with open (csv_file, mode="w", newline="",encoding="utf-16") as file:
        write_header = csv.writer(file, delimiter=";")
        write_header.writerow(header)
        for data in clean_urls2_index: 
            prepare_data = download_data.get_data(clean_urls2[data], 2, 3, 8, 138)
            write_data = csv.writer(file, delimiter = ";")
            write_data.writerows(prepare_data)

elif cityname == "Brno-město":
    call_link(brno_city, 0, 1, "div", "topline", "a")
    clean_urls ("ps311?")
    clean_urls2 = list(set(cleaning4))
    clean_urls2_index = range(0, int(len(clean_urls2)))
    krpole_sample = ("https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=11&xobec=582786&xmc=551007&xvyber=6202")
    header = download_data.get_headers(krpole_sample, "Okres", "MČ / MO", 10, 140)
    with open (csv_file, mode="w", newline="",encoding="utf-16") as file:
        write_header = csv.writer(file, delimiter=";")
        write_header.writerow(header)
        for data in clean_urls2_index: 
            prepare_data = download_data.get_data(clean_urls2[data], 3, 0, 11, 141)
            write_data = csv.writer(file, delimiter = ";")
            write_data.writerows(prepare_data)

elif cityname in cities_dict:
    call_link(cities_dict[cityname], 0, 1, "div", "topline", "a")
    clean_urls ("ps311?")
    clean_urls2 = list(set(cleaning4))
    clean_urls2_index = range(0, int(len(clean_urls2)))
    stochov_sample = "https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=532860&xvyber=2103"
    header = download_data.get_headers(stochov_sample, "Okres", "Obec", 10, 140)
    with open (csv_file, mode="w", newline="",encoding="utf-16") as file:
        write_header = csv.writer(file, delimiter=";")
        write_header.writerow(header)
        for data in clean_urls2_index: 
            prepare_data = download_data.get_data(clean_urls2[data], 2, 0, 11, 141)
            write_data = csv.writer(file, delimiter = ";")
            write_data.writerows(prepare_data)   
else:
    print('Sorry, entered city was not found in the list: ')
    print('-----------------------------------------------')
    print(cities_list)
    print('-----------------------------------------------')
    quit()
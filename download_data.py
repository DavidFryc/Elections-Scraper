import requests
import bs4


def get_headers (url, okres, obec, start, end):
    simple_header = [str(okres), "Kód obce", str(obec), "Voliči v seznamu", " Vydané obálky", "Volební účast v %", "Platné hlasy"]
    get_reply = requests.get(url)
    soup = bs4.BeautifulSoup(get_reply.content, 'html.parser')
    find_soup = soup.find('div', {'class': 'topline'})
    find_header = find_soup.find_all('td')
    header_index = range(int(start),end,5)
    header_list = []
    for header in header_index:
        header_list.append(find_header[header].text)
    full_header = simple_header + header_list
    return (full_header)

print(get_headers("https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=1&xobec=547344&xvyber=1100", "Okres,", "Obec", 10, 140))

def get_data (url, obec_name, offset_abr, start, end):    
# GET DATA FROM THE TOP TABLE
    get_reply = requests.get(url)
    soup = bs4.BeautifulSoup(get_reply.content, 'html.parser')
    find_soup = soup.find('div', {'class': 'topline'}) 
    okres = str(find_soup.find_all('h3')[1].text).replace("Okres: ","").replace("\n","").replace("Země a území: ", "").replace("Obec: ","")
    obec = str(find_soup.find_all('h3')[int(obec_name)].text).replace("Obec: ","").replace("\n","").replace("MČ/MO: ","").replace("Okrsek: ", "")\
        .replace ("Výsledky hlasování za územní celky – Obec ", "")
    voters = str(find_soup.find_all('td')[3-offset_abr].text).replace(u"\xa0","")
    envelops = str(find_soup.find_all('td')[4-offset_abr].text).replace(u"\xa0","")
    turnout = str(find_soup.find_all('td')[5-offset_abr].text).replace(u"\xa0","")
    votes = str(find_soup.find_all('td')[7-offset_abr].text).replace(u"\xa0","")

# GET CITY CODES
    if "99997" in url:
        code = "Zahraničí"
    elif "&xmc" in url:
        url_split = url.split("&xmc=")
        url_split2 = url_split[1].split("&xvyber")
        code = url_split2[0]
    else:
        url_split = url.split("obec=")
        url_split2 = url_split[1].split("&xvyber")
        code = url_split2[0]

# COMPILE TOP TABLE & CITY CODES
    res_list1 = [okres, code , obec, voters, envelops, turnout, votes]

# DOWNLOAD ELECTION RESULTS    
    find_results1 = find_soup.find_all('td')
    results_index = range(start, end, 5)
    res_list2 = []
    for results1 in results_index:
        res_cleaning = str(find_results1[results1].text).replace(u"\xa0","")
        res_list2.append(res_cleaning)

#COMPILE TOP TABLE & RESULTS LIST    
    res_list = [res_list1 + res_list2]
    return(res_list)

# FOR TESTING, IGNORE    
if __name__ == "__main__":
    clean_urls2 = ["https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=532762&xvyber=2103", 
            "https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=999997&xsvetadil=EV&xzeme=70&xokrsek=4",
            "https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=11&xobec=582786&xmc=550973&xvyber=6202"]

    urls_index = range (0,3)
    #print(get_headers(clean_urls2[0], "Okres", "Obec", 10, 140))
    #print(get_data(clean_urls2[0], 2, 0, 11, 141))
    


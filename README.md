# 3. Projekt v ramci Engeto

# Elections-Scraper

# Spousteni souboru: 
    # Soubor se spousti pomoci sys.argv se tremi parametry:
    # 1 - Jmeno souboru - "main.py"
    # 2 - Nazev volebniho okrsku. Napr. "Kladno"
    # 3 - Jmeno vystupniho souboru (vc. koncovky). Napr. "vystup_kladno.csv"
    # Priklad: "python main.py Kladno vystup_kladno.csv"
    # Pozn.: Prvni sloupec obsahuje vetsinou stejny vystup. Viz Priklad; 100x "Kladno". 
    #        Prvni sloupec dava smysl v podstate jen kdyz je "sys.argv[1] = Zahraničí"

# Hlavni skript je soubor "Main.py"
# Skript "download_data.py" je pomocny s nekolika funkcemi pro stazeni vysledku. 
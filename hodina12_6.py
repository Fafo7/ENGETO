import requests
from bs4 import BeautifulSoup

def nacti_obsah_stranky(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
        else:
            return None
    except requests.RequestException as e:
        print(f"Chyba pri načítavaní stránky: {e}")
        return None

def ziskej_cenu_zlata(rozdeleny_text):
    try:
        cena_element = rozdeleny_text.find('span', class_='price-section__current-value')
        if cena_element:
            return cena_element.get_text().strip()
        else:
            return None
    except Exception as e:
        print(f"Chyba pri extrahovaní ceny: {e}")
        return None

def main():
    url = "https://markets.businessinsider.com/commodities/gold-price"
    obsah = nacti_obsah_stranky(url)
    
    if obsah is None:
        print("Nedostupný HTML objekt")
        return None
    
    cena = ziskej_cenu_zlata(obsah)
    
    if cena is None:
        print("Nedostupná cena")
        return None
    
    print(f"Aktuální cena zlata $: {cena}")
    return cena

# Testovanie funkcie main
if __name__ == "__main__":
    main()
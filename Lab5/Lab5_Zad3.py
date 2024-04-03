import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

def pobierz_strone(url):
    response = requests.get(url)
    return response.text

def scrap_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    naglowki = [naglowek.text.strip() for naglowek in soup.find_all('h2')]
    odnosniki = [odnosnik['href'] for odnosnik in soup.find_all('a', href=True)]
    dane_adresowe = [dane.text.strip() for dane in soup.find_all(class_='adres')]
    return naglowki, odnosniki, dane_adresowe

def main(url):
    html = pobierz_strone(url)
    naglowki, odnosniki, dane_adresowe = scrap_info(html)

    print("Nagłówki:")
    for naglowek in naglowki:
        print(naglowek)

    print("\nOdnośniki:")
    for odnosnik in odnosniki:
        print(odnosnik)

    print("\nDane adresowe:")
    for dane in dane_adresowe:
        print(dane)

if __name__ == "__main__":
    urls = [
        "https://books.toscrape.com/catalogue/the-bulletproof-diet-lose-up-to-a-pound-a-day-reclaim-energy-and-focus-upgrade-your-life_931/index.html",
        "https://books.toscrape.com/catalogue/eat-fat-get-thin_688/index.html",
        "https://books.toscrape.com/catalogue/10-day-green-smoothie-cleanse-lose-up-to-15-pounds-in-10-days_581/index.html"
    ]

    with Pool() as pool:
        pool.map(main, urls)

#Przy uzyciu wielu url każdy z nich będzie pobierany i przetwarzany równolegle w różnych procesach

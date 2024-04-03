import requests
from bs4 import BeautifulSoup

def scrap_info(url):
    # Pobranie zawartości strony
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Pobranie nagłówków
    naglowki = [naglowek.text.strip() for naglowek in soup.find_all('h2')]

    # Pobranie odnośników
    odnosniki = [odnosnik['href'] for odnosnik in soup.find_all('a', href=True)]

    # Pobranie danych adresowych
    dane_adresowe = [dane.text.strip() for dane in soup.find_all(class_='adres')]

    return naglowki, odnosniki, dane_adresowe

if __name__ == "__main__":
    url = "https://books.toscrape.com/catalogue/the-most-perfect-thing-inside-and-outside-a-birds-egg_938/index.html"
    naglowki, odnosniki, dane_adresowe = scrap_info(url)

    print("Nagłówki:")
    for naglowek in naglowki:
        print(naglowek)

    print("\nOdnośniki:")
    for odnosnik in odnosniki:
        print(odnosnik)

    print("\nDane adresowe:")
    for dane in dane_adresowe:
        print(dane)

import requests
from bs4 import BeautifulSoup
import concurrent.futures
import time

def scrap_info(url):
    start_time = time.time()  # Zaczynamy mierzyć czas
    # Pobranie zawartości strony
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Pobranie nagłówków
    naglowki = [naglowek.text.strip() for naglowek in soup.find_all('h2')]

    # Pobranie odnośników
    odnosniki = [odnosnik['href'] for odnosnik in soup.find_all('a', href=True)]

    # Pobranie danych adresowych
    dane_adresowe = [dane.text.strip() for dane in soup.find_all(class_='adres')]

    end_time = time.time()  # Kończymy mierzyć czas
    print("Czas wykonania scrap_info:", end_time - start_time)  # Wyświetlamy czas wykonania

    return naglowki, odnosniki, dane_adresowe

if __name__ == "__main__":
    url = "https://books.toscrape.com/catalogue/the-bulletproof-diet-lose-up-to-a-pound-a-day-reclaim-energy-and-focus-upgrade-your-life_931/index.html"
    start_time = time.time()  # Zaczynamy mierzyć czas

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(scrap_info, url)
        naglowki, odnosniki, dane_adresowe = future.result()

    end_time = time.time()  # Kończymy mierzyć czas
    print("Całkowity czas wykonania:", end_time - start_time)  # Wyświetlamy czas wykonania

    print("Nagłówki:")
    for naglowek in naglowki:
        print(naglowek)

    print("\nOdnośniki:")
    for odnosnik in odnosniki:
        print(odnosnik)

    print("\nDane adresowe:")
    for dane in dane_adresowe:
        print(dane)


#Dzięki wykorzystaniu wielowątkowości, operacje pobierania i przetwarzania danych mogą
# być wykonywane równolegle w różnych wątkach, co przyspiesza cały proces.

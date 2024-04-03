import asyncio
import aiohttp
from bs4 import BeautifulSoup
import time

async def pobierz_strone(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def scrap_info(url):
    start_time = time.time()  # Zaczynamy mierzyć czas
    html = await pobierz_strone(url)
    soup = BeautifulSoup(html, 'html.parser')

    naglowki = [naglowek.text.strip() for naglowek in soup.find_all('h2')]
    odnosniki = [odnosnik['href'] for odnosnik in soup.find_all('a', href=True)]
    dane_adresowe = [dane.text.strip() for dane in soup.find_all(class_='adres')]

    end_time = time.time()  # Kończymy mierzyć czas
    print("Czas wykonania scrap_info:", end_time - start_time)  # Wyświetlamy czas wykonania

    return naglowki, odnosniki, dane_adresowe

async def main():
    start_time = time.time()  # Zaczynamy mierzyć czas
    url = "https://books.toscrape.com/catalogue/the-bulletproof-diet-lose-up-to-a-pound-a-day-reclaim-energy-and-focus-upgrade-your-life_931/index.html"
    naglowki, odnosniki, dane_adresowe = await scrap_info(url)
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

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


# Drugi kod jest bardziej wydajny w kontekście pobierania i parsowania danych z
# wielu źródeł w tym samym czasie, co może przynieść korzyści zwłaszcza w
# przypadku dużych ilości danych

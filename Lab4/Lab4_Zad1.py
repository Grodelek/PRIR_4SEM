import asyncio


async def print_numbers():
    for i in range(1, 6):
        print(i)
        await asyncio.sleep(1)


async def main():
    await asyncio.gather(print_numbers())

if __name__ == "__main__":
    asyncio.run(main())


#Wnioski: Wyswietlone zostaja liczby od 1-5 z sekundowym opoznieniem

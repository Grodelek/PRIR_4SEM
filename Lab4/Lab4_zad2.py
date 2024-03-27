import asyncio

async def count_down():
    for i in range(5, 0, -1):
        print(f"Countdown: {i}")
        await asyncio.sleep(1)

async def count_up():
    for i in range(1, 6):
        print(f"Countup: {i}")
        await asyncio.sleep(0.5)

async def main():
    await asyncio.gather(count_down(), count_up())

if __name__ == "__main__":
    asyncio.run(main())


#funkcja asyncio.gather powoduje jednoczesne wykonanie obu funkcji w tym przypadku
# count down i count up w roznych odstepach czasu 

import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("task 2 finished")

async def main():
    task1_handle = asyncio.create_task(task1())
    task2_handle = asyncio.create_task(task2())

    await task1_handle
    await task2_handle

if __name__ == "__main__":
    asyncio.run(main())

#Wniosek: kod uruchamia dwa zadania rownolegle i czeka na ich zakonczenie

from asyncio import gather, run, sleep as async_sleep
from time import sleep, time


async def serve_coffee():
    print("Preparing coffee...")
    sleep(1)  # Go to coffee machine
    sleep(3)  # Put coffee in machine
    await async_sleep(8)  # Wait for the coffee to be ready
    sleep(1)  # Bring back coffee    print("Coffee ready!")

    async def serve_cake():
        print("Preparing cake...")
        sleep(1)  # Go to cake
        sleep(3)  # Put cake in bag
        sleep(1)  # Bring back cake
        print("Cake ready!")


async def serve_breakfast():
    print("Serving!")
    before = time()
    await gather(serve_coffee(), serve_cake())
    print(f"Finished in {time() - before : .2f}s")


run(serve_breakfast())

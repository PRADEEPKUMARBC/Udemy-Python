import asyncio
import time

async def brew(name):
    print(f"Brewing {name} ....")
    await asyncio.sleep(2)
    print(f"{name} is ready....")

async def main():
    await asyncio.gather(
        brew("Masala Chai....")
        brew("Ginger Chai....")
        brew("Green Chai.....")
    )
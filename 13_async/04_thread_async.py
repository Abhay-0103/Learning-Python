import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(iteam):
    print(f"Checking stock for {iteam}...")
    time.sleep(2)  # Blocking operation
    return f"{iteam} stock: 42"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "Laptop")
        print(result)

asyncio.run(main())
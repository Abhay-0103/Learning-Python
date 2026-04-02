import asyncio

async def brew_pyaar():
    print("Brewing Pyaar...")
    await asyncio.sleep(2)
    print("Pyaar is ready!")

asyncio.run(brew_pyaar())
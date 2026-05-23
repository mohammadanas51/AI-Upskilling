import asyncio

async def ask_gpt():
    await asyncio.sleep(2)
    return "GPT Response"

async def ask_claude():
    await asyncio.sleep(1)
    return "Claude Response"

async def main():
    results = await asyncio.gather(
        ask_gpt(),
        ask_claude()
    )
    print(results)

asyncio.run(main())
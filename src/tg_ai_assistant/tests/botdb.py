import asyncio

from tg_ai_assistant.storage.bot import init, get_data, set_data

if __name__ == "__main__":
    asyncio.run(init())
    asyncio.run(set_data("count", "1011"))
    print(asyncio.run(get_data("count")))

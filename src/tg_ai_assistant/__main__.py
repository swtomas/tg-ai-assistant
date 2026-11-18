import asyncio

from tg_ai_assistant.handlers.interface import router as interface_router
from tg_ai_assistant.utils.config import bot, dp


async def run() -> None:
    try:
        print("Start")
        dp.include_router(interface_router)
        await dp.start_polling(bot)
    finally:
        print("End")


def main() -> None:
    asyncio.run(run())


if __name__ == "__main__":
    main()

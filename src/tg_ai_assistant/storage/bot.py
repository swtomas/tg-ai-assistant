import aiosqlite

BOT_DB_PATH = "bot.db"


async def init() -> None:
    async with aiosqlite.connect(str(BOT_DB_PATH)) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS bot (
                data_name TEXT PRIMARY KEY,
                data_count TEXT
            )
            """
        )
        await db.commit()


async def set_data(data_name: str, data_count: str) -> None:
    async with aiosqlite.connect(str(BOT_DB_PATH)) as db:
        await db.execute(
            """
            INSERT OR REPLACE INTO bot (data_name, data_count) VALUES (?, ?)
            """, (data_name, data_count)
        )
        await db.commit()

async def get_data(data_name: str) -> str:
    async with aiosqlite.connect(str(BOT_DB_PATH)) as db:
        async with db.execute(
            """
            SELECT data_count FROM bot WHERE data_name = ?""", (data_name,)
        ) as cursor:
            row = await cursor.fetchone()
            return row[0]
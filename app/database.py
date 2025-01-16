import asyncpg

DATABASE_URL = "postgresql://postgres:dani0919@localhost:5432/ReservationDeleteDb"

async def get_db_connection():
    return await asyncpg.connect(DATABASE_URL)

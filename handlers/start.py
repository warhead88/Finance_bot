from aiogram import Router, types
from aiogram.filters import Command

from sqlalchemy import select

from db.db import get_async_session
from db.tables import User

router = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    async with get_async_session() as session:
        result = await session.execute(
            select(User).filter_by(id = message.from_user.id)
        )
        user = result.scalar_one_or_none()

        if not user:
            user = User(id=message.from_user.id)
            session.add(user)
            await message.answer("Привет! Это бот финансовый менеджер. Он поможет тебе справиться с финансами.")
        else:
            await message.answer("Для получения инструкций введи команду /help.")

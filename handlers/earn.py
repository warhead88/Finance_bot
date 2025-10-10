from aiogram import Router, types
from aiogram.filters import Command

from sqlalchemy import select

from db.db import get_async_session
from db.tables import User, Operation

router = Router()

@router.message(Command("earn"))
async def add(message: types.message):
    try:
        amount = int(message.text.split()[1])
        if amount <= 0:
            raise
    except:
        await message.answer("Введёно неверное количество денег.")
        return

    async with get_async_session() as session:
        user_id = message.from_user.id

        result = await session.execute(
            select(User).filter_by(id = user_id)
        )
        user = result.scalar_one_or_none()

        user.earned = user.earned + amount

        operation = Operation(user_id = user_id, amount = count, type = "add")
        session.add(operation)

        await message.answer(f"Вы успешно зачислили {amount} рублей на счёт.")

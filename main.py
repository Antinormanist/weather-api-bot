import asyncio

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from decouple import config

TOKEN = config("TOKEN")

# All handlers should be attached to the Router (or Dispatcher)

disp = Dispatcher()


@disp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    '/start' command
    """
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}! Write your city below and I'll send you weather info!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await disp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
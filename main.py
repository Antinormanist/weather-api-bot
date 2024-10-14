import asyncio

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from decouple import config
import requests

TOKEN = config("TOKEN")
API_TOKEN = config('API_TOKEN')
# All handlers should be attached to the Router (or Dispatcher)

disp = Dispatcher()


@disp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    '/start' command
    """
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}! Write your city below and I'll send you weather info!")


@disp.message()
async def echo_handler(message: Message) -> None:
    data = requests.get('https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'.format(city_name=message.text, API_key=API_TOKEN)).json()
    try:
        await message.answer(f'{data['weather'][0]['main']}. {data['weather'][0]['description']}. speed {data['wind']['speed']} m/s')
    except:
        await message.answer('Что-то пошло не так. Вводите название города на английском.')


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await disp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
import asyncio
import telegram
from auth import telegram_token
from data import weather_data
hourly_data = weather_data['hourly'][:12]


async def main():
    will_rain = False
    bot = telegram.Bot(telegram_token)
    for hour in hourly_data:
        if hour['weather'][0]['id'] < 700:
            will_rain = True
    async with bot:
        if will_rain:
            await bot.send_message(text='bring an umbrella!', chat_id=307799724)
        else:
            await bot.send_message(text='no rain for the next 12 hours', chat_id=307799724)





if __name__ == '__main__':
    asyncio.run(main())

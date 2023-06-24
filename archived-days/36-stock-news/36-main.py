import asyncio
import telegram
from auth import telegram_token
from stock_data import get_stock_delta
from news_data import get_news
STOCK = "NVDA"
COMPANY_NAME = "NVIDIA"
NEWS_THRSHD = 0

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


async def main():
    delta = get_stock_delta(STOCK)
    if abs(delta) > NEWS_THRSHD:
        news = get_news(COMPANY_NAME)

    if news['totalResults'] > 0:
        bot = telegram.Bot(telegram_token)
        async with bot:
            await bot.send_message(text=f'NVDA: 🔺{delta:.2f}%', chat_id=307799724)
            await bot.send_message(text=f'{news["articles"][0]["title"]}: {news["articles"][0]["url"]}',
                                   chat_id=307799724)
            await bot.send_message(text=f'{news["articles"][1]["title"]}: {news["articles"][1]["url"]}',
                                   chat_id=307799724)
            await bot.send_message(text=f'{news["articles"][2]["title"]}: {news["articles"][2]["url"]}',
                                   chat_id=307799724)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


if __name__ == '__main__':
    asyncio.run(main())

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


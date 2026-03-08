import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, types

TELEGRAM_TOKEN = "7779251661:AAHV7fLWcEUiybFcnCEWWYSTgneOb18yphM"
XAI_API_KEY = "xai-quqqAzQahq22ood7ReEEmfBPPaZUrqJ6JbKGiJxRG6NoaQxIbmS3kJR17TBwpSCJWvmB2XSSDA3ivABU"

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message()
async def handle(message: types.Message):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://api.x.ai/v1/chat/completions",
                headers={"Authorization": f"Bearer {XAI_API_KEY}"},
                json={
                    "model": "grok-4-1-fast-non-reasoning",
                    "messages": [{"role": "user", "content": message.text}],
                    "max_tokens": 800
                }
            ) as r:
                data = await r.json()
                reply = data["choices"][0]["message"]["content"]
                await message.reply(reply)
    except:
        await message.reply("Try again later.")

asyncio.run(dp.start_polling(bot))

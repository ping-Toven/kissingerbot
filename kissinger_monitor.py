import discord
import os
from dotenv import load_dotenv
from discord import Webhook
import aiohttp


load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
kissbot = discord.Bot(intents=intents)

async def send_webhook(text):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url('https://discord.com/api/webhooks/1066229078987907103/M2ZXnLXf6O6H0mLDvBvpbtiF8oVMdPWMYMYyRVh3GJ4YQtEGhYZ53yc74I-Bz84mnmrB', session=session)
        await webhook.send(text, username='MaltHook')

@kissbot.event
async def on_message(message):
    logchannel = await kissbot.fetch_channel(1066230886254772264)
    content = message.content
    content_folded = content.casefold()
            
    if message.author == kissbot.user:
        return
    
    if message.channel.id == 1066222618853781534:
        print("RAW MESSAGE \n", message)

        try:
            await logchannel.send(content)
            await logchannel.send(message)
            await send_webhook(f"AP News mentioned Kissinger. Tweet:\n{content}")
        except Exception as e:
            await logchannel.send(str(e))
            pass
    elif "hi bot" in content_folded or "hey bot" in content_folded or "hello bot" in content_folded:
        greeter = str(message.author)
        greeter = greeter[:-5]
        await message.channel.send(f'Hey {greeter}!')
        
# Write to terminal on login
@kissbot.event
async def on_ready():
    print(f'Logged on as {kissbot.user}!')

# Write to terminal on disconnect
@kissbot.event
async def on_disconnect():
    print(f'Disconnected as {kissbot.user}')
    
# run bot token
def main():
    kissbot.run(os.getenv('TOKEN'))
    
if __name__ == '__main__':
    main()
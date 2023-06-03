import discord
# from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

token = 'MTExNDM1NzE1MjExNTU5NzMyMw.GLZurV.aUviYLuR-XsJNe9id3GveiPNLX9V6XG2qgg5zo'
#bot = commands.Bot(command_prefix='#')
 
@client.event # 이벤트 함수
async def on_ready(): # 비동기로 작동함
    print(f'Login bot: {client.user}') #이거 콘솔창에 로그인했다고 뜨는거임
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
 
client.run(token)
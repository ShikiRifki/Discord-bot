import discord
from discord.ext import commands
from kodland_utils import *
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def generate_password(ctx):
    await ctx.send(pass_gen(10))

@bot.command()
async def emoji(ctx):
    await ctx.send(random_emoji())

@bot.command()
async def flip(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def meme(ctx):
    selected = random.choice(os.listdir('images'))
    with open(f'images/{selected}', 'rb') as f:
        pictures = discord.File(f)
    await ctx.send(file=pictures)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

organik =['sayur','makanan basi','roti']
kertas= ['kertas','tisu','paper bag']
plastik=['botol','kantong plastik', 'jam']
logam=['bateri','charger', 'botol cap' ]

@bot.command()
async def tanya_sampah(ctx):
    await ctx.send('apa sampah yang anda ingin periksa?')
    message = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    message = str(message.content)

    if message.lower() in organik:
        await ctx.send('itu mah sampah **ORGANIK**')
        await ctx.send('bagusnya make buat pupuk untuk tumbuhan')
    elif message.lower() in kertas:
        await ctx.send('itu mah sampah **KERTAS**')
        await ctx.send('bagusnya make buat ulang jadi kertas baru')
    elif message.lower() in plastik:
        await ctx.send('itu mah sampah **PLASTIK**')
        await ctx.send('bagusnya make di recycle jadi barang baru aja')
    elif message.lower() in logam:
        await ctx.send('itu mah sampah **LOGAM**')
        await ctx.send('bagusnya di daur ulang supay bisa dipake lagi')
    else:
        await ctx.send('bung itu bukan sampah!')

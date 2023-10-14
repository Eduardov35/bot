import requests
import os,random
import random
import discord
from discord.ext import commands
from bot_logic import gen_pass
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
img_alm = ['mem1.jpg', 'mem2.jpg', "mem3.jpg", "men4,jpg"]
img_alma = ["memp1.jpg", "memp2.jpg", "memp3.jpg"]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def copia(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def suma(ctx, arg1, arg2):
    await ctx.send(int(arg1) + int(arg2))
    
@bot.command()
async def multiplicar(ctx, arg1, arg2):
    await ctx.send(int(arg1) * int(arg2))

@bot.command()
async def resta(ctx, arg1, arg2):
    await ctx.send(int(arg1) - int(arg2))  
    
@bot.command()
async def dividir(ctx, arg1, arg2):
    await ctx.send(int(arg1) // int(arg2))
    
@bot.command()
async def numazar(ctx, arg1, arg2):
    await ctx.send(random.randint(int(arg1), int(arg2)))

@bot.command()
async def ayuda(ctx):
    await ctx.send(f"$hello : Sirve para que el bot te salude"
                   "$heh : Sirve para poner la catidad de heh que quieres poner pones $heh y la cantidad"
                   "$suma : Pones un número y otro y lo suma"
                   "$multiplicar : Pones un número y otro y lo multiplica"
                   "$resta : Pones un número y otro y lo resta"
                   "$dividir : Pones un número y otro y lo divide"
                    "$mem1")

@bot.command()
async def mem(ctx):
    with open('imagen/mem1.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
@bot.command()
async def memrandom(ctx):
    img_random = random.choice(img_alm)
    with open(f'imagen/{img_random}', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
@bot.command()
async def animales(ctx):
    img_randoma = random.choice(img_alma)
    with open(f'imagen/{img_randoma}', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
bot.run("TOKEN")

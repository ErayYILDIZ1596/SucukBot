import discord
import random
import time
import EggBotSifre

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

numbers = [20, 21,22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78,79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97,98, 99, 100
]

operators = ['/', '*', '+', '-']

a = random.choice(numbers)

b = random.choice(numbers)

c = random.choice(numbers)

d = random.choice(operators)
operators.remove(d)

e = random.choice(operators)
operators.remove(e)

cevap = 0

score = 0

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık.')

@bot.command()
async def BotSucuk(ctx):
    await ctx.send('Sucuk is real!')

@bot.command()
async def BotSucukAbout(ctx):
    await ctx.send('"Sucuk is real!" der.')

@bot.command()
async def Sucuk(ctx, sayi = 0):
    await ctx.send('Sucuk\n'*sayi)

@bot.command()
async def SucukAbout(ctx):
    await ctx.send('$Sucuk {sayi}, sayi kadar alt alta "Sucuk" der.')

for i in range(1): 
    @bot.command()
    async def matematik(ctx, sayi = 0):
        if sayi > 2:
            await ctx.send('En fazla 2 işlem yapabilirsiniz!')
            pass
        await ctx.send('Matematik oyununa hoş geldiniz.')
        time.sleep(1)
        await ctx.send('Bu oyunda aşağıda bir matematik işlemi verilecek ve siz de bu işlemi çözmeye çalışacaksınız!')
        time.sleep(2)
        await ctx.send('İsterseniz oyunu zorlaştırmak için 1 işlemli değil 2 işlemli sorular haline getirebilirsiniz!')
        time.sleep(3)
        await ctx.send('İşte Sorunuz:')
        time.sleep(1)
        start_time = time.time()
        await ctx.send(f'{a}{d}{b}')
        if d == '/':
            cevap += a//b
        elif d == '*':
            cevap += a*b
        elif d == '+':
            cevap += a+b
        elif d == '-':
            #!Cevap (cevap)
            cevap += a-b
        async def Cevap(ctx, sayi = 0):
            if sayi == cevap:
                await ctx.send('Doğru cevap!')
            else:
                await ctx.send('Cevabınız yanlış!')
                time.sleep(1)
                await ctx.sleep(f'Doğru cevap : {cevap}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

@bot.command()
async def matematikyine(ctx, sayi = 0):
    await ctx.send("İşlem 2 sayılı mı olacak, 3'mü?:")
    tahmin_mesaji = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
    sayi = tahmin_mesaji.content
    if sayi != int:
        await ctx.send('Lütfen bir sayı giriniz(2-3)')
        time.sleep(1)
    if sayi == 2:
        await ctx.send('İşte Sorunuz:')
        time.sleep(1)
        await ctx.send(f'{a}{d}{b}')
        if d == '/':
            cevap += a//b
        elif d == '*':
            cevap += a*b
        elif d == '+':
            cevap += a+b
        elif d == '-':
            cevap += a-b
        
        if ctx.author.send() == cevap:
            await ctx.send('Doğru cevap!')
            global score
            score += 1

        else:
            await ctx.send('Cevabınız yanlış!')
            time.sleep(1)
            await ctx.sleep(f'Doğru cevap : {cevap}')

    elif sayi == 3:
        await ctx.send('İşte Sorunuz:')
        time.sleep(1)
        await ctx.send(f'{a}{d}{b}{e}{c}')

        if d == '/' and e == '*':
            cevap += a//b*c

        elif d == '/' and e == '+':
            cevap += a//b+c

        elif d == '/' and e == '-':
            cevap += a//b-c

        elif d == '*' and e == '/':
            cevap += a*b//c

        elif d == '*' and e == '+':
            cevap += a*b+c

        elif d == '*' and e == '-':
            cevap += a*b-c

        elif d == '+' and e == '/':
            cevap += a+b//c

        elif d == '+' and e == '*':
            cevap += a+b*c

        elif d == '+' and e == '-':
            cevap += a+b-c

        elif d == '-' and e == '/':
            cevap += a-b//c

        elif d == '-' and e == '*':
            cevap += a-b*c

        elif d == '-' and e == '+':
            cevap += a-b+c

        if ctx.author.send() == cevap:
            await ctx.send('Doğru cevap!')
            score += 1
            print(score)
            
        elif ctx.author.send() != cevap:
            await ctx.send('Cevabınız yanlış!')
            time.sleep(1)
            await ctx.sleep(f'Doğru cevap : {cevap}')
        
    elif sayi != 2 or 3:
        await ctx.send('Girmeniz gereken komut = Sayı:(sayı). Sayı sadece 2 veya 3 olabilir!')

@bot.command()
async def MatematikAbout(ctx):
    await ctx.send('Matematik oyunu açar(Yakında gelecek...)')

@bot.command()
async def SucukSifre(ctx, sayi = 0):
    await ctx.send(EggBotSifre.EggBot(sayi))

@bot.command()
async def SucukSifreAbout(ctx):
    await ctx.send('$SucukSifre{sayi}, sayi kadar uzun bir parola verir.')

@bot.command()
async def commands(ctx):
    await ctx.send('!SucukSifre\n!Sucuk\n!matematik\n!BotSucuk\n!matematikyine\n\nBotlarla ilgili açıklama istiyorsanız; botların komudunu yazıp yanına "About" eklemeniz yeterli')


bot.run('BotTokeni')

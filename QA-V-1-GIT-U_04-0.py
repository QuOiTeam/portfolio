# "Qorporate Assistant" [Version 01.GIT.U.4.0]
# (c) Корпорация QuOiTeam (QuOiTeam corporation)

# import основных библиотек

import disnake
from disnake.ext import commands
from disnake.utils import get

# import дополнительных библиотек

import random
import time
from time import sleep
import os
import sys
import asyncio
import json

# import токена бота

token = open("git-token.txt", 'r').readline()

# Обозначение бота

bot = commands.Bot(
    command_prefix="/",
    intents=disnake.Intents.all(),
    activity=disnake.Game("qa (v 1.4)", status=disnake.Status.online)
)

# Убираем команду /help

bot.remove_command("help")

# Начало работы

@bot.event
async def on_ready():
    # Основная функция on_ready
    
    print("┌[ YOUR QORPORATION IS ACTIVATED ]")
    print(f"├[Bot name: ➤ {bot.user.name}]")
    print(f"├[Bot version:          ➤ 01.GIT.U.4.0]")
    print(f"├[Bot developer:           ➤ QuOi]")
    print(f"└[Bot ID:   ➤ {bot.user.id}]")

    # Проверяем существование файла и его содержимое
    
    if not os.path.exists("user.json") or os.stat("user.json").st_size == 0:
        with open("user.json", 'w') as file:
            file.write("{}")

    # Загружаем данные из файла JSON
    
    with open("user.json", 'r') as file:
        file_data = file.read()

    # Проверяем, что файл содержит данные, прежде чем их загружать
    
    if file_data.strip():
        data = json.loads(file_data)
    else:
        data = {}

    for guild in bot.guilds:
        for member in guild.members:
            
            # Проверяем наличие ключа для участника
            
            if str(member.id) not in data:
                data[str(member.id)] = {
                    "WARNS": 0,
                    "CAPS": 0
                }

    # Сохраняем обновленные данные в файл
    
    with open("user.json", 'w') as file:
        json.dump(data, file, indent=4)


    # Сохраняем обновленные данные в файл
    
    with open("user.json", 'w') as file:
        json.dump(data, file, indent=4)



# Дополнительно

if not os.path.exists("user.json"):
    with open("user.json", 'w') as file:
        file.write("{}")

# Автомод (AutoMod)

@bot.event
async def on_message(message):
    
    BADWORDS = ["ban words"]
    LINKS = ["https", "https", "www.", "://", ".org", ".ru", ".su", ".net", ".com", ".shop"]
    WARN = BADWORDS + LINKS
    
    for i in range(0, len(WARN)):
        if WARN[i] in message.content.lower():
            with open('user.json', 'r') as file:
                data = json.load(file)
                file.close()
                
            data[str(message.author.id)]["WARNS"] += 1
                
            with open('user.json', 'w') as file:
                data[str(message.author.id)]["WARNS"] += 1
                json.dump(data, file, indent=4)
                
                file.close()
                
            emb = disnake.Embed(
                title="Нарушение!",
                description=f"Ранее было уже {data[str(message.author.id)]['WARNS'] - 1} нарушений.",
                timestamp=message.created_at
            )

            emb.add_field(name="Канал: ", value=message.channel.mention, inline=True)
            emb.add_field(name="Нарушитель: ", value=message.author.mention, inline=True)
            emb.add_field(name="Тип нарушения: ", value="Ругательства/ссылки", inline=True)

            await get(message.guild.text_channels, id= id).send(embed=emb) # id -> ID вашего канала администрации

            if data[str(message.author.id)]["WARNS"] >= 7:
                await message.author.ban(reason="Вы превысили максимально допустимое значение предупреждений")
             
        
    for word in WARN:
        if word in message.content.lower():
            with open("user.json", 'r') as file: 
                data = json.load(file)

            with open("user.json", 'w') as file:
                data[str(message.author.id)]["WARNS"] += 1
                json.dump(data, file, indent=4)

            emb = disnake.Embed(
                title="Нарушение!",
                description=f"Ранее было уже {data[str(message.author.id)]["WARNS"] - 1} нарушений.",
                timestamp=message.created_at
            )

            emb.add_field(name="Канал: ", value=message.channel.mention, inline=True)
            emb.add_field(name="Нарушитель: ", value=message.author.mention, inline=True)
            emb.add_field(name="Тип нарушения: ", value="Ругательства/ссылки", inline=True)

            await get(message.guild.text_channels, id= id).send(embed=emb)  # id -> ID канала администрации

            if data[str(message.author.id)]["WARNS"] >= 7:
                await message.author.ban(reason="Вы превысили максимально допустимое значение предупреждений")

    if message.content.isupper():
        with open("user.json", 'r') as file:
            data = json.load(file)

        with open("user.json", 'w') as file:
            data[str(message.author.id)]["WARNS"] += 1
            json.dump(data, file, indent=4)

            data[str(message.author.id)]["CAPS"] += 1

            if data[str(message.author.id)]["CAPS"] >= 3:
                data[str(message.author.id)]["CAPS"] = 0
                data[str(message.author.id)]["WARNS"] += 1

                with open("user.json", 'w') as file:
                    data[str(message.author.id)]["WARNS"] += 1
                    json.dump(data, file, indent=4)

            emb = disnake.Embed(
                title="Нарушение!",
                description=f"Ранее было уже {data[str(message.author.id)]['WARNS'] - 1} нарушений.",
                timestamp=message.created_at
            )

            emb.add_field(name="Канал: ", value=message.channel.mention, inline=True)
            emb.add_field(name="Нарушитель: ", value=message.author.mention, inline=True)
            emb.add_field(name="Тип нарушения: ", value="Капс", inline=True)

            await get(message.guild.text_channels, id= id).send(embed=emb)  # -> ID канала администрации

            if data[str(message.author.id)]["WARNS"] >= 7:
                await message.author.ban(reason="Вы превысили максимально допустимое значение предупреждений")

# Основные команды

@commands.command(description="Очистка сообщений", pass_context = True)
@commands.has_permissions(administrator=True)
async def clear(self, ctx, amount=1):
    messages = await ctx.channel.purge(limit=amount + 1)

@commands.command(description="Случайное число от 0 до 100", pass_context = True)
async def random(self, ctx):
    await ctx.reply(random.randint(0, 100))

# Slash-команды
@bot.slash_command(name="help", description="Выводит список команд")
async def help(inter):
    message = '''Реестр команд:
    help - Выводит список команд
    server - Выводит информацию о сервере
    random - Случайное число от 0 до 100
    clear [количество сообщений] (только для администрации) - удаляет сообщения '''
    await inter.response.send_message(message)

@bot.slash_command(name="server", description="Выводит информацию о сервере")
async def server(inter):
    await inter.response.send_message(
        f'''Название сервера: {inter.guild.name}
        Участников на сервере: {inter.guild.member_count}'''
    )

# Запуск

bot.run(git-token)

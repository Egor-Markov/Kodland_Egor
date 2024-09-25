import discord 
import random

token = ""

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

# Создаём фунцию генерирования пароля
pass_length = int(input("Enter the length of the password: "))
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)    
    return password

# Функция по подбросу монеты
def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "ОРЁЛ"
    else:
        return "РЕШКА"

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send(random.choice(["\U0001f642", "Bye!"]))
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(pass_length))
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    else:
        await message.channel.send(message.content)

client.run(token)
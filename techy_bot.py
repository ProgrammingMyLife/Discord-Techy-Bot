
import discord
import os
import datetime

client = discord.Client()


dt = datetime.datetime.now()
hour = dt.hour


@client.event
async def on_ready():
     print(f'Bot is online')


part_of_day(hour)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/hello'):
        await message.channel.send('Hello! ' + message.author.mention + '.' + 'Have a nice day ahead!')

    if message.content.startswith('/help'):
        await message.channel.send('''
1.'/hello' -> For telling "hi" to the bot
2.'/help' -> To know the commands
3.'/play' -> Function to be added
4.'/gm'-> To say Good Morning.
5.'/gn' -> To say Good night
6.'/ga '-> To say Good Afternoon

Sorry for inconvenience! More functions will be added soon

     ''' + message.author.mention)




    if message.content.startswith('/gm'):
        if hour < 12:
            await message.channel.send('Good Morning' + message.author.mention + '.' + 'Have nice day ahead')
        else:
            await message.channel.send("Ah.. It's not morning. " + message.author.mention + "I am not a fool (just informing you..) I don't wanna be rude tho")

    if message.content.startswith('/ga'):
        if hour > 12 and hour < 5:
            await message.channel.send('Good Afternoon' + message.author.mention + '.' + 'Have lunch!')
        else:
            await message.channel.send("Ah.. It's not noon. " + message.author.mention + "I am not a fool (just informing you..)")

    if message.content.startswith('/gn'):
        if hour > 19 and hour < 5:
            await message.channel.send('Good Night' + message.author.mention + '.' + 'Sweet Dreams..')
        else:
            await message.channel.send("Ah.. It's not night." + message.author.mention + "I am not a fool (just informing you..)")
    if message.content.startswith('/play'):
        await message.channel.send('Function yet to be added...')

#run
client.run(os.environ['Token'])

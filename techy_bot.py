import discord



client = discord.Client()

@client.event
async def on_ready():
     print(f'Bot is online')

def part_of_day(hour):
    return (
        "morning" if 5 <= hour <= 11
        else
        "afternoon" if 12 <= hour <= 17
        else
        "evening" if 18 <= hour <= 22
        else
        "night"
    )


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
4.'/Good Morning' or '/gm' or '/morning' -> To say Good Morning.
5.'/gn' or '/Good Afternoon' or '/noon'  -> To say Good night
6.'/ga ' or '/Good Night' or 'Night time'-> To say Good Afternoon

More commands to be added..
     ''' + message.author.mention)


# all gm's
    if message.content.startswith('/gm'):
        if part_of_day == 'morning':
            await message.channel.send('Good Morning' + message.author.mention + '.' + 'Have nice day ahead')
        else:
            await message.channel.send("Ah.. It's not morning. " + message.author.mention + "I am not a fool (just informing you..) I don't wanna be rude tho")

    if message.content.startswith('/morning'):
        if part_of_day == 'morning':
            await message.channel.send('Good Morning' + message.author.mention + '.' + 'Have nice day ahead')
        else:
            await message.channel.send("Ah.. It's not morning. " + message.author.mention + "I am not a fool (just informing you..)")

    if message.content.startswith('/Good Morning'):
        if part_of_day == 'morning':
            await message.channel.send('Good Morning' + message.author.mention + '.' + 'Have nice day ahead')
        else:
            await message.channel.send("Ah.. It's not morning. " + message.author.mention + "I am not a fool (just informing you..)")


# all ga's
    if message.content.startswith('/ga'):
        if part_of_day == 'afternoon':
            await message.channel.send('Good Afternoon' + message.author.mention + '.' + 'Have lunch!')
        else:
            await message.channel.send("Ah.. It's not noon. " + message.author.mention + "I am not a fool (just informing you..)")


    if message.content.startswith('/Good Afternoon'):
        if part_of_day == 'afternoon':
            await message.channel.send('Good Afternoon' + message.author.mention + '.' + 'Have lunch!')
        else:
            await message.channel.send("Ah.. It's not noon. " + message.author.mention + "I am not a fool (just informing you..)")

    if message.content.startswith('/noon'):
        if part_of_day == 'afternoon':
            await message.channel.send('Good Afternoon' + message.author.mention + '.' + 'Have lunch!')
        else:
            await message.channel.send("Ah.. It's not noon. " + message.author.mention + "I am not a fool (just informing you..)")

    # all gns

    if message.content.startswith('/gn'):
        if part_of_day == 'night':
            await message.channel.send('Good Night' + message.author.mention + '.' + 'Sweet Dreams..')
        else:
            await message.channel.send("Ah.. It's not night." + message.author.mention + "I am not a fool (just informing you..)")
    if message.content.startswith('Good Night'):
         if part_of_day == 'night':
             await message.channel.send('Good Morning' + message.author.mention + '.' + 'Sweet Dreams..')
    else:
         await message.channel.send("Ah.. It's not night." + message.author.mention + "I am not a fool (just informing you..)")

    if message.content.startswith('/Night time'):
        if part_of_day == 'night':
            await message.channel.send('Good Night' + message.author.mention + '.' + 'Sweet Dreams..')
    else:
        await message.channel.send("Ah.. It's not night." + message.author.mention + "I am not a fool (just informing you..)")



#run
client.run(os.environ['Token'])

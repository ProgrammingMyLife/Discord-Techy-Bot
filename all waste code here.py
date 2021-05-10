''    if message.content.startswith('/morning'):
        if part_of_day == 'morning':
            await message.channel.send('Good Morning' + message.author.mention + '.' + 'Have nice day ahead')
        else:
            await message.channel.send("Ah.. It's not morning. " + message.author.mention + "I am not a fool (just informing you..)")

    if message.content.startswith('/Good Morning'):
        if part_of_day == 'morning':
            await message.channel.send('Good Morning' + message.author.mention + '.' + 'Have nice day ahead')
        else:
            await message.channel.send("Ah.. It's not morning. " + message.author.mention + "I am not a fool (just informing you..)")''


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

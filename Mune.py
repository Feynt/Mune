# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
#! ~/py3.6/bin/python

import random
import re
from discord.ext.commands import Bot

BOT_PREFIX = ("!")
TOKEN = 'Mzc3NTA2OTUyOTc4MzY2NDY0.DdDlPw.anSkvdEBwBiMwoG8GWuJ3u4Vnao'

client = Bot(command_prefix=BOT_PREFIX)

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def rollDie(dieCmd):
    m = re.match(r"(\d+)d(\d+)(.+)?",dieCmd)
    if m is not None:
        diceResults = []
        print('len(groups()): {}'.format(len(m.groups()), m))
        for x in range(int(m[1])):
            diceResults.append(random.randint(1,int(m[2])))
        if len(m.groups()) > 3:
            if re.match(r"(\d+)d(\d+)(.+)?", m[3]) is not None:
                print("Found die roll? {}".format(m[3]))
                diceResults.append(rollDie(m[3]))
            else:
                print("Doesn't match die roll, trying math with {}".format(m[3]))
                nums = re.split(r"(\d+)", m[3])
                for num in nums:
                    print('num:'+num)
                    diceResults.append(int(num))
        total = 0
        for die in diceResults:
            total += die
        diceResults.insert(0,total)
        return diceResults

@client.command(name='r',
        description="Roll some dice using /r #d#(+/-#) formatting.  Ex:  /r 1d20+1, or /r 1d8+1d4+2.",
        brief="Roll some dice",
        pass_context=True)
async def roll_dice(context):
    cmdLine = context.message.content[2:]
    cmds = re.findall(r"[\w\d]+", cmdLine)
    parsedCmds = []
    for cmd in cmds:
        print('cmd: {}'.format(cmd))
        parsedCmds.append(str(rollDie(cmd)))

    output = 'Got message: {} - Total groups: {} - {}'.format(context.message.content, len(cmds), parsedCmds)
    print(output)
    await client.say(context.message.author.mention + ' - ' + output)


@client.command()
async def square():
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))

client.run(TOKEN)

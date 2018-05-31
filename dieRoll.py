
import random
import re
from discord.ext.commands import Bot

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    except TypeError:
        return False

def rollDie(dieCmd):
    print('Received string: {}'.format(dieCmd))
    if isInt(dieCmd):
        return [int(dieCmd)]
    m = re.match(r"(\d+)d(\d+)(.+)?",re.sub(r'^[\+\s]*','',dieCmd))
    if m is not None:
        diceResults = []
        ##print('len(groups()): {}'.format(len(m.groups())))
        #for u in m.groups():
            #print('m:{}'.format(u))
        for x in range(int(m.group(1))):
            ##print('Rolling 1d{}'.format(m.group(2)))
            diceResults.append(random.randint(1,int(m.group(2))))
        if len(m.groups()) > 2:
            #print('Recursive rollDie({})'.format(m.group(3)))
            if m.group(3) is not None:
                newResults = rollDie(m.group(3))
                for num in newResults:
                    diceResults.append(num)
        return diceResults
    else:
        m = re.match(r"(\d+)(.+)?", re.sub(r'^[\+\s]*','',dieCmd))
        if m is not None:
            diceResults = []
            diceResults.append(int(m.group(1)))
            #print('num groups: {}'.format(m.groups()))
            if len(m.groups()) > 1:
                #print('groups > 1, rolling on with {}'.format(m.group(2)))
                if m.group(2) is not None:
                    newResults = rollDie(m.group(2))
                    for num in newResults:
                        diceResults.append(int(num))
            return diceResults

dieRoll = "3d6+1d4+9+3d8"
total = 0;
dieResults = rollDie(dieRoll)
for die in dieResults:
    #print('die:{}'.format(die))
    total += die

print("Rolled {}, got {} ({})".format(dieRoll, total, dieResults))

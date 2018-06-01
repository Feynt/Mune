import random
import re

def rollDie(dieCmd):
    dieStr = re.sub('\s', '', dieCmd)
    #print('Received string: [{}]'.format(dieStr.lstrip('\+')))
    m = re.match(r"(\d+)d(\d+)(.+)?",dieStr.lstrip('\+'))
    if m is not None:
        diceResults = []
        #print('len(groups()): {}'.format(len(m.groups())))
        #for u in m.groups():
            #print('m:{}'.format(u))
        for x in range(int(m.group(1))):
            ##print('Rolling 1d{}'.format(m.group(2)))
            diceResults.append(random.randint(1,int(m.group(2))))
        if len(m.groups()) > 2:
            #print('Recursive rollDie({})'.format(m.group(3)))
            if m.group(3) is not None:
                newResults = rollDie(m.group(3))
                #print('m.group[3]({}) - newResults[{}]'.format(m.group(3),newResults))
                for num in newResults:
                    diceResults.append(num)
        return diceResults
    else:
        m = re.match(r"([\-\d]+)(.+)?", dieStr.lstrip('\s\+'))
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

def totalRoll(dieCmd):
    total = 0
    dieResults = rollDie(dieCmd)
    for die in dieResults:
        #print('die:{}'.format(die))
        total += die
    #print("Rolled {}, got {} ({})".format(dieCmd, total, dieResults))
    dieResults.append(total)
    return dieResults

#roll("3d6 + 1d4 - 9 +3d8")
#roll("8d6+6")
#roll("1d3+1d4+1d5-6")

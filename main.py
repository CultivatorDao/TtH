from char import *
from skill import *
from random import *
from color import Color
from cultivation import *
from ingredients import *
from mobs import *
from map import *
from researching import *
#import io
#import json
#state = {}
#state["health"] = 12

#io.file  json.dumps(state)
#state = json.loads(file_contents)


def intr():
    print('right[r]   left[l]   stat[s]   inv[i]')


print('--------------------------------------------------------------------------')
print('Version: 0.2.5')
print('--------------------------------------------------------------------------')
curLoc = loc1
save = 0
mobsLoc1 = [mobSlime, mobRat, mobGoblin, mobEmu, mobLizard]


def clock(time):
    global minute, hour, day, week, month, year
    y = time[0]
    m = time[1]
    w = time[2]
    d = time[3]
    h = time[4]
    minut = time[5]
    if minut >= 60:
        while minut >= 60 - 1:
            minut -= 60
            h += 1
    if h >= 24:
        while h >= 24:
            h -= 24
            d += 1
    if d >= 7:
        while d >= 7:
            d -= 7
            w += 1
    if w >= 4:
        while w >= 4:
            w -= 4
            m += 1
    if m >= 12:
        while m >= 12:
            m -= 12
            y += 1
    minute = minut
    hour = h
    day = d
    week = w
    month = m
    year = y


damage = kiPower // 100 * 5
mov = str(input())


while year < maxYear:
    dot = location(wMap, point, blank)
    geoloc(stance, blank, wMap)

    if mov == 'r':
        if loc4 == [0, 0, 1, 0, 2, 0, 0, 0, 0]:
            print('You see town')
            print('Enter?')
            print('Yes[1]   No[2]')
            mov = str(input())
            if mov == '1':
                while mov != 'y':
                    print('You see inn[1]')
                    print('You see shop[2]')
                    print('You see gym[3]')
                    print('Exit[e]')
                    mov = str(input())
                    if mov == '1':
                        gold -= (fullhp - hp) // 10
                        hp = fullhp
                        hour += (fullhp - hp) // 10
                        print('You rested')
                        mov = str(input())
                    elif mov == '2':
                        print('Choose action: buy[1]  sell[2]')
                        mov = str(input())
                        if mov == '1':
                            while mov != 'exit':
                                print('Ingregients[1]')
                                print('Materials[2]')
                                print('Skills[3]')
                                mov = input()
                                if mov == '1':
                                    while mov != 'exit':
                                        print('Exit[e]')
                                        print('Your gold: ' + str(gold))
                                        print(stash)
                                        mov = input()
                                        if mov == 'e':
                                            break
                                        mov = int(mov)
                                        ci = stash[mov]
                                        stuffPrice = eff(ci)
                                        tipe = type(ci)
                                        if tipe == 'ки':
                                            stuffPrice *= 2
                                        elif tipe == 'хп':
                                            stuffPrice *= 3
                                        elif tipe == 'фс':
                                            stuffPrice *= 5
                                        elif tipe == 'тт':
                                            stuffPrice *= 2000
                                        elif tipe == 'вс':
                                            stuffPrice *= 5000
                                        print(ci + ' Price:' + str(stuffPrice) + '/1')
                                        print('How much you need?')
                                        quantity = stash[mov + 1]
                                        quan = int(input())
                                        if quan <= quantity:
                                            stuffPrice = stuffPrice * quan
                                        else:
                                            stuffPrice = stuffPrice
                                        print(ci + ' Price for all: ' + str(stuffPrice))
                                        print('Do you want buy?')
                                        print('Yes[1]    No[2]')
                                        mov = input()
                                        if mov == '1':
                                            if gold >= stuffPrice:
                                                gold -= stuffPrice
                                                if inventory.count(ci) == 0:
                                                    inventory.append(ci)
                                                    ind = inventory.index(ci)
                                                    inventory.insert(ind + 1, quan)
                                                else:
                                                    ind = inventory.index(ci)
                                                    junk = inventory.pop(ind + 1)
                                                    junk += quan
                                                    inventory.insert(ind + 1, junk)
                                                print('You bought ' + ci)
                                                print('You spent: ' + str(stuffPrice) + ' gold')
                                                ind = stash.index(ci)
                                                junk = stash.pop(ind + 1)
                                                junk -= quan
                                                if junk == 0:
                                                    stash.pop(ci)
                                                else:
                                                    stash.insert(ind + 1, junk)
                                            else:
                                                print('Not enough gold')
                                        else:
                                            pass
                                elif mov == '3':
                                    print('What do you need?')
                                    print('[1]Wind Blades|Price: 1500 gold')
                                    print('[2]Singularity|Price: 5000 gold')
                                    print('Close[e]')
                                    mov = input()
                                    if mov == '1':
                                        if gold >= 1500:
                                            inventory.append('св: Wind Blades')
                                            inventory.append(1)
                                            gold -= 1500
                                            print('You spent 1500 gold')
                                            print('You bought св: Wind Blades')
                                        else:
                                            print('Not enough gold')
                                    elif mov == '2':
                                        if gold >= 5000:
                                            inventory.append('св: Singularity')
                                            inventory.append(1)
                                            gold -= 5000
                                            print('You spent 5000 gold')
                                            print('You bought св: Singularity')
                                        else:
                                            print('Not enough gold')
                                    elif mov == 'e':
                                        break
                                    else:
                                        pass
                                else:
                                    break
                        elif mov == '2':
                            while mov != 'exit':
                                print('Your gold ' + str(gold))
                                print('What you want to sell?')
                                print(inventory)
                                sellStuff = str(input())
                                if sellStuff == 'e' or sellStuff == '':
                                    break
                                sellStuff = int(sellStuff)
                                if sellStuff > len(inventory):
                                    break
                                ci = inventory[sellStuff]
                                quantity = inventory[sellStuff + 1]
                                ef = eff(ci)
                                tipe = type(ci)
                                if tipe == 'ки':
                                    price = 2
                                elif tipe == 'хп':
                                    price = 3
                                elif tipe == 'фс':
                                    price = 5
                                elif tipe == '%':
                                    price = 10
                                elif tipe == 'ун':
                                    price = 1
                                elif tipe == 'тт':
                                    price = 2000
                                elif tipe == 'вс':
                                    price = 5000
                                stuffPrice = ef * price
                                print(ci + ' Price: ' + str(stuffPrice) + ' gold')
                                mov = input('How much:')
                                if mov == 'e' or mov == '':
                                    break
                                quan = int(mov)
                                if quan > quantity:
                                    break
                                stuffPrice = stuffPrice * quan
                                print(str(quan) + 'x' + ci + ' Price: ' + str(stuffPrice) + ' gold')
                                print('Sell[1]   Close[e]')
                                mov = input()
                                if mov == '1':
                                    print('You sell ' + ci + 'x' + str(quan) + ' for:' + str(stuffPrice) + ' gold')
                                    quantity -= quan
                                    gold += stuffPrice
                                    if quantity == 0:
                                        inventory.pop(sellStuff + 1)
                                        inventory.pop(sellStuff)
                                    else:
                                        junk = inventory.pop(sellStuff + 1)
                                        junk -= quan
                                        inventory.insert(sellStuff + 1, junk)
                                else:
                                    pass
                        else:
                            print('Unknown action')
                    elif mov == '3':
                        while mov != 'exit':
                            print('Training for 1 t/u costs 10 gold')
                            print('Wanna train?')
                            mov = str(input())
                            if mov == 'yes':
                                print('How many t/u?')
                                tTime = int(input())
                                if gold >= tTime * 10:
                                    gold -= tTime * 10
                                    pPower = 0
                                    pPower += randrange(1, physPower // 100) * tTime
                                    physPower += pPower
                                    time += tTime // 2
                                    print('You feel stronger')
                                    print('Phy.Power +' + str(pPower))
                                    barehand = physPower // 25
                                    hand = barehand + handmodifier
                                    kick = barehand * 2
                                    mov = str(input())
                                else:
                                    print('Not enough gold')
                                    mov = str(input())
                            else:
                                print('Unknown action')
                                mov = str(input())
                    elif mov == 'e':
                        print('You see a valley')
                        break
                    else:
                        print('Unknown destination')
                        mov = str(input())
            else:
                mov = str(input())
        if loc1 == [0, 0, 0, 0, 0, 0, 1, 0, 3]:
            print('You see Tower of Challenge')
            print('Do you want climb to tower?')
            mov = str(input())
            if mov == 'yes':
                height = 0
                climbReq = 100
                while mov != 'down':
                    print('Your current height: ' + str(height))
                    mov = str(input())
                    if mov == 'up':
                        if physPower >= climbReq:
                            print('You climbed 100m')
                            print('You used ' + str(climbReq) + ' of your Phys.Power')
                            print('Your Phys.Power ' + str(physPower))
                            height += 100
                            climbReq += 100
                            physPower += physPower // 100
                            print('To climb up need ' + str(climbReq) + ' Phys.Power')
                            time += 1
                            if height == 1000:
                                print('?????:You can climb up to this tower')
                                print('?????:And now what you need?')
                                print('?????:Power or nothing.Ge Ge Ge')
                                print('?????:Oh...My name is Korin, guardian of this tower')
                                print('You see small cat')
                                mov = str(input())
                                if mov == 'power':
                                    print('Korin:Ge Ge Ge.Then lets fight')
                                    boss = bossKorin
                                    bhp = boss[1]
                                    bfhp = boss[3]
                                    batk = boss[2]
                                    bki = boss[11]
                                    bmki = boss[10]
                                    print('You meet ' + boss[0])
                                    print(boss[0] + ' health ' + str(bhp) + '/' + str(bfhp))
                                    print(boss[0] + ' ki ' + str(bki) + '/' + str(bmki))
                                    print('Your health ' + str(hp) + '/' + str(fullhp))
                                    print('Your ki ' + str(ki) + '/' + str(maxki))
                                    mov = str(input())
                                    while mov != 'surr':
                                        if mov == 'fist':
                                            if hp <= 0:
                                                print('You lose')
                                                break
                                            if ki > 0:
                                                if fistLvL == 3 or fistLvL == 4:
                                                    bhp -= (hand + fistModifier) * 2 + (kiPower // 100) * kiLvL
                                                    ki -= kiPower // 100 * kiLvL
                                                else:
                                                    bhp -= hand + fistModifier + (kiPower // 100) * kiLvL
                                                    ki -= kiPower // 100 * kiLvL
                                                kiMastery += kiPower // 100 * kiLvL
                                                if kiMastery >= kiMreq:
                                                    kiMastery -= kiMreq
                                                    kiLvL += 1
                                                    kickModifier += 1
                                                    kMreq += kiMreq // 2
                                                    kiRand = randrange(1, (maxki // 10) // 2)
                                                    maxki += kiRand * (talent // 2)
                                                    print('Your Ki Mastery increased to ' + str(kiLvL))
                                                    print('Your Max Ki increased to ' + str(maxki))
                                            else:
                                                if fistLvL == 3 or fistLvL == 4:
                                                    bhp -= (hand + fistModifier) * 2
                                                else:
                                                    bhp -= hand + fistModifier
                                            print(boss[0] + ' Health ' + str(bhp) + '/' + str(bfhp))
                                            print(boss[0] + ' ki ' + str(bki) + '/' + str(bmki))
                                            hp -= batk
                                            hpModifier += batk
                                            if hpModifier >= hpMreq:
                                                hpModifier -= hpMreq
                                                hpRand = randrange(1, fullhp // 10)
                                                fullhp += hpRand
                                                hpMreq += hpMreq // 2
                                                print('Your health increased to ' + str(fullhp))
                                            print('Your health ' + str(hp) + '/' + str(fullhp))
                                            print('Your ki ' + str(ki) + '/' + str(maxki))
                                            fistMastery += 1
                                            if fistMastery >= fMreq:
                                                fistMastery -= fMreq
                                                fistModifier += 5
                                                fMreq += fMreq // 2
                                                fistLvL += 1
                                                print('Your Fist Mastery improved')
                                                mov = str(input())
                                            mov = str(input())
                                        elif mov == 'kick':
                                            if hp <= 0:
                                                print('You lose')
                                                break
                                            if ki > 0:
                                                if kickLvL == 4 or kickLvL == 5:
                                                    bhp -= (kick + kickModifier) * 2 + (kiPower // 100) * kiLvL
                                                    ki -= kiPower // 100 * kiLvL
                                                else:
                                                    bhp -= kick + kickModifier + (kiPower // 100) * kiLvL
                                                    ki -= kiPower // 100 * kiLvL
                                            kiMastery += kiPower // 100 * kiLvL
                                            if kiMastery >= kiMreq:
                                                kiMastery -= kiMreq
                                                kiLvL += 1
                                                kickModifier += 1
                                                kMreq += kiMreq // 2
                                                kiRand = randrange(1, (maxki // 10) // 2)
                                                maxki += kiRand * (talent // 2)
                                                print('Your Ki Mastery increased to ' + str(kiLvL))
                                                print('Your Max Ki increased to ' + str(maxki))
                                            else:
                                                if kickLvL == 4 or kickLvL == 5:
                                                    bhp -= (kick + kickModifier) * 2
                                                else:
                                                    bhp -= kick + kickModifier
                                            print(boss[0] + ' Health ' + str(bhp) + '/' + str(bfhp))
                                            print(boss[0] + ' ki ' + str(bki) + '/' + str(bmki))
                                            hp -= batk
                                            hpModifier += batk
                                            if hpModifier >= hpMreq:
                                                hpModifier -= hpMreq
                                                hpRand = randrange(1, fullhp // 10)
                                                fullhp += hpRand
                                                hpMreq += hpMreq // 2
                                                print('Your health increased to ' + str(fullhp))
                                            print('Your health ' + str(hp) + '/' + str(fullhp))
                                            print('Your ki ' + str(ki) + '/' + str(maxki))
                                            kickMastery += 1
                                            print(kickMastery)
                                            if kickMastery >= kMreq:
                                                kickMastery -= kMreq
                                                kickModifier += 10
                                                kMreq += kMreq // 2
                                                kickLvL += 1
                                                print('Your Kick Mastery improved')
                                                mov = str(input())
                                            mov = str(input())
                                        elif mov == 'ki':
                                            if ki > 0:
                                                if kiLvL == 5 and kiLvL <= 10:
                                                    kicons = int(input())
                                                    if kicons * 10 <= ki:
                                                        bhp -= ((kicons * (physPower // 100)) * kiModifier) * 2
                                                        ki -= ((kicons * 10) * 2) // kiControl // 10
                                                        print(boss[0] + ' Health ' + str(bhp) + '/' + str(bfhp))
                                                        print(boss[0] + ' ki ' + str(bki) + '/' + str(bmki))
                                                        kiMastery += (kicons * 10) * 2
                                                        if kiMastery >= kMreq:
                                                            kiMastery -= kMreq
                                                            kiLvL += 1
                                                            kickModifier += 1
                                                            kMreq += kiMreq // 2
                                                            kiRand = randrange(1, (maxki // 10) // 2)
                                                            maxki += kiRand * (talent // 2)
                                                            print('Your Ki Mastery increased to ' + str(kiLvL))
                                                            print('Your Max Ki increased to ' + str(maxki))
                                                        hp -= batk
                                                        hpModifier += batk
                                                        if hpModifier >= hpMreq:
                                                            hpModifier -= hpMreq
                                                            hpRand = randrange(1, fullhp // 10)
                                                            fullhp += hpRand
                                                            hpMreq += hpMreq // 2
                                                            print('Your health increased to ' + str(fullhp))
                                                        print('Your health ' + str(hp) + '/' + str(fullhp))
                                                        print('Your ki ' + str(ki) + '/' + str(maxki))

                                                    else:
                                                        print('Not enough ki')
                                                        mov = str(input())
                                                else:
                                                    kicons = maxki // 10
                                                    if kicons * 2 <= ki + 1:
                                                        bhp -= (kicons * (kiPower // 75)) * kiModifier
                                                        ki -= kicons * 2 // kiControl
                                                        print(boss[0] + ' Health ' + str(bhp) + '/' + str(bfhp))
                                                        print(boss[0] + ' ki ' + str(bki) + '/' + str(bmki))
                                                        kiMastery += kicons
                                                        if kiMastery >= kiMreq:
                                                            kiMastery -= kiMreq
                                                            kiLvL += 1
                                                            kickModifier += 1
                                                            kMreq += kiMreq // 2
                                                            kiRand = randrange(1, (maxki // 10) // 2)
                                                            maxki += kiRand * (talent // 2)
                                                            print('Your Ki Mastery increased to ' + str(kiLvL))
                                                            print('Your Max Ki increased to ' + str(maxki))
                                                        hp -= batk
                                                        hpModifier += batk
                                                        if hpModifier >= hpMreq:
                                                            hpModifier -= hpMreq
                                                            hpRand = randrange(1, fullhp // 10)
                                                            fullhp += hpRand
                                                            hpMreq += hpMreq // 2
                                                            print('Your health increased to ' + str(fullhp))
                                                        print('Your health ' + str(hp) + '/' + str(fullhp))
                                                        print('Your ki ' + str(ki) + '/' + str(maxki))
                                                        mov = str(input())
                                                    else:
                                                        print('Not enough ki')
                                                        mov = str(input())
                                            else:
                                                print('Not enough ki')
                                                mov = str(input())
                                        elif mov == 'run':
                                            print('You cant ran from battle')
                                            mov = str(input())
                                        else:
                                            print('Unknown action')
                                            mov = str(input())
                                        if hp <= 0:
                                            print('You lose')
                                            break
                                        elif bhp <= 0:
                                            print('You win')
                                            droprange1 = boss[8]
                                            droprange2 = boss[9]
                                            drop = randrange(droprange1, droprange2)
                                            drop1 = boss[5]
                                            drop2 = boss[6]
                                            drop3 = boss[7]
                                            if drop == drop1 or drop == drop2 or drop == drop3:
                                                if inventory.count(boss[4]) == 0:
                                                    inventory.append(boss[4])
                                                    inventory.insert(inventory.index(boss[4]) + 1, 1)
                                                    print('You get ' + str(boss[4]))
                                                    break
                                                else:
                                                    junk = inventory.pop(inventory.index(boss[4]) + 1)
                                                    junk += 1
                                                    inventory.insert(inventory.index(boss[4]) + 1, junk)
                                                    print('You get ' + str(boss[4]))
                                                    break
                                            else:
                                                break
                                    while mov != 'cd':
                                        print('Korin:Ge Ge Ge.You win')
                                        print('Korin:Now take your reward')
                                        if maxki < 1500:
                                            maxki = 1500
                                            print('You feel stronger')
                                            print('Your ki ' + str(ki) + '/' + str(maxki))
                                        else:
                                            print('You to strong')
                                        print('Korin:Now you can go')
                                        break
                                    break
                                else:
                                    mov = str(input())
                            else:
                                mov = str(input())
                        else:
                            print('You not enough strong')
                            mov = str(input())
            else:
                mov = str(input())
        g = l.index(1)
        time += 1
        minute += 10
        timer += 1
        if timer >= 30:
            timer = 0
        ran = randrange(0, 10)
        if ran == 2:
            mov = 'sf'
        elif ran == 3 or ran == 4:
            mov = 'f'
        else:
            l.remove(1)
            l.insert(g + 1, 1)
            x += 1
            stance = y, x
            if x >= 8:
                x = 0
            print(l)
            if hp < fullhp - 1:
                hp += regeneration
            mov = str(input())
    elif mov == 'up':
        minute += 10
        y -= 1
        stance = y, x
        if y == -1:
            y = 5
        ind = l.index(1)
        l.remove(1)
        l.insert(ind, 0)
        l = movement(stance, wMap, l)
        print(l)
        mov = input()
    elif mov == 'y':
        week += 1
        mov = input()
    elif mov == 'f':
        enemy = mobSlime
        a = randrange(0, 5)
        if a == 2:
            a = randrange(0, 4)
            if a == 3:
                enemy = mobDragon
        if y == 0:
            a = randrange(0, 3)
            if a == 1:
                enemy = mobSlime
            elif a == 2:
                enemy = mobRat
        elif y == 1:
            if a == 2:
                enemy = mobLizard
            elif a == 5 or a == 1:
                enemy = mobGoblin
            else:
                enemy = mobSlime
        elif y == 2:
            a = randrange(-1, len(mobsLoc4))
            enemy = mobsLoc4[a]
        elif y == 3:
            a = randrange(-1, len(mobsLoc5))
            enemy = mobsLoc5[a]
        elif y == 4:
            if a == 1 or a == 2 or a == 3 or a == 4:
                enemy = mobLizard
            else:
                enemy = mobSlime
        elif y == 5:
            if a == 1 or a == 2 or a == 3 or a == 4:
                enemy = mobLizard
            elif a == 5 or a == 6 or a == 7 or a == 8:
                enemy = mobZombie
            else:
                enemy = mobEmu
        ehp = enemy[1]
        efhp = enemy[3]
        eatk = enemy[2]
        print('You meet ' + enemy[0])
        print('Your health ' + str(hp) + '/' + str(fullhp) + '    ' + enemy[0] + ' health ' + str(ehp) + '/' + str(efhp))
        print('Your ki ' + str(ki) + '/' + str(maxki))
        print('Fist[fist]  Kick[kick]  Skill[sk]')
        mov = str(input())
        yatk = 0
        atk = 0
        sk = 0
        satk = eatk
        while mov != 'surr':
            satk = eatk
            if mov == 'f':
                if hp <= 0:
                    print('You lose')
                    break
                if fistLvL == 3 or fistLvL == 4:
                    yatk += (hand + fistModifier) * 2
                else:
                    yatk += hand + fistModifier
                atk = hand + fistModifier
                hpModifier += eatk
                if hpModifier >= hpMreq:
                    hpModifier -= hpMreq
                    hpRand = randrange(1, fullhp // 10)
                    fullhp += hpRand
                    hpMreq += hpMreq // 2
                    print('Your health increased to ' + str(fullhp))
                print('You dealt damage: ' + str(fistModifier + hand))
                hp += regeneration
                fistMastery += 1
                if fistMastery >= fMreq:
                    fistMastery -= fMreq
                    fistModifier += 5
                    fMreq += fMreq // 2
                    fistLvL += 1
                    print('Your Fist Mastery improved')
                    mov = str(input())
                minute += 30
                timer += 1
            elif mov == 'k':
                if hp <= 0:
                    print('You lose')
                    break
                if kickLvL == 4 or kickLvL == 5:
                    yatk += (kick + kickModifier) * 2
                else:
                    yatk += kick + kickModifier
                atk = kick + kickModifier
                hpModifier += eatk
                if hpModifier >= hpMreq:
                    hpModifier -= hpMreq
                    hpRand = randrange(1, fullhp // 10)
                    fullhp += hpRand
                    hpMreq += hpMreq // 2
                    print('Your health increased to ' + str(fullhp))
                kickMastery += 1
                if kickMastery >= kMreq:
                    kickMastery -= kMreq
                    kickModifier += 10
                    kMreq += kMreq // 2
                    kickLvL += 1
                    print('Your Kick Mastery improved')
                hp += regeneration
                minute += 30
                timer += 1
            elif mov == 'sk':
                if ki - skills[2] >= 0:
                    sk += 1
                    tipe = skills[1]
                    print('You used ' + skills[4] + skills[0] + Color.END)
                    if tipe == 'phy':
                        hp -= skills[2]
                        hpModifier += skills[2]
                        if hpModifier >= hpMreq:
                            hpModifier -= hpMreq
                            hpRand = randrange(1, fullhp // 10)
                            fullhp += hpRand
                            hpMreq += hpMreq // 2
                            print('Your health increased to ' + str(fullhp))
                    else:
                        ki -= skills[2]
                    if tipe == 'atk':
                        yatk += damage
                    elif tipe == 'phy':
                        yatk += damage
                    elif tipe == 'buff':
                        save = physPower
                        eff = damage
                        buff = int(physPower * eff)
                        physPower += buff
                        barehand = physPower // 25
                        hand = barehand + handmodifier
                        kick = int((barehand * 2) // 1.5)
                        print('Your Physical Power increased PhysPower: ' + str(save) + ' to ' + str(physPower))
                    minute += 30
                    timer += 1
                else:
                    print('Not enough ki')
            elif mov == 'i':
                while mov != 'c':
                    print('------------------------------INVENTORY-----------------------------------')
                    print(inventory)
                    print('-------------------------------ACTIONS------------------------------------')
                    print('Close[e]    Use[u]')
                    print('--------------------------------------------------------------------------')
                    mov = str(input())
                    print('--------------------------------------------------------------------------')
                    if mov == 'u':
                        indI = int(input('Chose item: '))
                        print('--------------------------------------------------------------------------')
                        uItem = inventory[indI]
                        tipe = type(uItem)
                        if tipe == 'ки':
                            if toxicity <= 99:
                                pill = eff(uItem)
                                ind = inventory.index(uItem)
                                junk = inventory.pop(ind + 1)
                                junk -= 1
                                if junk > 0:
                                    inventory.insert(ind + 1, junk)
                                else:
                                    inventory.remove(uItem)
                                ki += pill
                                if ki > maxki:
                                    k = ki - maxki
                                    if k <= maxki // 2:
                                        toxicity += 5
                                    elif k > maxki // 2 and k > maxki:
                                        toxicity += 15
                                    else:
                                        toxicity += 40
                                    maxki += k
                                else:
                                    k = 0
                                    toxicity += 5
                                print('You used ' + str(uItem))
                                print('You recovered ' + str(pill) + ' ki')
                                print('Your max ki increased on ' + str(k) + ' ki')
                            else:
                                print('Toxicity is very high')
                        elif tipe == 'фс':
                            if hp > fullhp // 2 - 1:
                                pill = eff(uItem)
                                hp -= pill
                                ind = inventory.index(uItem)
                                junk = inventory.pop(ind + 1)
                                junk -= 1
                                if junk > 0:
                                    inventory.insert(ind + 1, junk)
                                else:
                                    inventory.remove(uItem)
                                physPower += pill
                                barehand = physPower // 25
                                hand = barehand + handmodifier
                                kick = int((barehand * 2) // 1.5)
                                print('You used ' + str(uItem))
                                print('Your Heath decreased to ' + str(pill))
                                print('Your Physical Power increased to ' + str(pill))
                        elif tipe == 'тт':
                            pill = eff(uItem)
                            ind = inventory.index(uItem)
                            junk = inventory.pop(ind + 1)
                            junk -= 1
                            if junk > 0:
                                inventory.insert(ind + 1, junk)
                            else:
                                inventory.remove(uItem)
                            talent += pill
                            if uItem == 'Chudo Rastenie +5 тт':
                                print('You used ' + Color.Yellow + uItem + Color.END)
                            else:
                                print('You used ' + str(uItem))
                            print('Your talent increased to ' + str(pill))
                        elif tipe == '%':
                            pill = eff(uItem)
                            ind = inventory.index(uItem)
                            junk = inventory.pop(ind + 1)
                            junk -= 1
                            if junk > 0:
                                inventory.insert(ind + 1, junk)
                            else:
                                inventory.remove(uItem)
                            toxicity -= pill
                            time += 1
                            print('You used ' + str(uItem))
                            print('Your toxicity decreased to ' + str(pill))
                        elif tipe == 'хп':
                            if toxicity < 100:
                                pill = eff(uItem)
                                ind = inventory.index(uItem)
                                junk = inventory.pop(ind + 1)
                                junk -= 1
                                if junk > 0:
                                    inventory.insert(ind + 1, junk)
                                else:
                                    inventory.remove(uItem)
                                hp += pill
                                if hp >= fullhp:
                                    k = hp - fullhp
                                    hp -= k
                                    fullhp += k // 100
                                    pill -= k
                                    k = k // 100
                                else:
                                    k = 0
                                toxicity += 5
                                print('You used ' + str(uItem))
                                print('You recovered ' + str(pill) + ' hp')
                                print('Your Max HP increased on ' + str(k) + ' hp')
                            else:
                                print('Toxicity is very high')
                        elif tipe == 'ун':
                            print('You use ' + inventory[indI])
                            ef = eff(uItem)
                            ehp -= ef
                            print('You dealt: ' + str(ef) + ' damage')
                            hp -= eatk
                            ind = inventory.index(uItem)
                            junk = inventory.pop(ind + 1)
                            junk -= 1
                            if junk > 0:
                                inventory.insert(ind + 1, junk)
                            else:
                                inventory.remove(uItem)
                        print('Your health ' + str(hp) + '/' + str(fullhp) + '    ' + enemy[0] + ' health ' + str(
                            ehp) + '/' + str(efhp))
                        print('Your ki ' + str(ki) + '/' + str(maxki))
                    elif mov == 'e':
                        break
            elif mov == 'tec':
                print('Select technique:')
                print(curTechs)
                mov = int(input())
                tech = curTechs[mov]
                if tech == 'Lightning':
                    tech = Lightning
                elif tech == 'Drain':
                    tech = Drain
                if ki - tech.cost >= 0:
                    char = [ki, ehp, eatk, hp]
                    tech.requiremnt(tech.allPar, tech.allPar, char)
                    tech.action(tech.allPar, char, tech.allPar)
                    ki = char[0]
                    ehp = char[1]
                    hp = char[3]
                    tech.tecname(tech.name, tech.allPar)
                    print('Fist[fist]  Kick[kick]  Skill[sk]')
                else:
                    print('Not enough ki')
                mov = str(input())
            elif mov == 'run':
                print('You ran from battle')
                break
            else:
                pass
            ehp -= yatk
            yatk = 0
            if eatk - armor >= 0:
                hp -= eatk - armor
                satk -= armor
            else:
                hp -= 0
                satk = 0
            if sk == 1:
                print('You dealt: ' + str(damage) + ' Damage' + '     ' + enemy[0] + ' dealt: ' + str(satk) + ' Damage')
                sk = 0
            else:
                print('You dealt: ' + str(atk) + ' Damage' + '      ' + enemy[0] + ' dealt: ' + str(satk) + ' Damage')
            print('Your health ' + str(hp) + '/' + str(fullhp) + '       ' + enemy[0] + ' health ' + str(
                ehp) + '/' + str(efhp))
            print('Your ki ' + str(ki) + '/' + str(maxki))
            mov = str(input())
            if hp <= 0:
                print('You lose')
                if save != 0:
                    physPower = save
                    barehand = physPower // 25
                    hand = barehand + handmodifier
                    kick = int((barehand * 2) // 1.5)
                break
            elif ehp <= 0:
                print('You win')
                drop = randrange(0, 5)
                if save != 0:
                    physPower = save
                    barehand = physPower // 25
                    hand = barehand + handmodifier
                    kick = int((barehand * 2) // 1.5)
                if drop == 3:
                    if inventory.count(enemy[4]) == 0:
                        inventory.append(enemy[4])
                        inventory.insert(inventory.index(enemy[4]) + 1, 1)
                        print('You get ' + str(enemy[4]))
                        break
                    else:
                        junk = inventory.pop(inventory.index(enemy[4]) + 1)
                        junk += 1
                        inventory.insert(inventory.index(enemy[4]) + 1, junk)
                        print('You get ' + str(enemy[4]))
                        break
                else:
                    break
    elif mov == 'sf':
        if y == 3:
            enemy = Wolf
        elif y == 4:
            enemy == Enemy
        elif y == 5:
            enemy = BlackSabbath
        else:
            enemy = Hound
        ehp = enemy.health[0]
        print('You met ' + enemy.name)
        while mov != 1:
            print('--------------------------------------------------------------------------')
            print('Your health: ' + str(hp) + '/' + str(fullhp) + '    ' + enemy.name + ' health: ' + str(ehp) + '/' + str(enemy.health[1]))
            print('Your ki: ' + str(ki) + '/' + str(maxki))
            print('--------------------------------------------------------------------------')
            mov = input()
            if mov == 'f':
                if hp <= 0:
                    print('You lose')
                    break
                if fistLvL == 3 or fistLvL == 4:
                    ehp -= (hand + fistModifier) * 2
                else:
                    ehp -= hand + fistModifier
                atk = hand + fistModifier
                hpModifier += enemy.allPar[2] - armor
                if hpModifier >= hpMreq:
                    hpModifier -= hpMreq
                    hpRand = randrange(1, fullhp // 10)
                    fullhp += hpRand
                    hpMreq += hpMreq // 2
                    print('Your health increased to ' + str(fullhp))
                print('You dealt damage: ' + str(fistModifier + hand))
                hp += regeneration
                fistMastery += 1
                if fistMastery >= fMreq:
                    fistMastery -= fMreq
                    fistModifier += 5
                    fMreq += fMreq // 2
                    fistLvL += 1
                    print('Your Fist Mastery improved')
                    mov = str(input())
                minute += 30
            elif mov == 'k':
                if hp <= 0:
                    print('You lose')
                    break
                if kickLvL == 4 or kickLvL == 5:
                    ehp -= (kick + kickModifier) * 2
                else:
                    ehp -= kick + kickModifier
                atk = kick + kickModifier
                hpModifier += enemy.allPar[2] - armor
                if hpModifier >= hpMreq:
                    hpModifier -= hpMreq
                    hpRand = randrange(1, fullhp // 10)
                    fullhp += hpRand
                    hpMreq += hpMreq // 2
                    print('Your health increased to ' + str(fullhp))
                kickMastery += 1
                if kickMastery >= kMreq:
                    kickMastery -= kMreq
                    kickModifier += 10
                    kMreq += kMreq // 2
                    kickLvL += 1
                    print('Your Kick Mastery improved')
                hp += regeneration
                minute += 30
            elif mov == 'sk':
                if ki - skills[2] >= 0:
                    tipe = skills[1]
                    print('You used ' + skills[4] + skills[0] + Color.END)
                    if tipe == 'phy':
                        hp -= skills[2]
                        hpModifier += skills[2]
                        if hpModifier >= hpMreq:
                            hpModifier -= hpMreq
                            hpRand = randrange(1, fullhp // 10)
                            fullhp += hpRand
                            hpMreq += hpMreq // 2
                            print('Your health increased to ' + str(fullhp))
                    else:
                        ki -= skills[2]
                    if tipe == 'atk':
                        ehp -= damage
                    elif tipe == 'phy':
                        ehp -= damage
                    elif tipe == 'buff':
                        save = physPower
                        eff = damage
                        buff = int(physPower * eff)
                        physPower += buff
                        barehand = physPower // 25
                        hand = barehand + handmodifier
                        kick = int((barehand * 2) // 1.5)
                        print('Your Physical Power increased PhysPower: ' + str(save) + ' to ' + str(physPower))
                    minute += 30
                else:
                    print('Not enough ki')
            elif mov == 'i':
                while mov != 'c':
                    print('------------------------------INVENTORY-----------------------------------')
                    print(inventory)
                    print('-------------------------------ACTIONS------------------------------------')
                    print('Close[e]    Use[u]')
                    print('--------------------------------------------------------------------------')
                    mov = str(input())
                    print('--------------------------------------------------------------------------')
                    if mov == 'u':
                        indI = int(input('Chose item: '))
                        print('--------------------------------------------------------------------------')
                        uItem = inventory[indI]
                        tipe = type(uItem)
                        if tipe == 'ки':
                            if toxicity <= 99:
                                pill = eff(uItem)
                                ind = inventory.index(uItem)
                                junk = inventory.pop(ind + 1)
                                junk -= 1
                                if junk > 0:
                                    inventory.insert(ind + 1, junk)
                                else:
                                    inventory.remove(uItem)
                                ki += pill
                                if ki > maxki:
                                    k = ki - maxki
                                    if k <= maxki // 2:
                                        toxicity += 5
                                    elif k > maxki // 2 and k > maxki:
                                        toxicity += 15
                                    else:
                                        toxicity += 40
                                    maxki += k
                                else:
                                    k = 0
                                    toxicity += 5
                                print('You used ' + str(uItem))
                                print('You recovered ' + str(pill) + ' ki')
                                print('Your max ki increased on ' + str(k) + ' ki')
                            else:
                                print('Toxicity is very high')
                        elif tipe == 'фс':
                            if hp > fullhp // 2 - 1:
                                pill = eff(uItem)
                                hp -= pill
                                ind = inventory.index(uItem)
                                junk = inventory.pop(ind + 1)
                                junk -= 1
                                if junk > 0:
                                    inventory.insert(ind + 1, junk)
                                else:
                                    inventory.remove(uItem)
                                physPower += pill
                                barehand = physPower // 25
                                hand = barehand + handmodifier
                                kick = int((barehand * 2) // 1.5)
                                print('You used ' + str(uItem))
                                print('Your Heath decreased to ' + str(pill))
                                print('Your Physical Power increased to ' + str(pill))
                        elif tipe == 'тт':
                            pill = eff(uItem)
                            ind = inventory.index(uItem)
                            junk = inventory.pop(ind + 1)
                            junk -= 1
                            if junk > 0:
                                inventory.insert(ind + 1, junk)
                            else:
                                inventory.remove(uItem)
                            talent += pill
                            if uItem == 'Chudo Rastenie +5 тт':
                                print('You used ' + Color.Yellow + uItem + Color.END)
                            else:
                                print('You used ' + str(uItem))
                            print('Your talent increased to ' + str(pill))
                        elif tipe == '%':
                            pill = eff(uItem)
                            ind = inventory.index(uItem)
                            junk = inventory.pop(ind + 1)
                            junk -= 1
                            if junk > 0:
                                inventory.insert(ind + 1, junk)
                            else:
                                inventory.remove(uItem)
                            toxicity -= pill
                            time += 1
                            print('You used ' + str(uItem))
                            print('Your toxicity decreased to ' + str(pill))
                        elif tipe == 'хп':
                            if toxicity < 100:
                                pill = eff(uItem)
                                ind = inventory.index(uItem)
                                junk = inventory.pop(ind + 1)
                                junk -= 1
                                if junk > 0:
                                    inventory.insert(ind + 1, junk)
                                else:
                                    inventory.remove(uItem)
                                hp += pill
                                if hp >= fullhp:
                                    k = hp - fullhp
                                    hp -= k
                                    fullhp += k // 100
                                    pill -= k
                                    k = k // 100
                                else:
                                    k = 0
                                toxicity += 5
                                print('You used ' + str(uItem))
                                print('You recovered ' + str(pill) + ' hp')
                                print('Your Max HP increased on ' + str(k) + ' hp')
                            else:
                                print('Toxicity is very high')
                        elif tipe == 'ун':
                            print('You use ' + inventory[indI])
                            ef = eff(uItem)
                            ehp -= ef
                            print('You dealt: ' + str(ef) + ' damage')
                            hp -= eatk
                            ind = inventory.index(uItem)
                            junk = inventory.pop(ind + 1)
                            junk -= 1
                            if junk > 0:
                                inventory.insert(ind + 1, junk)
                            else:
                                inventory.remove(uItem)
                        print('Your health ' + str(hp) + '/' + str(fullhp) + '    ' + enemy[0] + ' health ' + str(
                            ehp) + '/' + str(efhp))
                        print('Your ki ' + str(ki) + '/' + str(maxki))
                    elif mov == 'e':
                        break
            elif mov == 'tec':
                print('Select technique:')
                print(curTechs)
                mov = int(input())
                tech = curTechs[mov]
                if tech == 'Lightning':
                    tech = Lightning
                elif tech == 'Drain':
                    tech = Drain
                if ki - tech.cost >= 0:
                    char = [ki, ehp, eatk, hp]
                    tech.requiremnt(tech.allPar, tech.allPar, char)
                    tech.action(tech.allPar, char, tech.allPar)
                    ki = char[0]
                    ehp = char[1]
                    hp = char[3]
                    tech.tecname(tech.name, tech.allPar)
                    print('Fist[fist]  Kick[kick]  Skill[sk]')
                else:
                    print('Not enough ki')
                mov = str(input())
            elif mov == 'run':
                break
            a = randrange(0, 5)
            char = [ki, hand, kick, hp, enemy.atk, enemy.health[0], inventory, armor]

            if a == 1:
                enemy.special(enemy, enemy.allPar, char)
            else:
                enemy.ussual(enemy.allPar, enemy.allPar, char)
            hp = char[3]
            hand = char[1]
            enemy.atk = char[4]
            kick = char[2]
            ki = char[0]
            drop = enemy.allPar[4]
            if hp <= 0 + 1:
                print('You Lost')
                break
            if ehp <= 0:
                print('You Won')
                a = randrange(0, 2)
                if a == 1:
                    if inventory.count(drop) == 0:
                        inventory.append(drop)
                        inventory.append(1)
                    else:
                        ind = inventory.index(drop)
                        junk = inventory.pop(ind + 1)
                        junk += 1
                        inventory.insert(ind + 1, junk)
                    print('You get: ' + enemy.allPar[4])
                else:
                    pass
                break
    elif mov == 'boss':
        boss = bossKorin
        bhp = boss[1]
        bfhp = boss[3]
        batk = boss[2]
        bki = boss[11]
        bmki = boss[10]
        print('You meet ' + boss[0])
        print(boss[0] + ' health ' + str(ehp) + '/' + str(efhp))
        print(boss[0] + ' ki ' + str(bki) + '/' + str(bmki))
        print('Your health ' + str(hp) + '/' + str(fullhp))
        print('Your ki ' + str(ki) + '/' + str(maxki))
        mov = str(input())
        while mov != 'surr':
            if mov == 'fist':
                if hp <= 0:
                    print('You lose')
                    break
                if ki > 0:
                    if fistLvL == 3 or fistLvL == 4:
                        bhp -= (hand + fistModifier) * 2 + (kiPower // 100) * kiLvL
                        ki -= kiPower // 100 * kiLvL
                    else:
                        bhp -= hand + fistModifier + (kiPower // 100) * kiLvL
                        ki -= kiPower // 100 * kiLvL
                    kiMastery += kiPower // 100 * kiLvL
                    if kiMastery >= kiMreq:
                        kiMastery -= kiMreq
                        kiLvL += 1
                        kickModifier += 1
                        kMreq += kiMreq // 2
                        kiRand = randrange(1, (maxki // 10) // 2)
                        maxki += kiRand * (talent // 2)
                        print('Your Ki Mastery increased to ' + str(kiLvL))
                        print('Your Max Ki increased to ' + str(maxki))
                else:
                    if fistLvL == 3 or fistLvL == 4:
                        bhp -= (hand + fistModifier) * 2
                    else:
                        bhp -= hand + fistModifier
                print(enemy[0] + ' Health ' + str(ehp) + '/' + str(efhp))
                print(boss[0] + ' ki ' + str(bki) + '/' + str(bmki))
                hp -= batk
                hpModifier += batk
                if hpModifier >= hpMreq:
                    hpModifier -= hpMreq
                    hpRand = randrange(1, fullhp // 10)
                    fullhp += hpRand
                    hpMreq += hpMreq // 2
                    print('Your health increased to ' + str(fullhp))
                print('Your health ' + str(hp) + '/' + str(fullhp))
                print('Your ki ' + str(ki) + '/' + str(maxki))
                fistMastery += 1
                if fistMastery >= fMreq:
                    fistMastery -= fMreq
                    fistModifier += 5
                    fMreq += fMreq // 2
                    fistLvL += 1
                    print('Your Fist Mastery improved')
                    mov = str(input())
                mov = str(input())
            elif mov == 'kick':
                if hp <= 0:
                    print('You lose')
                    break
                if ki > 0:
                    if kickLvL == 4 or kickLvL == 5:
                        bhp -= (kick + kickModifier) * 2 + (kiPower // 100) * kiLvL
                        ki -= kiPower // 100 * kiLvL
                    else:
                        bhp -= kick + kickModifier + (kiPower // 100) * kiLvL
                        ki -= kiPower // 100 * kiLvL
                kiMastery += kiPower // 100 * kiLvL
                if kiMastery >= kiMreq:
                    kiMastery -= kiMreq
                    kiLvL += 1
                    kickModifier += 1
                    kMreq += kiMreq // 2
                    kiRand = randrange(1, (maxki // 10) // 2)
                    maxki += kiRand * (talent // 2)
                    print('Your Ki Mastery increased to ' + str(kiLvL))
                    print('Your Max Ki increased to ' + str(maxki))
                else:
                    if kickLvL == 4 or kickLvL == 5:
                        bhp -= (kick + kickModifier) * 2
                    else:
                        bhp -= kick + kickModifier
                print(boss[0] + ' Health ' + str(bhp) + '/' + str(bfhp))
                print(boss[0] + ' ki ' + str(bki) + '/' + str(bmki))
                hp -= batk
                hpModifier += batk
                if hpModifier >= hpMreq:
                    hpModifier -= hpMreq
                    hpRand = randrange(1, fullhp // 10)
                    fullhp += hpRand
                    hpMreq += hpMreq // 2
                    print('Your health increased to ' + str(fullhp))
                print('Your health ' + str(hp) + '/' + str(fullhp))
                print('Your ki ' + str(ki) + '/' + str(maxki))
                kickMastery += 1
                print(kickMastery)
                if kickMastery >= kMreq:
                    kickMastery -= kMreq
                    kickModifier += 10
                    kMreq += kMreq // 2
                    kickLvL += 1
                    print('Your Kick Mastery improved')
                    mov = str(input())
                mov = str(input())
            elif mov == 'ki':
                if ki > 0:
                    if kiLvL == 5 and kiLvL <= 10:
                        kicons = int(input())
                        if kicons * 10 <= ki:
                            bhp -= ((kicons * (physPower // 100)) * kiModifier) * 2
                            ki -= ((kicons * 10) * 2) // kiControl // 10
                            print(enemy[0] + ' Health ' + str(ehp) + '/' + str(efhp))
                            print(boss[0] + ' ki ' + str(bki) + '/' + str(bmki))
                            kiMastery += (kicons * 10) * 2
                            if kiMastery >= kMreq:
                                kiMastery -= kMreq
                                kiLvL += 1
                                kickModifier += 1
                                kMreq += kiMreq // 2
                                kiRand = randrange(1, (maxki // 10) // 2)
                                maxki += kiRand * (talent // 2)
                                print('Your Ki Mastery increased to ' + str(kiLvL))
                                print('Your Max Ki increased to ' + str(maxki))
                            hp -= batk
                            hpModifier += batk
                            if hpModifier >= hpMreq:
                                hpModifier -= hpMreq
                                hpRand = randrange(1, fullhp // 10)
                                fullhp += hpRand
                                hpMreq += hpMreq // 2
                                print('Your health increased to ' + str(fullhp))
                            print('Your health ' + str(hp) + '/' + str(fullhp))
                            print('Your ki ' + str(ki) + '/' + str(maxki))

                        else:
                            print('Not enough ki')
                            mov = str(input())
                    else:
                        kicons = maxki // 10
                        if kicons * 2 <= ki + 1:
                            bhp -= (kicons * (kiPower // 75)) * kiModifier
                            ki -= kicons * 2 // kiControl
                            print(enemy[0] + ' Health ' + str(ehp) + '/' + str(efhp))
                            print(boss[0] + ' ki ' + str(bki) + '/' + str(bmki))
                            kiMastery += kicons
                            if kiMastery >= kiMreq:
                                kiMastery -= kiMreq
                                kiLvL += 1
                                kickModifier += 1
                                kMreq += kiMreq // 2
                                kiRand = randrange(1, (maxki // 10) // 2)
                                maxki += kiRand * (talent // 2)
                                print('Your Ki Mastery increased to ' + str(kiLvL))
                                print('Your Max Ki increased to ' + str(maxki))
                            hp -= batk
                            hpModifier += batk
                            if hpModifier >= hpMreq:
                                hpModifier -= hpMreq
                                hpRand = randrange(1, fullhp // 10)
                                fullhp += hpRand
                                hpMreq += hpMreq // 2
                                print('Your health increased to ' + str(fullhp))
                            print('Your health ' + str(hp) + '/' + str(fullhp))
                            print('Your ki ' + str(ki) + '/' + str(maxki))
                            mov = str(input())
                        else:
                            print('Not enough ki')
                            mov = str(input())
                else:
                    print('Not enough ki')
                    mov = str(input())
            elif mov == 'run':
                print('You ran from battle')
                break
            else:
                print('Unknown action')
                mov = str(input())
            if hp <= 0:
                print('You lose')
                break
            elif ehp <= 0:
                print('You win')
                droprange1 = boss[8]
                droprange2 = boss[9]
                drop = randrange(droprange1, droprange2)
                drop1 = boss[5]
                drop2 = boss[6]
                drop3 = boss[7]
                if drop == drop1 or drop == drop2 or drop == drop3:
                    if inventory.count(boss[4]) == 0:
                        inventory.append(boss[4])
                        inventory.insert(inventory.index(boss[4]) + 1, 1)
                        print('You get ' + str(boss[4]))
                        break
                    else:
                        junk = inventory.pop(inventory.index(boss[4]) + 1)
                        junk += 1
                        inventory.insert(inventory.index(boss[4]) + 1, junk)
                        print('You get ' + str(boss[4]))
                        break
                else:
                    break
    elif mov == 'i':
        while mov != 'c':
            print('------------------------------INVENTORY-----------------------------------')
            print(inventory)
            print('-------------------------------ACTIONS------------------------------------')
            print('Close[e]    Use[u]')
            print('--------------------------------------------------------------------------')
            mov = str(input())
            print('--------------------------------------------------------------------------')
            if mov == 'u':
                indI = int(input('Chose item: '))
                print('--------------------------------------------------------------------------')
                uItem = inventory[indI]
                tipe = type(uItem)
                if tipe == 'ки':
                    if toxicity + 20 <= 99:
                        pill = eff(uItem)
                        ind = inventory.index(uItem)
                        junk = inventory.pop(ind + 1)
                        junk -= 1
                        if junk > 0:
                            inventory.insert(ind + 1, junk)
                        else:
                            inventory.remove(uItem)
                        ki += pill
                        if ki > maxki:
                            k = ki - maxki
                        else:
                            k = 0
                        maxki += k
                        toxicity += 20
                        print('You used ' + str(uItem))
                        print('You recovered ' + str(pill) + ' ki')
                        print('Your max ki increased on ' + str(k) + ' ki')
                    else:
                        print('Toxicity is very high')
                elif tipe == 'фс':
                    if hp > fullhp // 2 - 1:
                        pill = eff(uItem)
                        hp -= pill
                        ind = inventory.index(uItem)
                        junk = inventory.pop(ind + 1)
                        junk -= 1
                        if junk > 0:
                            inventory.insert(ind + 1, junk)
                        else:
                            inventory.remove(uItem)
                        physPower += pill
                        barehand = physPower // 25
                        hand = barehand + handmodifier
                        kick = int((barehand * 2) // 1.5)
                        print('You used ' + str(uItem))
                        print('Your Heath decreased to ' + str(pill))
                        print('Your Physical Power increased to ' + str(pill))
                elif tipe == 'тт':
                    pill = eff(uItem)
                    ind = inventory.index(uItem)
                    junk = inventory.pop(ind + 1)
                    junk -= 1
                    if junk > 0:
                        inventory.insert(ind + 1, junk)
                    else:
                        inventory.remove(uItem)
                    talent += pill
                    if uItem == 'Chudo Rastenie +5 тт':
                        print('You used ' + Color.Yellow + uItem + Color.END)
                    else:
                        print('You used ' + str(uItem))
                    print('Your talent increased to ' + str(pill))
                elif tipe == '%':
                    pill = eff(uItem)
                    ind = inventory.index(uItem)
                    junk = inventory.pop(ind + 1)
                    junk -= 1
                    if junk > 0:
                        inventory.insert(ind + 1, junk)
                    else:
                        inventory.remove(uItem)
                    toxicity -= pill
                    hour += 1
                    print('You used ' + str(uItem))
                    print('Your toxicity decreased to ' + str(pill))
                elif tipe == 'хп':
                    if toxicity < 100:
                        minute += 30
                        pill = eff(uItem)
                        ind = inventory.index(uItem)
                        junk = inventory.pop(ind + 1)
                        junk -= 1
                        if junk > 0:
                            inventory.insert(ind + 1, junk)
                        else:
                            inventory.remove(uItem)
                        hp += pill
                        if hp >= fullhp:
                            k = hp - fullhp
                            hp -= k
                            fullhp += k // 100
                            pill -= k
                            k = k // 100
                        else:
                            k = 0
                        toxicity += 5
                        print('You used ' + str(uItem))
                        print('You recovered ' + str(pill) + ' hp')
                        print('Your Max HP increased on ' + str(k) + ' hp')
                    else:
                        print('Toxicity is very high')
                elif tipe == 'ун':
                    print('Incorrect target')
                elif tipe == 'вс':
                    print('You used ' + uItem)
                    ef = eff(uItem)
                    kiRecovery += ef
                    day += ef * 10
                    ki = 0
                    year += 1
                    print('Ki Recover: +' + str(ef))
                    print('Ki = 0')
                    junk = inventory.pop(indI + 1)
                    junk -= 1
                    if junk == 0:
                        inventory.remove(uItem)
                    else:
                        inventory.insert(indI + 1, junk)
                elif tipe == 'св':
                    print('You use ' + uItem)
                    skill = ''
                    ind = 4
                    for i in uItem:
                        r = uItem[ind]
                        skill += r
                        ind += 1
                        if ind == len(uItem):
                            break
                    curSkills.append(skill)
                    inventory.pop(indI + 1)
                    inventory.remove(uItem)
                    month += 1
                    print('Now you can use: ' + str(skill))
            elif mov == 'e':
                break
    elif mov == 'l':
        if loc4 == [0, 0, 1, 0, 2, 0, 0, 0, 0]:
            print('You see town')
            print('Enter?')
            mov = str(input())
            if mov == 'yes':
                while mov != 'exit':
                    print('You see inn')
                    print('You see shop')
                    mov = str(input())
                    if mov == 'inn':
                        gold -= (fullhp - hp) // 10
                        hp = fullhp
                        print('You rested')
                        mov = str(input())
                    elif mov == 'shop':
                        print('Choose action: buy/sell')
                        mov = str(input())
                        if mov == 'buy':
                            while mov != 'exit':
                                print('Your gold ' + str(gold))
                                print('Leather gloves +10 hands damage.Price:50 gold')
                                mov = str(input())
                                if mov == 'lg':
                                    if gold >= 0:
                                        handmodifier += 10
                                        hand = barehand + handmodifier
                                        gold -= 50
                                        print('You bought Leather gloves')
                                        mov = str(input())
                                    else:
                                        print('Not enough gold')
                                        mov = str(input())
                                else:
                                    print('Unknown thing')
                                    mov = str(input())
                        elif mov == 'sell':
                            while mov != 'exit':
                                print('Your gold ' + str(gold))
                                print('What you want to sell?')
                                print(inventory)
                                sellStuff = str(input())
                                ss = inventory.index(sellStuff)
                                ss1 = ss + 1
                                sq = inventory.pop(ss1)
                                stuffPrice = 0
                                if sellStuff == 'slime':
                                    stuffPrice = 5
                                elif sellStuff == 'venom':
                                    stuffPrice = 10
                                elif sellStuff == 'lizard meat':
                                    stuffPrice = 20
                                sellSum = stuffPrice * sq
                                gold += sellSum
                                inventory.remove(sellStuff)
                                print('You sell ' + sellStuff + ' for ' + str(sellSum) + ' gold')
                                mov = str(input())
                        else:
                            print('Unknown action')
                            mov = str(input())
                    elif mov == 'exit':
                        print('You see a valley')
                        break
                    else:
                        print('Unknown destination')
                        mov = str(input())
            else:
                mov = str(input())
        ran = randrange(0, 10)
        minute += 10
        timer += 1
        if ran == 2:
            if ran == 2:
                mov = 'sf'
            elif ran == 3 or ran == 4:
                mov = 'f'
        else:
            g = l.index(1)
            l.remove(1)
            l.insert(g - 1, 1)
            x -= 1
            if x <= 0:
                x = 8
            print(l)
            if hp < fullhp - 1:
                hp += regeneration
            mov = str(input())
    elif mov == 'map':
        print(loc1)
        print(loc2)
        print(loc3)
        print(loc4)
        print(loc5)
        print(loc6)
        mov = str(input())
    elif mov == 'm':
        ent = str(input())
        if ent == 'l1':
            if loc1 == [0, 0, 0, 0, 0, 0, 0, 0, 3]:
                loc2.remove(1)
                loc2.insert(0, 0)
                loc1.remove(0)
                loc1.insert(g + 1, 1)
                curLoc = loc1
                l = loc1
                time += 1
                timer += 1
                print(l)
                if hp < fullhp:
                    hp += regeneration
                mov = str(input())
            else:
                l = loc1
                print(l)
                mov = str(input())
        elif ent == 'l2':
            if loc2 == [0, 0, 0, 0, 0, 0, 0, 0, 0]:
                loc1.remove(1)
                loc1.insert(0, 0)
                loc2.remove(0)
                loc2.insert(g + 1, 1)
                curLoc = loc2
                l = loc2
                time += 1
                timer += 1
                print(l)
                if hp < fullhp:
                    hp += regeneration
                mov = str(input())
            else:
                l = loc2
                print(l)
                mov = str(input())
        elif ent == 'l3':
            if loc3 == [0, 0, 0, 0, 0, 0, 0, 0, 0]:
                loc2.remove(1)
                loc2.insert(0, 0)
                loc3.remove(0)
                loc3.insert(g + 1, 1)
                curLoc = loc3
                l = loc3
                time += 1
                timer += 1
                print(l)
                if hp < fullhp:
                    hp += regeneration
                mov = str(input())
            else:
                l = loc3
                print(l)
                mov = str(input())
        elif ent == 'l4':
            if loc4 == [0, 0, 0, 0, 2, 0, 0, 0, 0]:
                loc3.remove(1)
                loc3.insert(0, 0)
                loc4.remove(0)
                loc4.insert(g + 1, 1)
                curLoc = loc4
                l = loc4
                time += 1
                timer += 1
                print(l)
                if hp < fullhp:
                    hp += regeneration
                mov = str(input())
            else:
                l = loc4
                print(l)
                mov = str(input())
        elif ent == 'l5':
            if loc5 == [0, 0, 0, 0, 0, 0, 0, 0, 0]:
                loc4.remove(1)
                loc4.insert(0, 0)
                loc5.remove(0)
                loc5.insert(g + 1, 1)
                curLoc = loc5
                l = loc5
                time += 1
                timer += 1
                print(l)
                if hp < fullhp:
                    hp += regeneration
                mov = str(input())
            else:
                l = loc5
                print(l)
                mov = str(input())
        elif ent == 'l6':
            if loc6 == [0, 0, 0, 0, 0, 0, 0, 0, 0]:
                loc5.remove(1)
                loc5.insert(0, 0)
                loc6.remove(0)
                loc6.insert(g + 1, 1)
                curLoc = loc6
                l = loc6
                time += 1
                timer += 1
                print(l)
                if hp < fullhp:
                    hp += regeneration
                mov = str(input())
            else:
                l = loc6
                print(l)
                hp += regeneration
                mov = str(input())
        else:
            print('Unknown location')
            mov = str(input())
    elif mov == 'stat':
        armor = physPower // 50
        barehand = physPower // 25
        hand = barehand + handmodifier
        kick = int((barehand * 2) // 1.5)
        print('-------------------------------STATISTICS---------------------------------')
        print('Your gold ' + str(gold) + '  Your health ' + str(hp) + '/' + str(fullhp) + '  ' + 'Your ki ' + str(ki) + '/' + str(maxki)
              + '  Armor ' + str(armor))
        print('----------------------------CHARACTERISTICS-------------------------------')
        print('Ki Control ' + str(kiControl) + '  ' + 'Talent ' + str(talent) + '  ' + 'Ki Power ' + str(kiPower))
        print('Hand Damage ' + str(hand) + '  ' + 'Kick Damage ' + str(kick) + '  ' + 'Physical Power ' + str(physPower))
        print('Fist Mastery lvl:' + str(fistLvL) + '  ' + 'Kick Mastery lvl:' + str(kickLvL) + '  ' + 'Ki Mastery lvl:' + str(kiLvL))
        print('------------------------------CULTIVATION---------------------------------')
        print('Cultivation:' + cultivationGrades[t] + ' ' + str(culLvL) + ' Stage')
        print('--------------------------------------------------------------------------')
        mov = str(input())
    elif mov == 'bl':
        elems = [neutElem, fireElem, windElem, earthElem, waterElem]
        mainElemPow = max(elems)
        indElem = elems.index(mainElemPow)
        mainElem = elements[indElem]
        print('Elemental Blood')
        print('Main Element: ' + mainElem)
        print('Neutral: ' + str(neutElem) + '%')
        print('Fire: ' + str(fireElem) + '%')
        print('Wind: ' + str(windElem) + '%')
        print('Earth: ' + str(earthElem) + '%')
        print('Water: ' + str(waterElem) + '%')
        mov = input()
    elif mov == 'p':
        print('--------------------------------------------------------------------------')
        if ki <= maxki - 1:
            timeCost = ((maxki - ki) // talent) // kiRecovery
            hour += timeCost * 10
            if hp < fullhp:
                hp += regeneration * timeCost
            kiAdd = (maxki - ki) // 10
            maxki += kiAdd + talent
            ki = maxki
            print('You recovered ki')
            print('You meditated ' + str(timeCost) + ' t/u')
            if culLvL != 10:
                if h < 41:
                    if ki >= culReq[h]:
                        if culLvL != 10:
                            print('--------------------------------------------------------------------------')
                            print('Your current cultivation ' + cultivationGrades[t] + ' ' + str(culLvL) + ' Stage')
                            print('You can up to  ' + cultivationGrades[t] + ' ' + str(culLvL + 1) + ' Stage')
                            print('Yes[1]  Hold[2]')
                            print('--------------------------------------------------------------------------')
                            if genkai == 3:
                                print('You cant more hold your cultivation')
                                mov = '1'
                            else:
                                mov = str(input())
                            print('--------------------------------------------------------------------------')
                            if mov == '1':
                                kiPower += kiPower // kPM
                                culLvL += 1
                                toxicity -= 5
                                maxtime += 100 + tM
                                fullhp += fullhp // 10
                                h += 1
                                print('You success your gap to ' + cultivationGrades[t] + ' ' + str(culLvL) + ' Stage')
                                print('Next Stage require ' + str(ki) + '/' + str(culReq[h]))
                                genkai = 0
                            else:
                                genkai += 1
                                mov = str(input())
                        elif culLvL == 10:
                            print('--------------------------------------------------------------------------')
                            print('Your current cultivation ' + cultivationGrades[t] + ' ' + str(culLvL) + ' Stage')
                            print('You can do a gap to ' + cultivationGrades[t + 1])
                            print('Yes[1]  Hold[2]')
                            print('--------------------------------------------------------------------------')
                            if genkai == 3:
                                print('You cant more hold  your cultivation')
                                mov = '1'
                            else:
                                mov = str(input())
                                print('--------------------------------------------------------------------------')
                            if mov == '1':
                                maxki += mkM
                                toxicity -= 10
                                maxtime += 200 * t
                                mkM += mkM * t
                                kiPower += kiPower // 5
                                t += 1
                                if t == 2:
                                    kPM -= 1
                                    tM += 100
                                culLvL = 1
                                fullhp += fullhp // 5
                                print('Success gap: ' + str(cultivationGrades[t - 1]) + ' => ' + str(cultivationGrades[t]))
                                genkai = 0
                            else:
                                genkai += 1
                                mov = str(input())
                        else:
                            mov = str(input())
                    else:
                        print('--------------------------------------------------------------------------')
                        print('To power up you need: ' + str(ki) + '/' + str(culReq[h]) + ' ki')
                        print('You need more practice')
                        print('--------------------------------------------------------------------------')
                        mov = input()
                else:
                    print('You have reached the limit of Cultivation')
                    mov = input()
        else:
            print('You not enough tired')
        print('--------------------------------------------------------------------------')
        mov = str(input())
    elif mov == 'ref':
        while True:
            print('-----------------------------REFINING-------------------------------------')
            if refKi >= fullhp:
                print('Pressure ' + str(refKi) + ' ki')
            else:
                print('Intensity ' + str(refKi) + ' ki')
            if refKi >= hp:
                print(Color.Red + 'Destruction:' + Color.END + '3 Physical Power/5 ki')
                print('Decreases Full Health')
            else:
                print('Refining:1 Physical Power/5 ki')
            print('-----------------------------ACTIONS--------------------------------------')
            if refKi <= hp:
                print('Begin refining[1]')
                tipe = 1
            else:
                print(Color.Red + 'Begin destruction[1]' + Color.END)
                tipe = 2
            if refKi >= fullhp:
                print(Color.Red + 'Change pressure[2]' + Color.END)
                tipe1 = 1
            else:
                print(Color.END + 'Change intensity[2]' + Color.END)
                tipe1 = 2
            print('Close[e]')
            print('--------------------------------------------------------------------------')
            mov = input()
            print('--------------------------------------------------------------------------')
            if mov == '1':
                if tipe == 1:
                    if ki - refKi >= 0:
                        ki -= refKi
                        hp -= refKi // 10
                        maxki -= refKi // 10
                        physPower += refKi // 10
                        hour += refKi // 10
                        print('Your Physical Power increased on ' + str(refKi // 10))
                        print('Time lost ' + str(hour) + ' Hours')
                        print('Health decreased on ' + str(refKi // 10))
                        print('Max Ki decreased on ' + str(refKi // 5))
                    else:
                        print('Not enough ki')
                elif tipe == 2:
                    if ki - refKi >= 0:
                        print(Color.Red + 'It can kill you')
                        ki -= refKi
                        hp -= refKi // 10
                        fullhp -= refKi // 10
                        physPower += refKi // 10 * 3
                        maxki -= refKi // 5
                        hour += refKi // 10
                        print('Your Physical Power increased on ' + str(refKi // 10 * 3))
                        print('Time lost ' + str(hour) + ' Hours')
                        print('Max Health decreased on ' + str(refKi // 10) + Color.END)
                        print('Max Ki decreased on ' + str(refKi // 10))
                    else:
                        print('Not enough ki')
            elif mov == '2':
                print('Change to:')
                print('Close[e]')
                mov = input()
                if mov != 'e':
                    refKi = int(mov)
                    if tipe1 == 1:
                        print('Intensity changed to ' + str(mov) + ' ki')
                    elif tipe1 == 2:
                        print(Color.Red + 'Pressure changed to ' + str(mov) + ' ki' + Color.END)
            elif mov == 'e':
                break
    elif mov == 'view':
        print('Toxicity: ' + str(toxicity) + ' %')
        print(stash)
        mov = input()
    elif mov == 'g':
        while 1:
            print('1. Gate of ' + physicalGrades[0] + '    ' + physBody[0])
            print('2. Gate of ' + physicalGrades[1] + '   ' + physBody[1])
            print('3. Gate of ' + physicalGrades[2] + '      ' + physBody[2])
            print('4. Gate of ' + physicalGrades[3] + '         ' + physBody[3])
            print('5. Gate of ' + physicalGrades[4] + '         ' + physBody[4])
            print('6. Gate of ' + physicalGrades[5] + '        ' + physBody[5])
            print('7. Gate of ' + physicalGrades[6] + '         ' + physBody[6])
            print('8. Gate of ' + physicalGrades[7] + '        ' + physBody[7])
            print('Close[e]   Action[u]')
            mov = input()
            if mov == 'u':
                while 1:
                    if mov == 'ee':
                        break
                    a = input('Number of Gate: ')
                    a = int(a)
                    b = a - 1
                    print('Name:     Gate of ' + physicalGrades[b])
                    print('Status:   ' + physBody[b])
                    print('Requires: ' + str(phyReq[b]) + ' Physical Power')
                    print('Current:  ' + str(physPower) + ' Physical Power')
                    print('Pill:     ' + str(phyReq[b] // 2) + ' фс')
                    print('Close[e]   Open[u]')
                    mov = input()
                    if mov == 'u':
                        if physPower >= phyReq[b]:
                            while 1:
                                print(inventory)
                                if physPower // 2 > phyReq[b]:
                                    pillName = 'Physical Essence +' + str(phyReq[b] // 2) + ' фс'
                                    inventory.append(pillName)
                                    inventory.append(1)
                                    ie = pillName
                                else:
                                    n = input('Choose pill: ')
                                    if n == 'e':
                                        mov = 'ee'
                                        break
                                    n = int(n)
                                    ie = inventory[n]
                                tipe = type(ie)
                                if tipe == 'фс':
                                    pillEff = eff(ie)
                                    if pillEff >= phyReq[b] // 2:
                                        ind = inventory.index(ie)
                                        junk = inventory.pop(ind + 1)
                                        junk -= 1
                                        if junk == 0:
                                            inventory.remove(ie)
                                        else:
                                            inventory.insert(ind + 1, junk)
                                        hp = 1
                                        hour += 10 * a
                                        fistModifier += pillEff // 50
                                        kickModifier += pillEff // 40
                                        physPower += phyProg[b]
                                        fullhp += phyProg[b] // 10
                                        toxicity = 0
                                        physBody.pop(-1)
                                        physBody.insert(0, 'OPENED')
                                        print(Color.Green + 'Physical Power increased on ' + str(phyProg[b]))
                                        print('Full Health increased on ' + str(phyProg[b] // 10))
                                        print('Fist Power increase on ' + str(pillEff // 50))
                                        print('Kick Power increased on ' + str(pillEff // 40) + Color.END)
                                        print(Color.Red + 'Health decreased to 1')
                                        print('Time left: ' + str(time) + '/' + str(maxtime) + Color.END)
                                        print('You opened: Gate of ' + physicalGrades[b])
                                        if a == 2:
                                            regeneration = 10
                                            print(Color.Green + 'Regeneration increased to 10' + Color.END)
                                            curSkills.append('Primitive Lotus')
                                            print('Now you can use: ' + Color.Red + 'Primitive Lotus' + Color.END)
                                        elif a == 3:
                                            talent += 1
                                            maxtime += 1000
                                            curSkills.append('Reverse Lotus')
                                            print(Color.Yellow + 'Talent increased on 1' + Color.END)
                                            print(Color.Green + 'Life time increased on 1000' + Color.END)
                                            print('Now you can use: ' + Color.Red + 'Reverse Lotus' + Color.END)
                                        elif a == 4:
                                            fistModifier += 40
                                            kickModifier += 60
                                            print(Color.Red + 'Fist Power increased on 40' + Color.END)
                                            print(Color.Red + 'Kick Power increased on 60' + Color.END)
                                        elif a == 5:
                                            talent += 2
                                            curSkills.append('Hundred Fists')
                                            print(Color.Yellow + 'Talent increased on 2' + Color.END)
                                            print('Now you can use: ' + Color.Green + 'Hundred Fists' + Color.END)
                                        elif a == 6:
                                            regeneration = 20
                                            fullhp += 500
                                            print(Color.Green + 'Regeneration increased to 20' + Color.END)
                                            print(Color.Green + 'Full Health increased on 500' + Color.END)
                                        elif a == 7:
                                            regeneration = 50
                                            fullhp += 1000
                                            maxtime += 3000
                                            print(Color.Green + 'Regeneration increased to 50' + Color.END)
                                            print(Color.Green + 'Full Health increased on 1000' + Color.END)
                                            print(Color.Green + 'Life time increased on 3000' + Color.END)
                                        elif a == 8:
                                            fistModifier += 200
                                            kickModifier += 250
                                            talent += 3
                                            maxtime += 6000
                                            print(Color.Red + 'Fist Power increased on 200' + Color.END)
                                            print(Color.Red + 'Kick Power increased on 250')
                                            print(Color.Yellow + 'Talent increased on 3' + Color.END)
                                            print(Color.Green + 'Life time increased on 6000' + Color.END)
                                        a = input()
                                        mov = 'ee'
                                        break
                                    else:
                                        print('Not good pill')
                                else:
                                    print('Incorrect type of pill')
                        else:
                            print('Not enough Physical Power')
                            break
                    if mov == 'e':
                        mov = 'ee'
                        break
            if mov == 'e':
                break
    elif mov == 'gap':
        if h < 41:
            if ki >= culReq[h]:
                print('--------------------------------------------------------------------------')
                if culLvL != 10:
                    print('Your current cultivation ' + cultivationGrades[t] + ' ' + str(culLvL) + ' Stage')
                    print('You can up to  ' + cultivationGrades[t] + ' ' + str(culLvL + 1) + ' Stage')
                    print('Yes[1]  Hold[2]')
                    print('--------------------------------------------------------------------------')
                    if genkai == 3:
                        print('You cant more hold your cultivation')
                        mov = '1'
                    else:
                        mov = str(input())
                    if mov == '1':
                        kiPower += kiPower // kPM
                        culLvL += 1
                        toxicity -= 5
                        maxtime += 100 + tM
                        fullhp += fullhp // 10
                        h += 1
                        print('--------------------------------------------------------------------------')
                        print('You success your gap to ' + cultivationGrades[t] + ' ' + str(culLvL) + ' Stage')
                        print('Next Stage require ' + str(ki) + '/' + str(culReq[h]))
                        genkai = 0
                        mov = str(input())
                    else:
                        genkai += 1
                        mov = str(input())
                elif culLvL == 10:
                    print('Your current cultivation ' + cultivationGrades[t] + ' ' + str(culLvL) + ' Stage')
                    print('You can do a gap to ' + cultivationGrades[t + 1])
                    print('Yes[1]  Hold[2]')
                    print('--------------------------------------------------------------------------')
                    if genkai == 3:
                        print('You cant more hold  your cultivation')
                        mov = '1'
                    else:
                        mov = str(input())
                    print('--------------------------------------------------------------------------')
                    if mov == '1':
                        maxki += mkM
                        toxicity -= 10
                        maxtime += 200 * t
                        mkM += mkM * t
                        kiPower += kiPower // 5
                        t += 1
                        if t == 2:
                            kPM -= 1
                            pPM = 0
                            tM = 100
                        culLvL = 1
                        h += 1
                        fullhp += fullhp // 10
                        if t == 2:
                            maxYear = 100
                        elif t == 3:
                            maxYear = 150
                        elif t == 4:
                            maxYear = 250
                        elif t == 5:
                            maxYear = 500
                        elif t == 6:
                            maxYear = 1000
                        print('--------------------------------------------------------------------------')
                        print('Success gap from ' + str(cultivationGrades[t - 1]) + ' to ' + str(cultivationGrades[t]))
                        genkai = 0
                        mov = str(input())
                    else:
                        genkai += 1
                        mov = str(input())
            else:
                print('--------------------------------------------------------------------------')
                print('To power up you need: ' + str(ki) + '/' + str(culReq[h]) + ' ki')
                print('You need more practice')
                print('--------------------------------------------------------------------------')
                mov = input()
        else:
            print('You have reached the limit of Cultivation')
            mov = input()
    elif mov == 'time':
        print('----------------------------------TIME------------------------------------')
        print('Age: ' + str(year) + ' Years ' + str(month) + ' Months')
        print('Time: ' + str(hour) + ':' + str(minute) + ' O`clock')
        print('Week: ' + str(week))
        print('Day: ' + str(day))
        print('--------------------------------------------------------------------------')
        mov = str(input())
    elif mov == 'cheat':
        gold += 100000
        fullhp = 10000
        hp = fullhp
        maxki += 1000000
        fistLvL = 10
        fistModifier = 50
        kickLvL = 10
        kickModifier = 100
        mov = str(input())
    elif mov == 's':
        loot = ingBlueGrass
        dChance = randrange(0, 10)
        if dChance == 6:
            a = randrange(0, 5)
            if a == 4:
                dChance = randrange(-1, len(medQual))
                loot = medQual[dChance]
                a = randrange(0, 10)
                if a == 1 or a == 5:
                    loot = rareTruffle
                elif a == 3:
                    loot = rareStealShade
        elif dChance == 3 or dChance == 4:
                dChance = randrange(-1, len(lowQual))
                loot = lowQual[dChance]
                dChance = randrange(0, 50)
                if dChance == 2:
                    dChance = randrange(-1, len(hihgQual))
                    loot = hihgQual[dChance]
        else:
            loot = 0
        if loot == 0:
            print('You found nothing')
            hour += 5
            if hp < fullhp - 1:
                hp += regeneration * 5
        else:
            if inventory.count(loot[0]) == 0:
                inventory.append(loot[0])
                ind = inventory.index(loot[0])
                inventory.insert(ind + 1, 1)
                print('You found ' + loot[0])
                hour += 5
                if hp < fullhp:
                    hp += regeneration * 5
            else:
                ind = inventory.index(loot[0])
                junk = inventory.pop(ind + 1)
                junk += 1
                inventory.insert(ind + 1, junk)
                print('You found ' + loot[0])
                hour += 5
                if hp < fullhp - 1:
                    hp += regeneration * 5
        mov = str(input())
    elif mov == 'c':
        while mov != 'e':
            print('--------------------------------CRAFT-------------------------------------')
            print('Choose action:')
            print('--------------------------------------------------------------------------')
            print('Make a powder[1]')
            print('Alchemy[2]')
            print('Refine[3]')
            print('Close[e]')
            print('-------------------------------ACTIONS------------------------------------')
            mov = str(input())
            if mov == '1':
                recipe = []
                pillEff = 0
                while mov != 'i':
                    print('------------------------------POWDER--------------------------------------')
                    print('Select ingredient Type: x%')
                    print('------------------------------PROCESS-------------------------------------')
                    print(inventory)
                    print(recipe)
                    print('-----------------------------EFFICIENCY-----------------------------------')
                    print('Powder efficiency: ' + str(pillEff) + '%')
                    print('-----------------------------SELECTION------------------------------------')
                    mov = input()
                    if mov == 'end':
                        print('------------------------------NAMING---------------------------------------')
                        pillName = input('Name powder: ')
                        pillName = '*' + pillName + ' ' + str(pillEff) + '%'
                        if inventory.count(pillName) == 0:
                            inventory.append(pillName)
                            inventory.append(1)
                        else:
                            ind = inventory.index(pillName)
                            junk = inventory.pop(pillName)
                            junk += 1
                            inventory.insert(ind + 1, junk)
                        print('------------------------------RESULT--------------------------------------')
                        print('You crafted ' + pillName)
                        print('--------------------------------------------------------------------------')
                        break
                    if mov == 'e':
                        mov = 'i'
                        break
                    mov = int(mov)
                    ie = inventory[mov]
                    tipe = type(ie)
                    if tipe != '%':
                        print('Incorrect type')
                        break
                    junk = inventory.pop(mov + 1)
                    junk -= 1
                    if junk == 0:
                        inventory.remove(ie)
                    else:
                        inventory.insert(mov + 1, junk)
                    if recipe.count(ie) == 0:
                        recipe.append(ie)
                        recipe.append(1)
                    else:
                        ind = recipe.index(ie)
                        junk = recipe.pop(ind + 1)
                        junk += 1
                        recipe.insert(ind + 1, junk)
                    ef = eff(ie)
                    pillEff += ef
            elif mov == '2':
                recipe = []
                pillEff = 0
                pillType = 'ки'
                hP = 0
                kI = 0
                fS = 0
                dG = 0
                kiUsage = 0
                while mov != 'i':
                    print('--------------------------------PILL--------------------------------------')
                    print('Select ingredient Type: +фс, +ки, +хп, +ун')
                    print('------------------------------PROCESS-------------------------------------')
                    print(inventory)
                    print(recipe)
                    print('-----------------------------EFFICIENCY-----------------------------------')
                    print('Pill efficiency: ' + str(pillEff))
                    print('Your ki: ' + str(ki) + '/' + str(maxki))
                    print('Ki usage: ' + str(kiUsage))
                    print('-----------------------------SELECTION------------------------------------')
                    mov = input()
                    if mov == 'end':
                        if kiUsage == 0:
                            break
                        print('------------------------------NAMING---------------------------------------')
                        pillName = input('Name pill: ')
                        value = [kI, hP, fS, dG]
                        pillType = value.index(max(value))
                        s1 = max(value)
                        value.remove(s1)
                        s2 = value[0] + value[1] + value[2]
                        if pillType == 0:
                            pillType = 'ки'
                        elif pillType == 1:
                            pillType = 'хп'
                        elif pillType == 2:
                            pillType = 'фс'
                        elif pillType == 3:
                            pillType = 'ун'
                        if s1 > s2:
                            pillT = pillType
                        else:
                            pillT = 'ун'
                        pillEff = dG + hP + kI + fS
                        ki -= kiUsage
                        pillName = '*`' + str(pillName) + ' +' + str(pillEff) + ' ' + str(pillT)
                        if inventory.count(pillName) == 0:
                            inventory.append(pillName)
                            inventory.append(1)
                        else:
                            ind = inventory.index(pillName)
                            junk = inventory.pop(pillName)
                            junk += 1
                            inventory.insert(ind + 1, junk)
                        print('------------------------------RESULT--------------------------------------')
                        print('You crafted: ' + pillName)
                        print('You used: ' + str(kiUsage) + ' ki')
                        print('--------------------------------------------------------------------------')
                        hour += pillEff
                        break
                    if mov == 'e':
                        mov = 'i'
                        break
                    mov = int(mov)
                    ie = inventory[mov]
                    tipe = type(ie)
                    pillType = useful(ie)
                    if pillType == '*':
                        print('Can not be refined')
                        break
                    pillType = tipe
                    if tipe == '%':
                        print('Incorrect type')
                        break
                    coef = 1
                    if tipe == 'хп':
                        coef = 3
                    elif tipe == 'ки':
                        coef = 2
                    elif tipe == 'фс':
                        coef = 5
                    else:
                        coef = 1
                    junk = inventory.pop(mov + 1)
                    junk -= 1
                    if junk == 0:
                        inventory.remove(ie)
                    else:
                        inventory.insert(mov + 1, junk)
                    if recipe.count(ie) == 0:
                        recipe.append(ie)
                        recipe.append(1)
                    else:
                        ind = recipe.index(ie)
                        junk = recipe.pop(ind + 1)
                        junk += 1
                        recipe.insert(ind + 1, junk)
                    ef = eff(ie)
                    kiUsage += ef * coef
                    pillEff += ef
                    if tipe == 'хп':
                        hP += ef
                    elif tipe == 'фс':
                        fS += ef
                    elif tipe == 'ки':
                        kI += ef
                    elif tipe == 'ун':
                        dG += ef
                    value = [kI, fS, hP]
                    s1 = max(value)
                    value.remove(s1)
                    s2 = min(value)
                    value.remove(s2)
                    s3 = value[0]
                    s2 = s2 + s3
                    if s1 + 1 > s2:
                        dG += s2
                    else:
                        dG += s1
            elif mov == '3':
                mainIng = ''
                recipe = []
                pillEff = 0
                kiUsage = 0
                succesChance = 0
                while mov != 'i':
                    print('----------------------------REFINING--------------------------------------')
                    print(inventory)
                    print('----------------------------SELECTION-------------------------------------')
                    mov = input('Choose item to Refine:')
                    if mov == 'e':
                        mov = 'i'
                        break
                    mov = int(mov)
                    ri = inventory[mov]
                    tipe = useful(ri)
                    if tipe != '*`':
                        print('Incorrect type')
                        break
                    ind = inventory.index(ri)
                    junk = inventory.pop(ind + 1)
                    junk -= 1
                    if junk == 0:
                        inventory.pop(ind)
                    else:
                        inventory.insert(ind + 1, junk)
                    tipe = type(ri)
                    if tipe == 'тт':
                        while mov != 'e':
                            if mov == 'o':
                                mov = 'i'
                                break
                            print('----------------------------INGREDIENTS-----------------------------------')
                            print('Selected item: ' + str(ri))
                            print('--------------------------CHARACTERISTICS---------------------------------')
                            print('Require: ' + str(pillEff) + '/' + '2000 Efficiency')
                            print('Success chance: ' + str(succesChance) + '%')
                            print('Your ki: ' + str(ki) + '/' + str(maxki))
                            print('Ki usage: ' + str(kiUsage) + ' ki')
                            print('-----------------------------INVENTORY------------------------------------')
                            print(inventory)
                            print('-----------------------------SELECTION------------------------------------')
                            mov = input('Choose item:')
                            print('--------------------------------------------------------------------------')
                            if mov == 'e':
                                mov = 'i'
                                inventory.append(ri)
                                inventory.append(1)
                                break
                            ind = int(mov)
                            ci = inventory[ind]
                            ef = eff(ci)
                            tipe = type(ci)
                            coef = 1
                            if tipe == 'хп':
                                coef = 3
                            elif tipe == 'ки':
                                coef = 2
                            elif tipe == 'фс':
                                coef = 5
                            else:
                                coef = 1
                            kiUsage += ef * coef
                            pillEff += ef
                            ind = inventory.index(ci)
                            junk = inventory.pop(ind + 1)
                            junk -= 1
                            if junk == 0:
                                inventory.pop(ind)
                            else:
                                inventory.insert(ind + 1, junk)
                            if pillEff == 2000:
                                print('Now add catalizator')
                                while mov != 'p':
                                    print('-----------------------------CATALIZATORS---------------------------------')
                                    print('Selected item: ' + str(ri))
                                    print('----------------------------CHARACTERISTICS-------------------------------')
                                    print('Require: ' + str(pillEff) + '/' + '2000 Efficiency')
                                    print('Success chance: ' + str(succesChance) + '%')
                                    print('Your ki: ' + str(ki) + '/' + str(maxki))
                                    print('Ki usage: ' + str(kiUsage) + ' ki')
                                    print('------------------------------INVENTORY-----------------------------------')
                                    print(inventory)
                                    print('------------------------------SELECTION-----------------------------------')
                                    mov = input('Choose item:')
                                    print('--------------------------------------------------------------------------')
                                    if mov == 'e' or mov == 'end' or succesChance == 100:
                                        o1 = []
                                        o2 = []
                                        o3 = []
                                        chance = 0
                                        chance2 = 0
                                        for i in range(101):
                                            unsuccesRate = randrange(0, 101)
                                            o1.append(unsuccesRate)
                                            suc = randrange(0, succesChance)
                                            o2.append(suc)
                                            unsuc = randrange(succesChance, 101)
                                            o3.append(unsuc)
                                        for i in o2:
                                            for ii in o1:
                                                if i == ii:
                                                    chance += 1
                                        for i in o3:
                                            for ii in o1:
                                                if i == ii:
                                                    chance2 += 1
                                        if chance > chance2:
                                            ef = eff(ri)
                                            ef += 1
                                            pillName = '*`' + 'Refined Matter +' + str(ef) + ' тт'
                                            ki -= kiUsage
                                            print('You Refined: ' + str(ri) + ' => ' + str(pillName))
                                            if inventory.count(pillName) == 0:
                                                inventory.append(pillName)
                                                inventory.append(1)
                                            else:
                                                ind = inventory.index(pillName)
                                                junk = inventory.pop(ind + 1)
                                                junk += 1
                                                inventory.insert(ind + 1)
                                        else:
                                            print('Unsuccess Refining')
                                        print(
                                            '--------------------------------------------------------------------------')

                                        mov = 'o'
                                        break
                                    ind = int(mov)
                                    ci = inventory[ind]
                                    tipe = type(ci)
                                    if tipe != '%':
                                        print('Incorrect type')
                                        break
                                    ef = eff(ci)
                                    kiUsage += ef * 50
                                    succesChance += ef
                                    junk = inventory.pop(ind + 1)
                                    junk -= 1
                                    if junk == 0:
                                        inventory.pop(ind)
                                    else:
                                        inventory.insert(ind + 1, junk)
            elif mov == 'e':
                mov = 'e'
                break
    elif mov == 'ss':
        while mov != 'e':
            print('--------------------------------SKILLS------------------------------------')
            grade = skills[4]
            damage = 0
            mod = 0
            skillElem = skills[6]
            if skillElem == mainElem:
                mod = mainElemPow // 100 + 1
            elif mainElem == 'Neutral':
                mod = 1
            if skills[1] == 'atk':
                damage = int((kiPower // 100 * skills[3]) * mod)
                if skills[0] == 'Pressure Point' and damage == 300:
                    skills = PressurePoint1
            elif skills[1] == 'buff':
                damage = int(kiPower // 500 * skills[3] * mod)
            elif skills[1] == 'phy':
                damage = int(physPower// 100 * skills[3] * mod)
            elif skills[1] == 'heal':
                damage = int(kiPower // 100 * skills[3] * mod)
            if damage > skills[5]:
                damage = skills[5]
            print('Current skill: ' + grade + str(skills[0]) + Color.END)
            print('---------------------------CHARACTERISTICS--------------------------------')
            print('Type: ' + str(skills[1]))
            print('Cost: ' + str(skills[2]))
            print('Power: ' + str(damage))
            print('Element: ' + str(skillElem))
            print('-------------------------------ACTIONS------------------------------------')
            print('Close[e]   Change[u]')
            print('--------------------------------------------------------------------------')
            mov = input()
            print('--------------------------------------------------------------------------')
            if mov == 'u':
                print('Select skill which you want change')
                print('--------------------------------------------------------------------------')
                print(curSkills)
                print('--------------------------------------------------------------------------')
                mov = input()
                if mov == 'e':
                    break
                elif mov == '':
                    mov = 0
                print('--------------------------------------------------------------------------')
                n = int(mov)
                print(n)
                dlina = int(len(curSkills))
                if n <= dlina:
                    sSkill = curSkills[n]
                    for i in allSkills:
                        sName = i[0]
                        if sName == sSkill:
                            skills = i
                        else:
                            pass
                    print('Skill changed to: ' + skills[4] + skills[0] + Color.END)
                else:
                    print('Choose another number')
            else:
                pass
    elif mov == 'd':
        minute += 10
        y += 1
        if y > 5:
            y = -1
        stance = y, x
        ind = l.index(1)
        l.remove(1)
        l.insert(ind, 0)
        l = movement(stance, wMap, l)
        print(l)
        mov = input()
    else:
        mov = str(input())
    chronology = year, month, week, day, hour, minute
    clock(chronology)

    ingCargo = ['red grass +10 ки', 'black flower +15 ки', 'blue grass +5 ки',
                'earth tongue +30 ки', 'sky trevor +10 фс', 'bloody grass +5 хп', 'Nirvana Fruit +70 фс',
                'Clock-Clock +1 вс', 'Trevor +500 ун']
    dChance = randrange(-1, 6)
    if week == 2:
        quantity = 0
        ci = ingCargo[dChance]
        dChance = randrange(0, 4)
        if dChance == 1:
            dChance = randrange(0, 5)
            if dChance == 2:
                dChance = randrange(0, 6)
                if dChance == 3:
                    quantity = 4
            else:
                quantity = 2
        else:
            quantity = 1
        if stash.count(ci) == 0:
            stash.append(ci)
            stash.append(quantity)
        else:
            ind = stash.index(ci)
            junk = stash.pop(ind + 1)
            junk += quantity
            stash.insert(ind + 1, junk)
    else:
        pass

print('Your time is end')

name = 'Lurker'
mhp = 600
mfull = 600
matk = 60
lootname = 'hard silk +30 хп'
mloot = lootname
mobLurker = [name, mhp, matk, mfull, mloot]

name = 'Iron skin Rhino'
mhp = 1000
mfull = 1000
matk = 40
lootname = 'iron skin +20 фс'
mloot = lootname
mobISRhino = [name, mhp, matk, mfull, mloot]

name = 'Ghoul'
mhp = 500
mfull = 500
matk = 50
lootname = 'Rotten Flesh +50 ун'
mloot = lootname
mobGhoul = [name, mhp, matk, mfull, mloot]


mobsLoc4 = [mobISRhino, mobLurker, mobGhoul]

name = 'Big Foot'
mhp = 1000
mfull = 1000
matk = 60
lootname = 'fat +50 хп'
mloot = lootname
mobBigFoot = [name, mhp, matk, mfull, mloot]

name = 'Black Miasm'
mhp = 1500
mfull = 1500
matk = 90
lootname = 'innocent matter +150 ки'
mloot = lootname
mobBlackMiasm = [name, mhp, matk, mfull, mloot]

name = 'Boiler'
mhp = 800
mfull = 800
matk = 60
lootname = 'hot water +70 ун'
mloot = lootname
mobBoiler = [name, mhp, matk, mfull, mloot]

name = 'Gnoll'
mhp = 800
mfull = 800
matk = 40
lootname = 'gnoll tooth +10 фс'
mloot = lootname
mobGnoll = [name, mhp, matk, mfull, mloot]

mobsLoc5 = [mobBigFoot, mobBlackMiasm, mobGnoll, mobBoiler]

name = 'Dragon'
mhp = 10000
mfull = 10000
matk = 150
lootname = 'sulfur 25%'
mloot = lootname
mobDragon = [name, mhp, matk, mfull, mloot]

name = 'Rat'
mhp = 80
mfull = 80
matk = 15
lootname = 'tail 1%'
mloot = lootname
mobRat = [name, mhp, matk, mfull, mloot]


class Enemy:

    name = 'Skelelton'
    health = 1500, 1500
    atk = 100
    drop = 'bone +5 фс'
    skillname = 'Blow'
    allPar = [name, health, atk, skillname, drop]

    def __init__(self, name, health, atk):
        self.atk = atk
        self.name = name
        self.hp = health

    def ussual(self, allPar, char):
        hah = allPar[2]
        if allPar[2] - char[7] > 0:
            char[3] -= allPar[2] - char[7]
            hah -= char[7]
        else:
            hah = 0
        print(allPar[0] + str(' Dealt: ' + str(hah) + ' Damage'))

    def special(self, allPar, char):
        allPar[2] += allPar[2]
        hah = allPar[2]
        if hah - char[7] > 0:
            hah -= char[7]
        else:
            hah = 0
        char[3] -= hah
        print(allPar[0] + ' used ' + allPar[3] + str(' dealt ' + str(hah) + ' damage'))
        allPar[2] = self.atk

class Wolf(Enemy):

    name = 'Dire Wolf'
    health = 800, 800
    atk = 80
    drop = 'fang 10%'
    skillname = 'Howl'
    allPar = [name, health, atk, skillname, drop]

    def special(self, allPar, char):
        if char[1] > 0:
            char[1] -= allPar[2] // 10
            print(self.name + ' used ' + allPar[3] + str(' your Power decreased ' + str(allPar[2] // 10)))
        else:
            print(self.name + ' used ' + allPar[3] + str(' your Power decreased ' + str(0)))
            char[1] = 0
        return char[1]

class BlackSabbath(Enemy):

    name = 'Black Sabbath'
    health = 3000, 3000
    atk = 150
    drop = 'dark essence +500 ки'
    skillname = 'Shadows'
    allPar = [name, health, atk, skillname, drop]

    def special(self, allPar, char):
        hah = allPar[2]
        if hah - char[7] > 0:
            hah -= char[7]
        else:
            hah = 0
        char[3] -= hah
        char[0] -= hah * 4
        print(self.name + ' used ' + allPar[3] + str(' Dealt: ' + str(hah) + ' Damage'))
        print('Your ki decreased on ' + str(hah * 4))

class Hound(Enemy):

    name = 'Hound'
    health = 500, 500
    atk = 50
    drop = 'fur +10 хп'
    skillname = 'Claws Slash'
    allPar = [name, health, atk, skillname, drop]

    def special(self, allPar, char):
        char[3] -= int(allPar[2] * 1.5)
        char[3] += char[7]
        print(self.name + ' used ' + allPar[3] + str(' Dealt: ' + str(int(allPar[2] * 1.5 - char[7])) + ' Damage'))

mobname = 'Zombie'
mobhp = 500
mobfull = 500
mobatk = 40
moblootname = 'brains'
mobloot = moblootname
mobdrop1 = 1
mobdrop2 = 2
mobdrop3 = 3
mobdrop = mobdrop1, mobdrop2, mobdrop3
mobdroprange1 = 0
mobdroprange2 = 10
mobdroprange = mobdroprange1, mobdroprange2
mobZombie = [mobname, mobhp, mobatk, mobfull, mobloot, mobdrop1, mobdrop2, mobdrop3, mobdroprange1, mobdroprange2]

mobname = 'Slime'
mobhp = 100
mobfull = 100
mobatk = 5
cost = 1
moblootname = 'slime'
slime = cost * 5
mobloot = moblootname
mobdrop1 = 1
mobdrop2 = 2
mobdrop3 = 3
mobdrop = mobdrop1, mobdrop2, mobdrop3
mobdroprange1 = 0
mobdroprange2 = 5
mobdroprange = mobdroprange1, mobdroprange2
mobSlime = [mobname, mobhp, mobatk, mobfull, mobloot, mobdrop1, mobdrop2, mobdrop3, mobdroprange1, mobdroprange2]

mobname = 'Lizard'
mobhp = 200
mobfull = 200
mobatk = 15
cost = 1
moblootname = 'lizard meat'
slime = cost * 5
mobloot = moblootname
mobdrop1 = 1
mobdrop2 = 2
mobdrop3 = 3
mobdrop = mobdrop1, mobdrop2, mobdrop3
mobdroprange1 = 0
mobdroprange2 = 5
mobdroprange = mobdroprange1, mobdroprange2
mobLizard = [mobname, mobhp, mobatk, mobfull, mobloot, mobdrop1, mobdrop2, mobdrop3, mobdroprange1, mobdroprange2]

mobname = 'Goblin'
mobhp = 150
mobfull = 150
mobatk = 10
moblootname = 'venom'
mobloot = moblootname
mobdrop1 = 1
mobdrop2 = 2
mobdrop3 = 3
mobdrop = mobdrop1, mobdrop2, mobdrop3
mobdroprange1 = 0
mobdroprange2 = 5
mobdroprange = mobdroprange1, mobdroprange2
mobGoblin = [mobname, mobhp, mobatk, mobfull, mobloot, mobdrop1, mobdrop2, mobdrop3, mobdroprange1, mobdroprange2]

mobname = 'Emu'
mobhp = 300
mobfull = 300
mobatk = 20
moblootname = 'feather'
mobloot = moblootname
mobdrop1 = 1
mobdrop2 = 2
mobdrop3 = 3
mobdrop = mobdrop1, mobdrop2, mobdrop3
mobdroprange1 = 0
mobdroprange2 = 7
mobdroprange = mobdroprange1, mobdroprange2
mobEmu = [mobname, mobhp, mobatk, mobfull, mobloot, mobdrop1, mobdrop2, mobdrop3, mobdroprange1, mobdroprange2]

mobname = 'Korin'
mobhp = 4000
mobfull = 4000
fullki = 500
kki = 500
tecName = 'Stone Skin'
tecReq = 100
tecEff = 'Deffense'
tecPow = 100
mobatk = 70
moblootname = 'blessed water'
mobloot = moblootname
mobdrop1 = 1
mobdrop2 = 2
mobdrop3 = 3
mobdrop = mobdrop1, mobdrop2, mobdrop3
mobdroprange1 = 0
mobdroprange2 = 15
mobdroprange = mobdroprange1, mobdroprange2
bossKorin = [mobname, mobhp, mobatk, mobfull, mobloot, mobdrop1, mobdrop2, mobdrop3, mobdroprange1, mobdroprange2, fullki, kki, tecName, tecReq, tecEff, tecPow]
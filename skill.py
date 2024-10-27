from color import Color

PressurePoint = ['Pressure Point ', 'atk', 10, 5, Color.White, 300, 'Neutral']
PressurePoint1 = ['Pressure Point', 'atk', 50, 15, Color.Red, 550, 'Neutral']
FirePressure = ['Fire Pressure', 'atk', 30, 10, Color.Red, 500, 'Fire']
FireBreathe = ['Fire Breathe', 'atk', 250, 20, Color.Red, 4000, 'Fire']
HawkDiving = ['Hawk Diving', 'atk', 900, 50, Color.Red, 5000, 'Neutral']
SteelFlesh = ['Steal Flesh', 'buff', 50, 0.2, Color.Red, 1, 'Earth']
WindBlades = ['Wind Blades', 'atk', 50, 20, Color.Green, 850, 'Wind']
Singularity = ['Singularity', 'atk', 500, 50, Color.Yellow, 5000, 'Neutral']
HeavyBlow = ['Heavy Blow', 'phy', 25, 50, Color.Red, 1500, 'Neutral']
PrimitiveLotus = ['Primitive Lotus', 'phy', 40, 75, Color.Red, 2000, 'Neutral']
ReverseLotus = ['Reverse Lotus', 'phy', 60, 100, Color.Red, 3000, 'Neutral']
HundredFists = ['Hundred Fists', 'phy', 100, 150, Color.Green, 5000, 'Neutral']
Reveal = ['Reveal', 'heal', 50, 1, Color.White, 100, 'Water']
FireLaws = ['Fire Laws', 'prog', 5, 1, Color.White, 30, 'Fire']

allSkills = [PressurePoint, FirePressure, SteelFlesh, WindBlades, Singularity, HeavyBlow,
             PrimitiveLotus, ReverseLotus, HundredFists, HawkDiving, FireBreathe, Reveal]

culSkill = FireLaws

class Skill:

    name = 'Blow'
    power = 40
    cost = 10
    grade = Color.END
    allPar = [name, power, cost, grade]

    def __init__(self, char):
        self.ki = char[0]
        self.ehp = char[1]
        self.eatk = char[2]
        self.hp = char[3]

    def tecname(self, allPar):
        print('You use ' + allPar[3] + str(allPar[0]) + Color.END)
        print('You deal ' + str(allPar[1]) + ' damage')
        print('You spent ' + str(allPar[2]) + ' ki')

    def requiremnt(self, allPar, char):
        char[0] -= allPar[2]
        return char

    def action(self, char, allPar):
        char[3] -= char[2]
        char[1] -= allPar[1]
        return char

    def upgrade(self, allPar, name):
        allPar[0] += '*'
        allPar[1] += allPar[1] // 10
        allPar[2] += allPar[2] // 10


class Lightning(Skill):

    name = 'Lightning'
    power = 750
    cost = 250
    grade = Color.Red
    allPar = name, power, cost, grade

    def requiremnt(self, allPar, char):
        char[3] -= allPar[2] // 10
        char[0] -= allPar[2]

    def upgrade(self, allPar, name):
        Lightning.name = 'Thunder'
        return Lightning.name

class Drain(Skill):
    name = 'Drain'
    power = 0
    cost = 1
    grade = Color.Yellow
    allPar = [name, power, cost, grade]


    def requiremnt(self, allPar, char):
        allPar[2] = char[0]
        char[0] -= char[0]
        return allPar[2]

    def action(self, char, allPar):
        allPar[1] = allPar[2] // 2
        char[1] -= allPar[1]
        char[3] += allPar[1] // 10
        return allPar[1]

def eff(ing):
    emp = []
    eff = ''
    for i in ing:
        if '1234567890.'.find(i) != -1:
            emp.append(i)
            junk = emp.pop(0)
            eff += junk
            fif = int(eff)
    return fif

def type(ing):
    emp = []
    prop = ''
    for i in ing:
        if 'кихпттфс%вун'.find(i) != -1:
            emp.append(i)
            junk = emp.pop(0)
            prop += junk
    return prop

def useful(ing):
    emp = []
    prop = ''
    for i in ing:
        if '*`'.find(i) != -1:
            emp.append(i)
            junk = emp.pop(0)
            prop += junk
    return prop

def location(map, g, legend):
    l = 0
    for i in map:
        l += 1
        c = 0
        for j in i:
            c += 1
            t = j
            leg = [2, '@']
            for w in leg:
                if t == w:
                    l -= 1
                    c -= 1
                    g = l, c
                    if legend.count(g) == 0:
                        legend.append(g)
                    else:
                        pass
    return legend

def geoloc(stance, legend, map):
    g = stance
    y = g[0]
    x = g[1]
    a = -1
    b = -1
    m = legend
    for i in m:
        if g == i:
            w = map
            for k in w:
                a += 1
                if a == y:
                    for c in k:
                        b += 1
                        if b == x:

                            n = k[b]
                            if n == '2':
                                print('Enter')

def movement(stance, map, h):
    global loc1, loc2, loc3, loc4, loc5, loc6, l
    y = stance[0]
    x = stance[1]
    loc = map[y]
    loc.pop(x)
    loc.insert(x, 1)
    h = map[y]
    return h


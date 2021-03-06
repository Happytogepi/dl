fac_ele = {
    'altar': (0.09, 0.09),
    'slime': 0.04,
    'flame': {
        'tree': 0.16,
        'arctos': 0.085
    },
    'water': {
        'yuletree': 0.085,
        'dragonata': 0.07
    },
    'wind': {
        'shrine': 0.07
    },
    'light': {
        'retreat': 0.085,
        'circus': 0.07
    },
    'shadow': {
        'library': 0.07
    }
}
fac_wt = {
    'dojo': (0.15, 0.15),
    'dagger': 0.05,
    'bow': 0.05
}
fac_faf = 0.115

def c(ele,wt):
    r = 0
    r += sum(fac_ele['altar']) + fac_ele['slime']
    r += sum(fac_ele[ele].values())
    r += sum(fac_wt['dojo'])
    if wt in fac_wt:
        r += fac_wt[wt]
    return 1+r

def d(ele):
    return 1 + fac_faf


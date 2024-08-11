"""Pokemon stat calculator, WIP
Input your pokemons base stat, iv, ev in that stat,
nature multiplier (1.1 for boost, 1.0 for neutral, 0.9 for neg)
and level to get their stat. rounds down like in the games.
"""
import math

class Nature:
    def __init__(self, name, boon, bane):
        self.name = name
        self.boon = boon
        self.bane = bane

class Bases:
    def __init__(self, hp, atk, defence, spatk, spdef, spe):
        self.hp = hp
        self.atk = atk
        self.defence = defence
        self.spatk = spatk
        self.spdef = spdef
        self.spe = spe

class Pokemon:
    def __init__(self, bases, stats, nature, level):
        self.bases = bases
        self.stats = stats
        self.nature = nature
        self.level = level


def stat_formula(stat_name, base, iv, ev, level, nature):
    gen = (((2*base + iv + (ev/4))*level)/100)
    if stat_name=="hp":
        stat = gen+level+10
    else:
        stat = (gen+5)*nature
    return math.floor(stat)

stat_name = "atk"
base = 55
iv = 0
ev = 0
level = 50
nature = 0.9
stat = stat_formula(stat_name, base, iv, ev, level, nature)
print(f'the level {level} pokemon with base {base} value in {stat_name} '
      f'with iv of {iv} and {ev} evs with a nature multiplying the '
      f'stat by {nature} has the stat of {stat}')
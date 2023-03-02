from land import info_alt, info_land
import random

def velg_tilfeldig_land():
    land = random.choice(info_alt())
    return land

def hovedstad(land):
    h = land["capital"][0]
    return h


"""
t = velg_tilfeldig_land()
print(t["name"]["common"])
print(hovedstad(t))
"""


from random import choice

d = ['Heads', 'Tails']

def flip_coin():
    return choice(d)

print(flip_coin())
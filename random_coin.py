import random

d = ['Heads', 'Tails']

def flip_coin():
    return random.choice(d)

print(flip_coin())
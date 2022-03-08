# Random is a Python library used to generate random numbers as a float
# go to https://docs.python.org/3/library/random.html for more info
import random 

# tdqm is a library that's used to produce a progress bar where you can visually see the progress of your code running - go to https://tqdm.github.io/ for more info
from tqdm import trange, tqdm

#randint is a function within the random library used to generate a random integers
from random import randint

numlist = []
for i in range(10):
    numlist.append(random.randint(1, 1000))
    print(numlist)


'''
note: If you receive an ImportError, NameError or message stating there is no module named tqdm, run the following in your terminal:
    python -m pip install tqdm
you may also have to run:
    python -c 'import tqdm'
'''


# for-loop
# This will perform a coin toss 1000 times, keep count of each heads or tails and display the results
heads = 0
tails = 0

for i in tqdm(range(1000), desc='Coin Flip Progress'):
    toss = randint(0, 1)
    if toss == 0:
        heads += 1
    else:
        tails += 1
print(heads, tails)
print(f"The difference between heads and tails is " + str(abs(heads - tails)) + " coin tosses.")

# Nested for-loop
# This will run the coin toss loop x number of times based on the value of num_games
num_games = 3

# The Outer Loop will display a bar that tracks the number of games that have completed.
for game in tqdm(range(num_games), desc='Outer Loop Progress'):
    heads = 0
    tails = 0
# The Inner Loop will track progress of the current game
    for j in trange((1000000), desc=f'Game {game+1} Inner Loop Progress'):
        toss = randint(0, 1)
        if toss == 0:
            heads += 1
        else:
            tails += 1
print(f'Heads: {heads}, Tails: {tails}')
print(f"The difference between heads and tails is " + str(abs(heads - tails)) + " coin tosses.")
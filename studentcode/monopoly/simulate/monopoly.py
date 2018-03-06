import random

def throw():
    #return random.randint(2, 12)
    return random.randint(1, 6) + random.randint(1, 6)

n = 1000
n_throws = 0
for i in range(n):
    values = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120,\
    		  0, 140, 120, 140, 160, 200, 180, 0, 180, 200,\
    		  0, 220, 0, 220, 240, 200, 260, 260, 150, 280,\
    		  0, 300, 300, 0, 320, 200, 0, 380, 0, 400]

    location = 0

    # while there is anything left to buy
    while any(values):

        # move
        location += throw()
        location %= len(values)

        # buy tile
        values[location] = 0

        n_throws += 1

print("The answer is: ")
print(n_throws / n)
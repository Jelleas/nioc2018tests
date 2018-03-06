change_owed = int(float(input("how much change is owed? ")) * 100)

n_coins = 0

while change_owed >= 25:
    change_owed -= 25
    n_coins += 1

while change_owed >= 10:
    change_owed -= 10
    n_coins += 1

while change_owed >= 5:
    change_owed -= 5
    n_coins += 1

while change_owed >= 1:
    change_owed -= 1
    n_coins += 1

print("minimum number of coins needed: {}".format(n_coins))
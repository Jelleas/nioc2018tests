change_owed = float(input("how much change is owed? "))

n_coins = 0

while change_owed >= 0.25:
    change_owed -= 0.25
    n_coins += 1

while change_owed >= 0.10:
    change_owed -= 0.10
    n_coins += 1

while change_owed >= 0.05:
    change_owed -= 0.05
    n_coins += 1

while change_owed >= 0.01:
    change_owed -= 0.01
    n_coins += 1

print("minimum number of coins needed: {}".format(n_coins))
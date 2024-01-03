#1
a_die = [1, 2, 3, 4, 5, 6]
b_die = [1, 2, 3, 4, 5, 6]
tot = 0
for i in a_die:
    for j in b_die:
        tot += 1
        print(f"Die A: {i}, Die B: {j}, Sum: {i + j}")
print(f"Total Combinations: {tot}")

# optimal path
'''
die_a = [1, 2, 3, 4, 5, 6]
die_b = [1, 2, 3, 4, 5, 6]

for i in die_a:
    for j in die_b:
        print(f"Die A: {i}, Die B: {j}, Sum: {i + j}")
total_combinations = len(die_a) * len(die_b)
print(f"\nTotal Combinations: {total_combinations}")
'''
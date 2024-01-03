# 3. Calculate the Probability of all Possible Sums occurring among the number of combinations from (2).
die_faces = [1, 2, 3, 4, 5, 6]
sum_count = [0] * 11
for die_a in die_faces:
    for die_b in die_faces:
        tot_sum = die_a + die_b
        sum_count[tot_sum - 2] += 1
tot = len(die_faces) * len(die_faces)
print("Probability Distribution: ")
for i, count in enumerate(sum_count, start=2):
    probability = count / tot
    print(f'P(Sum = {i}) = {count}/{tot} = {probability:.4f}')

# optimal path
'''
die_faces = [1, 2, 3, 4, 5, 6]
tot = len(die_faces) ** 2
sum_count = [0] * 11

for die_a in die_faces:
    for die_b in die_faces:
        total_sum = die_a + die_b
        sum_count[total_sum - 2] += 1

print("\nProbability Distribution: ")
for i, count in enumerate(sum_count, start=2):
    probability = count / tot
    print(f'P(Sum = {i}) = {count}/{tot} = {probability:.4f}')
'''
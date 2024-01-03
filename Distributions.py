#2
die = [1, 2, 3, 4, 5, 6]
mat = [[0] * 6 for _ in range(6)]
for i in range(6):
    for j in range(6):
        mat[i][j] = die[i] + die[j]
print("Distribution of Combinations:")
for row in mat:
    print(row)

# optimal path
'''
die1 = [1, 2, 3, 4, 5, 6]
mat1 = [[i + j for j in die1] for i in die1]
print("\nDistribution of Combinations:")
for row in mat1:
    print(row)

'''
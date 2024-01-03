Die_A = [1, 2, 3, 4, 5, 6]
Die_B = Die_A
faces_a = [face for face in Die_A if face > 4]
faces_b = [face for face in Die_B if face > 6]
new_die_a = [face if face <= 4 else face - 2 for face in Die_A]
new_die_b = [face if face <= 6 else face - 2 for face in Die_B]

print("Original Die_A:", Die_A)
print("Original Die_B:", Die_B)
print("New Die_A:", new_die_a)
print("New Die_B:", new_die_b)
prob = {i: 0 for i in range(2, 13)}
for face_a in new_die_a:
    for face_b in new_die_b:
        prob[face_a + face_b] += 1

tot = len(new_die_a) * len(new_die_b)
probabilities = {i: count / tot for i, count in prob.items()}
print("\nProbabilities for each sum:")
for i in range(2, 13):
    print(f"P(Sum = {i}) = {probabilities[i]:.4f}")
# Doomed_Dice_Challenge

README
The project involves an analysis of the outcomes when two six-faced dice are rolled simultaneously. It has sub divisions of question.
They are

1.How many total combinations are possible when the dice are rolled?
2.Calculate and display the distribution of all possible combinations that can be obtained when rolling both Die A and Die B together.
3.Calculate the Probability of all Possible Sums occurring among the number of combinations from 2.
4.There is also another part in this question. Let us consider you are playing with the dice and the spots on dice disappeared. The dice need to have the spots reattached for that we have some conditions. They are Die A cannot have more than 4 Spots on a face. Die A may have multiple faces with the same number of spots. Die B can have as many spots on a face as necessary i.e. even more than 6 But in order to get the spots, the probability of obtaining the Sums must remain the same.

SOLUTION

1.The approach for the first question is based on the logic. The logic is that each die has six faces. When you roll both dice together, there are 6 * 6 = 36 possible combinations. The code just goes through all these possibilities and keeps track of how many times each combination occurs.

2.To display the distribution of all possible outcomes it generates a 6x6 matrix representing the sum of all possible combinations of rolling two six-sided dice. It initializes a list ‘die’ with the faces of a die, and then uses nested loops to iterate through each combination, calculating the sum of the corresponding faces and storing the results in the matrix. Finally, it prints the matrix, displaying the distribution of sums for all possible combinations of the two dice.

3.The solution involves in calculating the probability distribution of the sum of two six-sided dice rolls. It initializes a list ‘die_faces’ with the faces of a die and a list ‘sum_count’ to store the count of each possible sum. Using nested loops, it iterates through all combinations of rolling two dice, calculates the sum, and updates the corresponding count in the ‘sum_count’ list. After counting all combinations, it calculates the total number of outcomes and prints the probability distribution for each possible sum, using the formula P(Sum = i) = count/tot. The code provides a concise way to analyse the likelihood of different sums when rolling two dice.


4.The code initiates with the definition of two six-sided dice, Die_A and Die_B. It adjusts faces exceeding 4 on Die_A and faces exceeding 6 on Die_B by subtracting 2 from them. The original and modified dice are printed. Following this, the code computes probabilities for each possible sum resulting from rolling the modified dice, based on the sums of values from Die_A and Die_B. These probabilities are determined by the frequency of each sum and the total number of outcomes, and the results are presented.

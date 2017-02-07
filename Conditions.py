#CONDITIONS (15PTS TOTAL)

# PROBLEM 1 (GPA - 4pts)
# Grades are values between 0 and 100
# We will translate grades to letters using:
# http://www.collegeboard.com/html/academicTracker-how to convert.html
# Make a variable for your percentage grade.
# Make a series of if/elif/else statements to print the letter grade.
# If the user enters a grade lower than zero or higher than 100, just give an error message.
# Don't worry about making an exception for these right now.

percentage_grade = input("Enter a percentage: ")

if percentage_grade > 100 or percentage_grade <0:
    print("Error")
elif percentage_grade >= 97 and percentage_grade <=100:
    print("You have an A+")
elif percentage_grade >= 93 and percentage_grade <= 96:
    print("You have an A")
elif percentage_grade >= 90 and percentage_grade <= 92:
    print("You have an A-")
elif percentage_grade >= 87 and percentage_grade <= 89:
    print("You have an B+")
elif percentage_grade >= 83 and percentage_grade <= 86:
    print("You have an B")
elif percentage_grade >= 80 and percentage_grade <=82:
    print("You have an B-")
elif percentage_grade >= 77 and percentage_grade <= 79:
    print("You have an C+")
elif percentage_grade >= 73 and percentage_grade <= 76:
    print("You have an C")
elif percentage_grade >= 70 and percentage_grade <= 72:
    print("You have an C-")
elif percentage_grade >= 67 and percentage_grade <= 69:
    print("You have an D+")
elif percentage_grade >= 65 and percentage_grade <= 66:
    print("You have an D")
elif percentage_grade >= 0 and percentage_grade <= 65:
    print("You have Failed")


# PROBLEM 2 (Vowels - 5pts)
# Ask the user to supply a string.
# Print how many different vowels there are in the string.
# The capital version of a lower case vowel is considered to be the same vowel.
# y is not considered a vowel.
# Try to print proper output (e.g., printing “There are 1 different vowels in the string” is ugly).
# Example: When the user enters the string “It’s Owl Stretching Time,”
# the program should say that there are 3 different vowels in the string.

vowel_a = False
vowel_i = False
vowel_u = False
vowel_o = False
vowel_e = False
user = input("Enter a string: ")
for j in range(len(user)):
    for i in range(len(user)):
        if user[j].lower() == "a":
            vowel_a = True
        if user[j].lower() == "i":
            vowel_i = True
        if user[j].lower() == "u":
            vowel_u = True
        if user[j].lower() == "o":
            vowel_o = True
        if user[j].lower() == "e":
            vowel_e = True
vowel_numbers = vowel_a+vowel_i+vowel_u+vowel_o+vowel_e
print("Numbers of vowels in string: ", vowel_numbers)





# PROBLEM 3 (Quadratic Equation - 6pts)
# You can solve quadratic equations using the quadratic formula.
# Quadratic equations are of the form Ax2 + Bx + C = 0.
# Such equations have zero, one or two solutions.
# The first solution is (−B + sqrt(B^22 − 4AC))/(2A).
# The second solution is (−B − sqrt(B^2 − 4AC))/(2A).
# There are no solutions if the value under the square root is negative.
# There is one solution if the value under the square root is zero.
# Write a program that asks the user for the values of A, B, and C,
# then reports whether there are zero, one, or two solutions,
# then prints those solutions.
# Note: Make sure that you also take into account the case that A is zero,
# and the case that both A and B are zero.


a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))

answers = 0

if ((b ** 2) - (4 * a * c)) == 0:
    print("Answer: ", b)
else:
    x = (-b -(((b ** 2) + (4 * a * c)))** 0.5)/(2 * a)
    y = (-b +(((b ** 2) + (4 * a * c)))** 0.5)/(2 * a)
    print("THe two answers are", y, "and", y)

from sys import argv

script, first, second, third = argv

answer_one = input(first)
answer_two = input(second)
answer_three = input(third)

print(f"Your answer to question one is: {answer_one}, \nYour answer to question two is: {answer_two}, \nYour answer to question three is: {answer_three} .")

#to run this program and the outcome:
#python drills/argv_drill.py "What is your name" "What is your quest" "What is your favorite color"
#What is your nameSarah
#What is your questBeamo
#What is your favorite colorYellow
#Your answer to question one is: Sarah,
#Your answer to question two is: Beamo,
#Your answer to question three is: Yellow .

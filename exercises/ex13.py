from sys import argv
#read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

#Pay attention to the presense of argv
#this particular file can't be run in the command line
#just by running python exercises/ex13.py

#must pass in arguments in the command line
#such as: python exercises/ex13.py first "Finn the Human" "Jake the Dog"
#will return:
#The script is called: exercises/ex13.py
#Your first variable is: first
#Your second variable is: Finn the Human
#Your third variable is: Jake the Dog

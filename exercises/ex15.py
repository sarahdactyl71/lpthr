from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())

#run with python exercises/ex15.py exercises/ex15_sample.txt
#should open the specified file in terminal

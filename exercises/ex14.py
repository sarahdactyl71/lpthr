from sys import argv

script, user_name = argv
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

#to run this biz

#python exercises/ex14.py "Sarah"
#Hi Sarah, I'm the exercises/ex14.py script.
#I'd like to ask you a few questions.
#Do you like me Sarah?
#>Sure thing babe!
#Where do you live Sarah?
#>NE Portland Oregon
#What kind of computer do you have?
#>Macbook that my work gave me

#Alright, so you said Sure thing babe! about liking me.
#You live in NE Portland Oregon. Not sure where that is.
#And you have a Macbook that my work gave me computer. Nice.

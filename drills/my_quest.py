#drills from exercise 31 asking to make my own game
print("""
You wake up in a strange room. \n
You aren't sure of how you got here or where you are. \n
You hear a noise, and as you come to,
you realize that you are not alone. \n
The voice starts to ask you some questions. \n
""")
print("What is your name?")
name = input("> ")
print("Why are you here?")
reason = input("> ")
print(f"So {name} you are here because of {reason})

print("""
You black out. \n
When you wake up once more you find yourself in a forest. \n
In the forest there is a trail that forks three ways. \n
1. The fork to the left is not well trodden,
but you can hear water as you near the head of the trail. \n
2. The fork in the middle is very dark.
When you investigate you can't see anything, but there is a scent of lavender. \n
3. The fork on the right is a bright and well used path.
You can hear people talking as you approach closer. \n
Which trail do you choose? 1, 2, or 3? \n
""")

trail = input("> ")

if trail == "1":

elif trail == "2":

elif trail == "3":

else:
    print("You didn't come here just to stand around. Pick a trail by typing 1, 2, or 3")

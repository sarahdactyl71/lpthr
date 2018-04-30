quest = input("What is your quest? ")
name = input("What is your name? ")
color = input("What is your favorite color? ")

#This method interpolates string with %s, kind of gross
print('So your name is %s, your quest is %s, and your favorite color is %s!' %(name, quest, color))
#This method intepolates the string with f in front of it and it's fucking beautiful,
#prettier than ruby dare I say.
print(f'So your name is {name}, your quest is {quest}, and your favorite color is {color}!')

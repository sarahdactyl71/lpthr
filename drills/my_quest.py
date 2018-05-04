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
print(f"So {name} you are here because of {reason}")

print("""
You black out. \n
When you wake up once more you find yourself in a forest. \n
In the forest there is a trail that forks three ways. \n
1. The fork to the left is not well trodden,
but you can hear water as you near the head of the trail. \n
2. The fork in the middle is very dark.
When you investigate you can't see anything, but there is a scent of lavender. \n
3. The fork on the right is a bright and well used path.
You can hear hushed voices as you approach closer. \n
Which trail do you choose? 1, 2, or 3? \n
""")

trail = input("> ")

if trail == "1":
    print("""
    You travel down the path for some time. \n
    You have to avoid getting scratched by branches
    and stumbling over roots. \n
    After walking this way for some time you come upon a stream
    where a red stag drinks water. \n
    Do you... \n
    1. Pet the stag to try and make him your best friend. \n
    2. Sit next to the stag and drink from the stream. \n
    """)
    choice = input("> ")

    if choice == "1":
        print("""You walk up to the stag who seems wary of you. \n
        But after taking your time and letting it smell your hand,
        it gets comfortable with you. \n
        You hop on its back, name it 'Dave' and get into shennanigans for years to come. \n""")
    if choice == "2":
        print("""
        You drink from the stream and feel drowsy. (Sleep again?) \n
        You resist the urge to fall into a deep slumber when you see your
        body start to transform. \n
        You grow hooves where your hands and feet used to be. \n
        Your body grows fur and you can feel antlers start to grow from your skull. \n
        You notice at the same time, the stag is also transforming. \n
        Gaining human parts as you lose yours. \n
        Just as the transformation is complete,
        you see the newly formed human stretch her arms and say \n
        "How long has it been? Years since I have walked on two feet? Sorry stranger,
        but I did what I had to. Now it's your turn to wait for a human to drink from this stream."
        """)
    else :
        print("Pay attention to instructions.")

elif trail == "2":
    print("""
    You can't see anything as you wander through the darkness. \n
    You move with your hands streched in front of you, protecting your face. \n
    As you gain distance the smell of lavender increases until it is almost too much to bear. \n
    You feel a hand reach out for yours, leading you further down the path. \n
    The hand is small, but it feels non-threatening. \n
    Do you follow it? \n
    1. Yes \n
    2. No \n
    """)
    choice = input("> ")

    if choice == "1":
        print("""
        You let the hand guide you down the path. \n
        Soon, you can see more and more light illuminating the path until
        you have found your way out of the forest. \n
        You turn to greet the being that guided your way here,
        and thank it for their kindness. \n
        But when you look there is nothing there. \n
        You look at your hand to see an impression of a tiny
        hand embedded in yours. \n
        You shudder, and walk out of the forest. \n
        """)
    else:
        print("""
        You wander in the darkness wondering if anyone will ever find you on this path. \n
        You don't know how much time as passed, but you feel like it has to be days at least. \n
        Hunger has subsided, but you are so thirsty. \n
        You lay down to rest, just for a minute... \n
        """)
# elif trail == "3":

else:
    print("You didn't come here just to stand around. Pick a trail by typing 1, 2, or 3")

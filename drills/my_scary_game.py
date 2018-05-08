from sys import exit

def start_game():

    print("""
    Through a series of escalading dares you and your friends find yourselves
    in a house that local legends would lead you to believe is haunted. \n
    You don't believe in ghosts or demons, but even so, as you walk through the
    threshold of the front door, you find yourself a bit nervous. \n
    Looking around you are in the foyer of a once great mansion. \n
    The years of neglect and decay have done their work on the home. \n
    You find it odd that none of the finer pieces like the candleabras
    or oil paintings have been looted. \n
    There is a suspicious looking stain in the persian carpet that you tell yourself
    is just mud and debris. \n
    You are the leader of your group. \n
    Which way do you go first? \n \n
    The left side: It looks like it leads to a grand living room, with a disheveled
    grand piano and several pieces of fine handmade furniture. \n
    The right side: It looks like it leads to a kitchen. All the pots and pans are out, like
    someone left in a hurry, and because of the dripping water and the dishes in the sink, you feel
    like it has been used recently. \n
    Up the stairs: You can't tell much from looking up the stairs. The only thing you can ascertain
    is that there is a light far off in the distance, slightly illuminating one of the hallways.
    """)

    explore()

def dead(reason):
    print(f"{reason}. Dare you play again?")

    choice = input("> ")

    if choice == "no":
        exit(0)
    elif choice == "yes":
        start_game()
    else:
        print("Try typing 'yes' if you want to play again, or 'no' if you don't.")
        dead("Dare you play again?")

def explore():

    print("Which room will you explore?")

    choice = input("> ")

    if "left" in choice or "living room" in choice:
        living_room()
    elif "right" in choice or "kitchen" in choice:
        kitchen()
    elif "stairs" in choice or "up" in choice:
        explore_upstairs()
    else:
        print("Are you too chicken to choose a direction?")
        start_game()

def explore_upstairs:
    print("""
    You start to ascend the creaky steps. They groan so loudly you think they will collapse
    under your weight. Hand on the railing, you and your friends breath a sigh of relief
    when you have reached the top of the stairs. 
    """)

def living_room():
    print("""
    You lead your friends into the living room. The entire room is covered with a thin layer of dust
    except for the grand piano which somehow, despite its degree of dilapitation, is seemingly spotless. \n
    Your can feel the mood in the room start to shift, but your friends shake it off among some nervous laughter. \n
    You are drawn to the piano. You don't know how to play, but you get a sudden urge to push your fingers down on the
    ivory keys. \n
    Do you dare play? Or will you explore another room? \n
    """)

    choice = input("> ")

    if "yes" in choice or "play" in choice:
        print("""
        You press one finger down on a key. The piano is badly out of tune, but you can't resist playing another key, and then another. \n
        Soon you are sitting on the bench playing your heart out to a tune that both pains and excites you. \n
        The more you keep playing the less the piano sounds out of tune, and the more
        it sounds like sweet music. \n
        You play until your fingers are raw, and you can feel hunger growing in your belly. \n
        You play your way to the final cresendo, fingers cascading down the keys almost too fast to be visible. \n
        Once the final note has been played you breath a sigh of releif. Your masterpiece is complete. \n
        You turn to see your friends but instead you are in an area restored to its former grandeur. \n
        An audience of ghostly figures applauds you. \n
        'Play another!' they shriek. \n
        You turn back to the piano. \n
        """)

        dead("""You are caught in a never ending loop of piano playing. \n
        You don't know how much time has passed, but eventually you are ushered off the piano bench
        and onto a seat in the audience. \n
        You don't understand, wasn't your playing enjoyable. \n
        A sad woman nearby seems to read your mind when she says 'Don't worry, we will just wait here until another player arrives. \n
        """)

    elif "explore" in choice or "room" in choice:
        explore()
    else:
        print("I don't understand. Try typing 'yes' or 'no'.")
        living_room()

def kitchen():
    print("""
    You enter the kitchen and are surprised to find it extraordinarily clean in an organized chaos kind of way. \n
    It seems like every piece of cookware is out of the cabinets and again you ask yourself why this stuff hasn't been stolen a long time ago.
    It is vintage but quality cookware from an era you can't recognize. You wonder how much a set like this must cost today. \n
    As you explore more of the kitchen, you turn around the kitchen island to find a small table with two chairs propped against a wall.
    On the table is an exotic dish. A type of cuisine you have never seen before. The smell emitted from it is delicious. Your mouth waters
    and you hear your friend Tom come up behind you. 'If you don't take a bite then I will' he says. \n
    Do you take the first bite or will you let Tom taste the delicacy before you?
    """)

    choice = input("> ")

    if "Tom" in choice or "tom" in choice:
        print("""
        Tom takes a hesitant first bite, but as he chews and swallows, you can see he enjoys it. He groans with delight as he forks a
        second, and then a third. His eyes get wide and soon he has wolfed down the entire dish. He picks up the plate and licks it clean. \n
        'That was so GOOD!' Tom yells. 'I HAVE TO HAVE MORE!'. Tom frantically searches through the kitchen to find any morsel of what he
        just ate. You see his eyes grow desperate and wild. 'PLEASE, I NEED MORE!' he shouts again. \n
        You walk over to comfort him or snap him out of whatever he is experiencing. You put a hand on Tom's shoulder, but before you can think of what to
        say, he graps your arm and sniffs deeply. 'Oh, THAT'S IT!' he screams. You try to yank your arm away, but Tom has too firm a hold. Tom takes a bite
        out of your arm and you are blinded with pain. You shout out to your remaining friends, but they have fled. \n
        You are soon overpowered by Tom who is wasting no time whittling you away bite by bite.
        """)

        dead("You start to lose vision and everything goes black. The last thing you feel is the far away sensation of Tom biting into your neck.")
    else:
        print("""
        You try to hide your nerves with a smile as you pick up the fork near the plate. You pry off the smallest portion possible,
        put it in your mouth and chew. You notice a slight off flavor, but also slightly familiar flavor to the meat. At first you
        are repulsed by it, but as you begin to chew it tastes more delactable and savory. \n
        Before you are aware of what is happening, the plate is clean. You feel a hunger start to boil in your stomach. You ignore
        it at first, but it grows from a dull annoyance to a crippling gurgle. \n
        You frantically search for anything edible. You tear through the kitchen, throwing pots and pans around, short of tearing
        your hair out. You turn and see your friends. Tom who is closest to you stares wide-eyed. \n
        You sniff the air. Something smells sweet. You follow your nose closer to the smell until you realize that it is coming
        from Tom. Not only is it coming from him, it IS him. \n
        You try to hide the fact that your mouth is watering. You do a poor job of this as you lick your lips. \n
        'Tom' you say 'when did you start smelling so... delicious'? Tom puts up his arms in defense as you lunge at him. You
        start taking bites from his legs as he squirms. He goes still when you go for his neck. \n
        """)

        dead("""You wipe your mouth when you are satiated. Knowing that you can't go home you decide it best to sit and wait for the next
        group of silly teenagers to come through. \n
        """)

start_game()

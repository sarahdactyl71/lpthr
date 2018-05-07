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

    choice = input("> ")

    if "left" in choice or "living room" in choice:
        living_room()
    elif "right" in choice or "kitchen" in choice:
        kitchen()
    elif "stairs" in choice or "up" in choice:
        upstairs()
    else:
        print("Are you too chicken to choose a direction?")
        start_game()

def living_room():
    print("""
    You lead your friends into the living room. The entire room is covered with a thin layer of dust
    except for the grand piano which somehow, despite its degree of dilapitation, is seemingly spotless. \n
    Your can feel the mood in the room start to shift, but your friends shake it off among some nervous laughter. \n
    You are drawn to the piano. You don't know how to play, but you get a sudden urge to push your fingers down on the
    ivory keys. \n
    Do you dare play? \n
    """)

    choice = input("> ")

    if choice == "yes":
    elif choice == "no":
    else:
        print("I don't understand. Try typing 'yes' or 'no'.")
        living_room()

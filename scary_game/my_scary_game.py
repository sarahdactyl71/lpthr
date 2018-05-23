from sys import exit

import explore_main_floor


def explore_basement():
    print("""
    You investigate the main floor to find the only closed door. You think it might be a broom closet, but you open
    it anyway. You find a winding, dusty, staircase leading to the basement. There is no light, but you find an electrical wire
    snaking its way on the wall. You can't find an outlet, but you assume that there will be a switch at the bottom of the stairs. \n
    With your right hand on the railing, you lead the way down to the basement in hopes of finding what you are searching for. \n
    You were right about the light switch. You flick it on, and for a breif moment light illuminates the room before the very old bulb shatters. \n
    You aren't sure if you saw a figure in the breif moment that the lights were on, or if it was just your imagination. Since this is the age of
    technology, everyone in your party gets out their cellphones to illuminate the room. The room is still shrouded in shadow, but it is just bright
    enough to make out the objects in the room. \n

    """)

    choice = input("> ")


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
        explore_main_floor()
    else:
        print("I don't understand. Try typing 'yes' or 'no'.")
        living_room()


start_game()

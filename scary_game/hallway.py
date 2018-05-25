class Hallway():

    def hallway(self):
        print("""
        Maybe you are feeling bold, or perhaps you are feeling a bit rash, but
        you decide to follow the voice that was coming from the hallway. You make
        your way forward, apprehensive of what you might find. \n
        There is a mirror at the end of the hall, only visible by the moonlight
        coming through one of the windows. In the mirror you see the reflection of
        a little girl. The era of her clothing looks like the era of the house, and
        similarly, in the same degree of disrepair. \n
        You walk closer to the mirror, directly in front of it, and address the child.
        You ask her what she is doing in the mirror, and why she told you to avoid
        the other room. \n
        The girl begins "A powerful deamon resides in that room. It trapped me in this
        mirror long ago, and it is one of the main reasons why this place is cursed.
        The deamon changes its appearence everytime you encounter it. It can look like
        a stranger or someone you know. This makes it particularly fearsome." \n
        You aren't sure what to say, or really, if you believe what you are seeing.
        The girl inturrupts your thoughts. "Help me," she pleads "something has
        to be done about this presence. Then I will finally be able to get out of this
        prison." The girl says the last part with a frown. \n
        Part of you is hesitant, but the other part wants to help this poor child.
        What do you do? \n
        Help the girl, or leave the house now?
        """)

        choice = input('> ')

        if "help" in choice:
            from dead import Dead
            print("""
            """)

            Dead().dead("""
            """)

        elif "leave" in choice:
            from upstairs_to_main_floor import UpstairsToMainFloor
            UpstairsToMainFloor().upstairs_to_main_floor()

        else:
            print(f"I don't understand {choice}. Try typing 'leave' or 'help'.")
            Hallway().hallway()

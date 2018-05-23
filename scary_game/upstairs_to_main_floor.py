class UpstairsToMainFloor():

    def upstairs_to_main_floor(self):
        print("""
        You and your friends are pretty creeped out at this point. You look around,
        meet everyone's eyes and motion your head to go down the stairs. Your friends
        nod, and you start to creep back down the way you came. As your last friend
        is about halway down the staircase, you hear one final creak and know that something
        is wrong. You feel the boards begin to creak beneath you. The wooden stairs
        begin to spinter and crack revealing that there is much more than just one floor
        that you will fall. You think that if you jump you can make it before the
        stairs collapse. However, you see your friend Lydia, will never make the jump.
        Do you jump and risk it or do you save Lydia?
        """)

        choice = input("> ")

        if "jump" in choice:
            print("""
            You manage to jump out of the way just in time, landing cleanly on your feet.
            Lydia, however, was not so lucky. You call her name down the cavernous black
            hole where the staircase used to be. You can't see anything and you hear
            nothing in response. What do you do? \n
            Do you cut your losses and leave the house? \n
            Or do you risk it all to save Lydia? \n
            """)

            choice = input("> ")

            if "leave" in choice:
                from dead import Dead
                Dead().dead("""You are too stunned from surviving the fall that you
                have no time to greive for your lost friend. You leave the house bruised,
                but you are alive. Time passes and you have never gone back to the house,
                out of fear, and also guilt. You are much older now, and you hear urban legends
                from the younger generation speaking of a young woman, badly crooked,
                wandering the house seeking her lost friends.""")
            else:
                from basement import Basement
                Basement().explore_basement()

        elif "Lydia" in choice or "save" in choice or "lydia":
            from dead import Dead
            Dead().dead("""
            You, and a few others, fall with Lydia to the cavern below. You land
            hard on your side. As you get up you find that you are badly injured,
            but you are able to walk. Upon investigation however, you find that some
            of your friends are not as lucky. \n
            As you investigate your surroundings you see no way out. It is as if this
            pit was here for this purpose. You touch the wall to find that it is carved
            from jagged rock. Lydia, who is the only climber among you, would have been
            able to scale out of there but here injuries are too extreme. You scream
            for help, but you know that there is no one around for miles. After several
            failed attempts you sit with your back against a wall. All you can do
            now is wait.
            """)
        else:
            print("Try typing 'Lydia' or 'jump'.")
            UpstairsToMainFloor().upstairs_to_main_floor()

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
            You decide that you should help this girl. You ask what you can do.
            She tells you that you need to remove the mirror from the wall. She reminds
            you to be careful, that this will only work if the mirror is intact.
            "Move it forward in front of you like a shield. Be mindful never to look
            at the deamon. Let my voice be your guide and I will take care of the rest." \n
            You pull the mirror off the wall. Just before you turn the mirror away from
            you, the girl flashes a smile. The mirror feels cumbersome in your hands as you
            move towards the illuminated room. When you reach the threshold of the room
            the already ajar door drifts open, inviting you in. \n
            You see nothing but the wooden panel of the back of the mirror, but you
            can feel the warmth of the fire on the fronts of your fingers. A voice that
            defies age, gender, or accent speaks "So it has finally come to this". Your
            grip tightens on the mirror. \n
            You hear someone stand up from a chair. Face still behind the mirror, you
            look off to the side and observe the shadows cast by the fire. You see
            a shape move toward you that is impossibly large. At first glance it resembles
            a human figure, the next you aren't even sure how you thought it looked
            human in the first place. \n
            That is the last thing you remember before you hear shrill, shrieking sounds
            that make you want to put your hands to your ears. You hold tighter to
            the mirror. Your fingertips feel heat, then they start to burn and sear.
            You grip the mirror through blinding pain. \n
            Almost as soon as it began it is over. You don't understand what transpired.
            You removed a hand from the mirror to inspect the damage. As you release your
            grip you see smoke rising from your singed hand. "Turn the mirror around, touch
            the glass and I can heal you the girl says". \n
            With some pain your turn the mirror to face you and put both palms on the glass.
            A light starts emitting from where your hands make contact and you can see
            your wounds healing, like you are watching the damange that was done in
            rewind. Your hands heal completely. When you try to pull them away they are
            stuck to the glass. You look up to see the little girl is sporting a
            sinsiter grin. \n
            You are actively working to pull your hands away, but bit by bit you are
            losing sensation in your arms. This moves through your torso, to your legs,
            and eventually, your head. You feel drowsy, like you are in a dream. \n
            You see your hands pull away and flex. You did not do this. You look to the
            mirror and the little girl has vanished.
            """)

            Dead().dead("""
            Your body stretches, takes in a deep breath, and sighs. "Ahhh!" you hear
            your own voice say. "It feels good to be back in flesh!" You try to scream
            but nothing happens. "Well, thank you for that! I have been stuck in that mirror
            for centuries. That deamon trapped me there years ago. Thanks for freeing me!
            Now, let's join your friends shall we?"
            """)

        elif "leave" in choice:
            from upstairs_to_main_floor import UpstairsToMainFloor
            UpstairsToMainFloor().upstairs_to_main_floor()

        else:
            print(f"I don't understand {choice}. Try typing 'leave' or 'help'.")
            Hallway().hallway()

class UpstairsRoom():

    def upstairs_room(self):
        print("""
        You can't resist the pull of the mysterious room. You creep up the stairs
        doing your best to do so quietly. Even so, the stairs complain with every step
        you take. You look behind your right shoulder, and stretch out your hand perpendicular to the
        ground. A guesture that your friends understand means hang back. You feel a
        palpable sigh of relief from some of the people in the group as you turn back to
        continue on alone. \n
        You take hesitant steps on the floor runner, sending dust spurting up with each foot
        fall. You feel your heart beat increase as you near the door. The warmth coming
        from the doorway is warm, somehow both comforting and unnerving. \n
        You take a deep breath as you splay your fingers out to gently push the door the rest of
        the way open. \n
        The view in front of you is... almost normal? The room is well lighted, with a
        fireplace blazing. The walls and floors are clean, a stark juxtoposition from the rest
        of the house you have explored. The walls are adorned with giant oil paintings. Each
        depciting what you assume to be a scene from some religious text. \n
        You hear a creak, and you nearly stumble backwards when you see a rocking chair
        sitting in front of the fire moving on its axis backward. How could you have missed
        the chair? Surely you would have known something else was in the room with you?
        The chair was there when you walked in the room right? Right? \n
        You gulp, and attempt to go back the way you came. When a voice from the chair states "
        I am really tired of you kids coming into my home and disturbing my peace. This is breaking and
        entering you know. I have a mind to call the authorities on you." \n
        You try to stammer a reply, but before you can formulate that first word, the stranger
        speaks again "Tell you what, I haven't entertained visitors in a long time, and I am very lonely. Play me at a game of
        chess, or a hand of cards, and I won't call the police." \n
        Which do you play? \n
        """)

        choice = input('> ')

        print(f"""
        Confidence suddenly on your side, you say "{choice}" in a flat voice. From the side of the chair
        you see a gloved hand guesture you forward.
        """)

        if "chess" in choice:
            from dead import Dead
            print("""
            You approach from the right hand side. Sitting in the rocking chair, you see a frail old woman.
            She has a wool blanket resting over her legs, and is rocking gently back and forth on feet that you cannot see.
            She is wearing a neat, white, bun on the top of her head, and earrings so grand, and so large, you are surprised she
            isn't toppling over. Despite her frailty she sits with an incredibly straight back. You try not to think that she
            might be stronger than she would appear. \n
            Without words she looks at you and nods at the board in front of her. Already set up, immaculately clean. The pieces
            gleam in the flickering fire. You sit in the armchair opposite the old woman. You convince yourself the armchair was always there.
            The room itself, feels bigger somehow, but after looking around it appears that nothing has changed. \n
            The woman makes the first move with a shaky hand. You follow up, first moving pawns to free up other
            pieces on the board. After the woman moves her rook across the board to take one of your knights you notice her hands
            are far less shaky. You move a piece to set up taking her rook and you see that your hands are losing composure. Nerves maybe?
            Maybe it was a trick of the fire, but the woman's hair looks far darker than you first noticed. \n
            You start to feel tired, at first a bit drowsy, but soon it is hard to keep your eyes open. You are hardly aware
            that you are playing the game, moving pieces less and less carefully. \n
            "Checkmate", you hear, nearly startled out of sleep. You look at the board and see that indeed it is checkmate.
            A checkmate that you should have been able to avoid. You send your gaze to the old woman. However she isn't old anymore.
            The hair on her head is thick and healthy, hands strong and certain in their movement. \n
            You look down at your hands, frail, shakey, full of veins and skin like paper. You touch your face to find the elastic
            has gone out of it, and you feel sagging flesh. Running your hands through your hair you find it is thin and brittle. \n
            The woman hops up from her seat "That was a lovely game" she says. "I doubt we will play again, sorry". She walks out
            of the room.
            """)
            Dead().dead("""You try to get up and follow her, but you find that you are too weak. All you can do is rock back and forth in your chair
            and warm your legs by the fire.""")

        elif "cards" in choice:
            print("""
            You approach from the left hand side.
            """)

        else:
            print("""
            Not sure what you are getting at. Try typing 'cards' or 'chess'.
            """)
            UpstairsRoom().upstairs_room()

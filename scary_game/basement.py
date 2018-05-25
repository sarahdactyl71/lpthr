class Basement():

    def explore_basement(self):
        print("""
        You investigate the main floor to find the only closed door. You think it
        might be a broom closet, but you open it anyway. You find a winding, dusty,
        staircase leading to the basement. There is no light, but you find an electrical
        wire snaking its way on the wall. You can't find an outlet, but you assume
        that there will be a switch at the bottom of the stairs. \n
        With your right hand on the railing, you lead the way down to the basement
        in hopes of finding what you are searching for. \n
        You were right about the light switch. You flick it on, and for a breif
        moment light illuminates the room before the very old bulb shatters. \n
        You aren't sure if you saw a figure in the short time that the lights
        were on, or if it was just your imagination. \n
        Since this is the age of technology, everyone in your party gets out their
        cellphones to illuminate the room. The room is still shrouded in shadow,
        but it is just bright enough to make out some of the objects scattered about. \n
        It looks like a storage room, or an old mueseum for turn of the century gadgets,
        made obsolete by newer inventions and cast aside. You see a butter churn,
        a loom, and an ornately carved chair that looks very uncomfortable to sit
        upon. None of these objects prove any use to you. \n
        After everyone has had time for their eyes to adjust, your friend Amy
        points at your feet and exclaims "You're standing on a trap door!". Confused,
        and a bit flustered, you look down at your shoes to see a trapdoor that even
        in this house, looks ancient. You don't need to touch it to know that it is
        extremely heavy, and you can feel a light draft on your ankles if you pay
        attention. \n
        You step aside, bend down, and try your hand at swinging the massive door open.
        You grip your hands around the circular lever. Just as you are starting to
        put your might into swinging the trap door open, your friend Brian interrupts. \n
        "Hey! Everyone! Check this out!" Brian is standing next to a wobbly shelf.
        At first glance you don't see what the big deal is, but after everyone aims
        their phones at the shelf, Brian pushes it aside to reveal a door.
        The door is red, or rather was painted red a long time ago. Most of the color
        has been scraped off. It looks like a very similar make to the trapdoor on the
        floor. "I think I can hear something moving on the other side!" Brian tells you.\n
        Which door do you go through? The trapdoor or the red door?
        """)

        choice = input("> ")

        if "red" in choice:
            from dead import Dead
            print("""
            You stand up from your squat and make your way to the red door. You give
            Brian a nod as you grab the donut shaped knob and pull towards yourself.
            It's heavy, but you manage to get it open on your own. You hear a click
            as the door settles all the way open, as far back on its hinges as it can go.
            You smell the scent of earth and mildew. Before you is a long, dark tunnel.
            You take a few steps into the tunnel, strain your ears and find that Brian
            was right, there IS something moving in the distance. It sounds like
            footfalls, but the cadence is unfamiliar, and you also hear a constant
            sound like something is being dragged. \n
            You tenatively make a few steps forward, as if you are unsure if the
            ground will support you. After a few steps you find comfort in the earth
            pushing back at you and you guesture your friends to follow you deeper into
            the tunnel. \n
            Keeping your right hand on the wall you walk, following the sound as it gets
            more and more defined. The tunnel gradually widens to a large room with
            several eroding pillars. You know the sound is coming from this room, but for
            whatever reason it is hard to triangulate. \n
            You hear an odd thud on the ground... then another. The third time you hear
            it, you turn around to see three of your friends on the ground. Their mouths
            are wide, screaming a silent scream and their eyes stare off into the distance.
            Brian is amongst the three fallen. You bend down to touch him and feel a
            slimy substance on his skin. He is cold to the touch. You turn your head
            to come over Brians mouth, and feel his neck for a pulse... nothing. \n
            As you stand up to talk with the rest of your friends about an escape you hear
            the sound that you now identify as a fallen friend. You hear that sound again,
            as you turn, and once more before your eyes can adjust.
            """)

            Dead.dead("""
            You look around and see now that everyone you were with is dead on the floor.
            You hear walking and dragging sound, so very close now. You close your
            eyes and wait. \n
            """)

        elif "trap" in choice:
            print("""
            You look at Amy, and together you heave the trapdoor open. You have
            Just enough time to move out of the way as the door crashing on the
            ground where you just were. A coolness escapes from the chamber envelops
            you all and the group lets out a shudder. \n
            You look down and all you can see is darkness, with a rope ladder leading
            the way down, eventually disappearing as the light has no more to travel. \n
            You start making your way down. The ladder squeaks under your weight, but
            after pushing yourself into it you determine that it should hold. Step by
            step, you make your way down until your foot rests softly on the dirt floor. \n
            One after the other your friends continue down in the same fashion. Now, it
            is just Amy reamaining at the top of the entrance. \n
            You call her name, and ask her to come down. She seems nervous, and
            understandably so. After some convincing, Amy makes decends about halway
            down the ladder when you notice something is wrong. \n
            Like in a movie or a text based adventure game, you hear the sound of the
            ropes fraying, and beginning to snap strands. You call Amy's name but she
            seems to be paralyzed. You know that if you try and climb the ladder the
            ropes with snap faster with you on it. You call her name again and she has
            just enough time to give you a terrified look over her shoulder and the
            ladder breaks. \n
            You can only watch as the the ladder falls to the ground with Amy to follow.
            You rush over to where Amy lay. She has blood running out of one ear
            and she shows no signs of movement. You check her pulse and find that she,
            in one sense of the phrase, is no longer with you. \n
            As much as you would like to mourn, you have bigger concerns. As far as you
            know, the ladder was the only way out of the pit. There is no cell phone
            reception down here for you to call for help. However, after some inspection
            you find that there seems to be channels of paths branching off from the
            main chamber you find yourself in. The group decided that you should split up,
            and should anyone find an exit they will come back and rescue everyone else.
            You and two friends take the left most tunnel, and start to walk. Still using
            your phones to light the way, you walk for a several hours. \n
            You notice that the walls are occasionally adorned with simple paintings.
            Most depicting people travelling in the direction that you are walking.
            How ironic. \n
            You hear a beeping noise and one of your friends informs you that their
            phone is almost out of battery. After a few minutes, it turns off completely,
            and you try not to notice that it is a bit darker. And hour later. the same thing
            happens to your other friend. You gulp and lead the way carrying the only light
            you have. After a while that too, blinks out. \n
            Your only option is to keep a hand on the wall and continue wandering
            blindly forward.
            """)

            Dead().dead("""
            You're not sure how much time has passed, or how you lost your friends
            along the way. Steps becoming harder now, you focus on moving one foot in
            front of the other, until you cannot propel yourself forward. You tell
            yourself it would be okay to sit and rest. You'll get up at any moment and
            keep walking. Any moment. 
            """)

        else:
            print("""
            I don't understand. Try typing 'trapdoor' or 'red door'.
            """)
            Basement().explore_basement()

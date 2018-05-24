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
        floor. \n
        Which door do you go through? The trapdoor or the red door?
        """)

        choice = input("> ")

        if "red" in choice:
            print("""
            """)

        elif "trap" in choice:
            print("""
            """)
            
        else:
            print("""
            I don't understand. Try typing 'trapdoor' or 'red door'.
            """)
            Basement().explore_basement()

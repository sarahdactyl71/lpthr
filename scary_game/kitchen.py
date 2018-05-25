class Kitchen():

    def kitchen(self):
        print("""
        You enter the kitchen and are surprised to find it extraordinarily clean in
        an organized chaos kind of way. \n
        It seems like every piece of cookware is out of the cabinets and again
        you ask yourself why this stuff hasn't been stolen a long time ago.
        It is vintage but quality cookware from an era you can't recognize.
        You wonder how much a set like this must cost today. \n
        As you explore more of the kitchen, you turn around the kitchen island to
        find a small table with two chairs propped against a wall. On the table is
        an exotic dish. A type of cuisine you have never seen before. The smell
        emitted from it is delicious. Your mouth waters and you hear your friend,
        Tom come up behind you. 'If you don't take a bite then I will' he says. \n
        Do you take the first bite or will you let Tom taste the delicacy before you?
        """)

        choice = input("> ")

        if "Tom" in choice or "tom" in choice:
            from dead import Dead
            print("""
            Tom takes a hesitant first bite, but as he chews and swallows, you can
            see he enjoys it. He groans with delight as he forks a second, and then
            a third. His eyes get wide and soon he has wolfed down the entire dish.
            He picks up the plate and licks it clean. \n
            'That was so GOOD!' Tom yells. 'I HAVE TO HAVE MORE!'. Tom frantically
            searches through the kitchen to find any morsel of what he just ate.
            You see his eyes grow desperate and wild. 'PLEASE, I NEED MORE!' he
            shouts again. \n
            You walk over to comfort him or snap him out of whatever he is experiencing.
            You put a hand on Tom's shoulder, but before you can think of what to
            say, he graps your arm and sniffs deeply. 'Oh, THAT'S IT!' he screams.
            You try to yank your arm away, but Tom has too firm a hold. Tom takes
            a bite out of your arm and you are blinded with pain. You shout out to
            your remaining friends, but they have fled. \n
            You are soon overpowered by Tom who is wasting no time whittling you
            away bite by bite.
            """)

            Dead().dead("""You start to lose vision and everything goes black. The last
            thing you feel is the far away sensation of Tom biting into your neck.""")

        elif "me" in choice or "I do" in choice:
            from dead import Dead
            print("""
            You try to hide your nerves with a smile as you pick up the fork near
            the plate. You pry off the smallest portion possible, put it in your
            mouth and chew. You notice a slight off flavor, but also slightly familiar
            flavor to the meat. At first you are repulsed by it, but as you begin
            to chew it tastes more delactable and savory. \n
            Before you are aware of what is happening, the plate is clean. You feel
            a hunger start to boil in your stomach. You ignore it at first, but it
            grows from a dull annoyance to a crippling gurgle. \n
            You frantically search for anything edible. You tear through the kitchen,
            throwing pots and pans around, short of tearing your hair out. You turn
            and see your friends. Tom who is closest to you stares wide-eyed. \n
            You sniff the air. Something smells sweet. You follow your nose closer
            to the smell until you realize that it is coming from Tom. Not only is
            it coming from him, it IS him. \n
            You try to hide the fact that your mouth is watering. You do a poor job
            of this as you lick your lips. \n
            'Tom' you say 'when did you start smelling so... delicious'? Tom puts up
            his arms in defense as you lunge at him. You start taking bites from his
            legs as he squirms. He goes still when you go for his neck. \n
            """)

            Dead().dead("""You wipe your mouth when you are satiated. Knowing that you
            can't go home you decide it best to sit and wait for the next group of silly
            teenagers to come through. \n
            """)

        else:
            print(f"""
            I don't understand {choice}. Try typing 'me' or 'Tom'.
            """)
            Kitchen().kitchen()

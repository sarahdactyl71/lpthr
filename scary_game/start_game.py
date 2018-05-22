from sys import exit

# import explore_main_floor
from explore_main_floor import ExploreMainFloor

class Start():

    def start_game(self):

        print("""
        Through a series of escalading dares you and your friends find yourselves
        in a house that local legends would lead you to believe is haunted. \n
        You don't believe in ghosts or demons, but even so, as you walk through the
        threshold of the front door, you find yourself uncharacteristically nervous. \n
        Looking around you are in the foyer of a once great mansion. \n
        The years of neglect and decay have done their work on the home. \n
        You find it odd that none of the finer pieces like the candleabras
        or oil paintings have been looted. \n
        There is a suspicious looking stain in the persian carpet that you tell yourself
        is just mud and debris. \n
        You are the leader of your group. \n
        Which way do you go first? \n
        The left side: It looks like it leads to a grand living room, with a disheveled
        grand piano and several pieces of fine handmade furniture. \n
        The right side: It looks like it leads to a kitchen. All the pots and pans are out, like
        someone left in a hurry, and because of the dripping water and the dishes in the sink, you feel
        like it has been used recently. \n
        Up the stairs: You can't tell much from looking up the stairs. The only thing you can ascertain
        is that there is a light far off in the distance, slightly illuminating one of the hallways.
        The only closed door in sight. \n
        """)

        explore_main_floor.ExploreMainFloor().explore()

Start().start_game()

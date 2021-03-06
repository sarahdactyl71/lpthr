class ExploreUpstairs():

    def explore(self):
        print("""
        You start to ascend the creaky steps. They groan so loudly you think they
        will collapse under your weight. Hand on the railing, you and your friends
        breathe a sigh of relief when you have reached the top of the stairs. You
        look to the right where the light is coming from. It is behind a closed door.
        The light doesn't seem to be consistent, as if it is a flickering candle
        or a fireplace. As you take a step towards the door you hear a small voice
        behind you that whispers "Turn around, don't go in there!". You look over
        your shoulder and see nothing but the darkened hallway to your left. \n
        Which way do you go? \n
        Back down the stairs? Go through the door? Investigate the hallway? \n
        """)

        choice = input("> ")

        if "stairs" in choice or "down" in choice:
            from upstairs_to_main_floor import UpstairsToMainFloor
            UpstairsToMainFloor().upstairs_to_main_floor()
        elif "door" in choice or "room" in choice:
            from upstairs_room import UpstairsRoom
            UpstairsRoom().upstairs_room()
        elif "hallway" in choice:
            from hallway import Hallway
            Hallway().hallway()
        else:
            "Try typing 'stairs', 'hallway', or 'door'"
            ExploreUpstairs().explore()

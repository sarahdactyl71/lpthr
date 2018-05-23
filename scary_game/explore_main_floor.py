class ExploreMainFloor():

    def explore_main_floor(self):

        print("Which room will you explore?")

        choice = input("> ")

        if "left" in choice or "living room" in choice:
            living_room()
        elif "right" in choice or "kitchen" in choice:
            from kitchen import Kitchen
            Kitchen().kitchen()
        elif "stairs" in choice or "up" in choice:
            from explore_upstairs import ExploreUpstairs
            ExploreUpstairs().explore()
        elif "door" in choice or "closed" in choice:
            explore_basement()
        else:
            print("""Are you too afraid to continue? \n
            Try typing 'lving room', 'basement', 'kitchen', or 'upstairs'.""")
            ExploreMainFloor().explore()

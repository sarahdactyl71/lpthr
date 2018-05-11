class ExploreMainFloor():

    def explore(self):
        print("Which room will you explore?")

        choice = input("> ")

        if "left" in choice or "living room" in choice:
            living_room()
        elif "right" in choice or "kitchen" in choice:
            kitchen()
        elif "stairs" in choice or "up" in choice:
            explore_upstairs()
        elif "door" in choice or "closed" in choice:
            explore_basement()
        else:
            print("Are you too chicken to choose a direction?")

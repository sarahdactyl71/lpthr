class Dead():

    def dead(self, reason):
        print(f"{reason} \n\n\n DARE YOU PLAY AGAIN (yes/no)???")

        choice = input("> ")

        if choice == "no":
            exit(0)
        elif choice == "yes":
            from start_game import Start
            Start().start_game()
        else:
            print("Try typing 'yes' if you want to play again, or 'no' if you don't.")
            Dead().dead("DARE YOU PLAY AGAIN (yes/no)???")

import start_game

class Dead():

    def dead(self, reason):
        print(f"{reason}. Dare you play again?")

        choice = input("> ")

        if choice == "no":
            exit(0)
        elif choice == "yes":
            start_game()
        else:
            print("Try typing 'yes' if you want to play again, or 'no' if you don't.")
            Dead().dead("Dare you play again?")

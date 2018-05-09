# MODULES, CLASSES, AND OBJECTS

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

yung_lean = Song(["So many lies that I've found",
                  "Blood, heaven, I stick to the ground",
                  "So many times I've realized",
                  "What I seek for is right in front of my eyes"])

the_surf = Song(["I shelter on the beach",
                 "All alone",
                 "You are the reach",
                 "The surf comes every day",
                 "Washes my creations away"])

home = ["Just do it right",
        "Make it perfect and real",
        "Because it's everything",
        "Yeah everything",
        "Was never the deal"]

lcd_sound = Song(home)

yung_lean.sing_me_a_song()

the_surf.sing_me_a_song()

lcd_sound.sing_me_a_song()

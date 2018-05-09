#Basic Object-Oriented Analysis and Design
# Working from the top down

from sys import exit
from random import randint
from textwrap import dedent

class Scene():

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1)

class Engine():

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "Your mother was a hampster and your father smelled of elderberries!",
        "Always look on the bright side of life *whistles*",
        "I fart in your general direction",
        "You died like Tommy Wiseau dies in 'The Room'",
        "You're tearing me apart Lisa!",
        "Words of encouragement are important!"
            ]
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Map():

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

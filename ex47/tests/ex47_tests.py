from nose.tools import *
import ex47.game import Room


def test_room():
    gold = Room("GoldRoom",
                """THis room has gold in it you can grab. There's a
                door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south =  Room("South", "Test roon in the south.")

    center.add_paths({'north': north, 'south': south})

    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def setup():
    print("SETUP!")

def teardown():
    print("TEARDOWN!")

def test_basic():
    print("I RAN!", end='')

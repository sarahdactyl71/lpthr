from nose.tools import *
import ex47.game import Room


def test_room():
    gold = Room("GoldRoom",
                """THis room has gold in it you can grab. There's a
                door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def setup():
    print("SETUP!")

def teardown():
    print("TEARDOWN!")

def test_basic():
    print("I RAN!", end='')

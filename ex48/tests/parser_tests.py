from nose.tools import *
from ex48 import parser

def test_peek():
    assert_equal(parser.peek([]), None)
    assert_equal(parser.peek([('noun', 'bear')]), 'noun')
    assert_equal(parser.peek([('verb', 'run')]), 'verb')

def test_match():
    assert_equal(parser.match(([('noun', 'bear'),
                               ('verb', 'run')]), 'noun'), ('noun', 'bear'))
    assert_equal(parser.match(([]), 'noun'), None)

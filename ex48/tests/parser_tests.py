from nose.tools import *
from ex48 import parser

def test_peek():
    assert_equal(parser.peek([]), None)
    assert_equal(parser.peek([('noun', 'bear')]), 'noun')
    assert_equal(parser.peek([('verb', 'run')]), 'verb')

def test_match():
    assert_equal(parser.match(([('noun', 'bear'),
                               ('verb', 'run')]), 'noun'), ('noun', 'bear'))
    assert_equal(parser.match(([('noun', 'badger'),
                               ('verb', 'run')]), 'noun'), ('noun', 'badger'))
    assert_equal(parser.match(([('noun', 'bear'),
                               ('verb', 'run')]), 'object'), None)
    assert_equal(parser.match(([]), 'noun'), None)

def test_parse_verbs():
    assert_equal(parser.parse_verb([('stop', 'the'), ('verb', 'run')]), ('verb', 'run'))
    assert_equal(parser.parse_verb([('stop', 'the'), ('verb', 'jump')]), ('verb', 'jump'))
    assert_equal(parser.parse_verb([('verb', 'jump'), ('noun', 'sword')]), ('verb', 'jump'))

def test_parse_objects():
    assert_equal(parser.parse_object([('stop', 'the'), ('noun', 'BMO')]), ('noun', 'BMO'))
    assert_equal(parser.parse_object([('stop', 'the'), ('noun', 'Lil Gideon')]), ('noun', 'Lil Gideon'))
    assert_equal(parser.parse_object([('stop', 'the'), ('direction', 'south')]), ('direction', 'south'))

def test_parse_subjects():
    assert_equal(parser.parse_subject([('stop', 'the'), ('noun', 'BMO')]), ('noun', 'BMO'))
    assert_equal(parser.parse_subject([('stop', 'the'), ('verb', 'jump')]), ('noun', 'player'))
    assert_equal(parser.parse_subject([('noun', 'BMO'), ('verb', 'jump')]), ('noun', 'BMO'))

def test_parse_sentence():
    a = parser.Sentence(('subject', 'sarah'), ('verb', 'play'), ('object', 'Scott'))
    assert_equal(a.subject, 'sarah')
    assert_equal(a.verb, 'play')
    assert_equal(a.object, 'Scott')

#FIVE TOOLS
#1) Way to loop through scanned words
#2) A way to match different types of tuples we expect in SubjectVerbObject setup
#3) A way to pee at potential tuple so we can make decisions
#4) A way to skip things we do not care about like stop words
#5) A sentence object to put the results in

class ParserError(Exception):
    pass

class Sentence(object):

    def __init__(self, subject, verb, object):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object =obj[1]

    def peek(word_list):
        if word_liest:
            word = word_list[0]
            retunr word[0]
        else:
            return None

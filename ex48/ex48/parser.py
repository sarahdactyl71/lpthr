#FIVE TOOLS
#1) Way to loop through scanned words
#2) A way to match different types of tuples we expect in SubjectVerbObject setup
#3) A way to pee at potential tuple so we can make decisions
#4) A way to skip things we do not care about like stop words
#5) A sentence object to put the results in

class ParserError(Exception):
    pass

lexicon = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',
    'west': 'direction',
    'go': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    }

def scan(phrase):
    words = phrase.split()
    output = []

    for word in words:
        checked_word = convert_numbers(word)

        if word in lexicon.keys():
            output.append((lexicon[word], checked_word))

    return output


def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return s

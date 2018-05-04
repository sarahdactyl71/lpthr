#imports sys
import sys

#args that we must add in order to run the file
script, input_encoding, error = sys.argv

#function that takes in a file, what kind of encoding it should have
#and errors
def main(language_file, encoding, errors):
    #reads a line of a particular file
    line = language_file.readline()

    if line:
        #if the line exists, print the line with the encoding and errors
        print_line(line, encoding, errors)
        #put it back to the function to do it again
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    #looks at stripped line and encodes it with the encoding and errors
    raw_bytes = next_lang.encode(encoding, errors=errors)
    #decodes the string with errors
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    #shows what the raw bytes are after encoding it from the input when
    #we ran the file, shows the decoded version and what they are
    #equivalent to
    print(raw_bytes, "<===>", cooked_string)

#the file that we want to process, and the endoding we want for it
languages = open("exercises/languages.txt", encoding="utf-8")

#runs through the entire process
main(languages, input_encoding, error)

#an example of how to run this is
#python exercises/ex22.py utf-8 strict
#this should essentially output a bunch of languages

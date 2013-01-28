import re

DIGITS = [str(x) for x in range(0,10)]

def strip_non_digit_characters(string):
    return clean_string(string, DIGITS)

def clean_price_string(string):
    return clean_string(string, DIGITS[:] + ["."])

def clean_string(string, legal_characters):
    new_string = ""
    for char in string:
        if char in legal_characters:
            new_string = new_string + char
    return new_string

def is_only_newline(line):
    return re.match("^\n", line)



class ParseError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)
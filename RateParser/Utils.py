import re

def strip_non_digit_characters(string):
    digits = [str(x) for x in range(0,10)]
    new_string = ""
    for char in string:
        if char in digits:
            new_string = new_string + char
    return new_string


def is_only_newline(line):
    return re.match("^\n", line)


class ParseError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)
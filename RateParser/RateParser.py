import argparse, re


def open_file(path):
    return open(path, 'r')


def parse_file(path):
    file = open_file(path)

    parse_lines(file)


def parse_lines(file):
    line_accumulator = None
    current_page_number = None
    for line in file:
        if not line_accumulator and is_only_newline(line): # Ignore lines when we have not identified a page.
            continue
        if is_line_start_of_new_page(line): # Start new accumulator if we have found the start of a new page.
            if line_accumulator:
                parse_page(current_page_number, line_accumulator)
            current_page_number = get_page_number(line)
            line_accumulator = []
        else:
            line_accumulator.append(line)


def is_only_newline(line):
    return re.match("^\n", line)


def is_line_start_of_new_page(line):
    return re.match("^NEW_PAGE.*", line)


def get_page_number(line):
    matches = re.search("^NEW_PAGE\s(\d+)", line)
    if not matches:
        raise ParseError("Could not find page number in string '" + line + "'")
    return int(matches.group(1))


def parse_page(page_number, lines):
    print str(page_number) + ": " + str(lines)


def parse_even_page(lines):
    pass

class ParseError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="RateParser")
    args = parser.parse_args()
    path = 'Datafiles/UPS_Next_Day_Air_Early_AM.txt'
    parse_file(path)
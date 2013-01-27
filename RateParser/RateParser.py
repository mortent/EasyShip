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
        if not line_accumulator and is_only_newline(line):
            continue
        if line_accumulator and not is_only_newline(line):
            parse_page(current_line_number, line_accumulator)
            line_accumulator = None
        if is_line_start_of_new_page(line):
            current_page_number = get_page_number(line)
            line_accumulator = []


def is_only_newline(line):
    return re.match("^\n", line)

def is_line_start_of_new_page(line):
    return re.match("^NEW_PAGE.*", line)

def get_page_number(line):
    matches = re.search("^NEW_PAGE\s(\d+)", line)
    if not matches:
        raise ParseError("Could not find page number in string '" + line + "'")
    return int(matches.group(1))


class ParseError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="RateParser")
    args = parser.parse_args()
    path = 'file.txt'
    parse_file(path)
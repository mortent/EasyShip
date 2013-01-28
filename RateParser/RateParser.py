import argparse, re

import EvenPageRateParser, OddPageRateParser, Utils


def open_file(path):
    return open(path, 'r')


def parse_file(path):
    file = open_file(path)

    parse_lines(file)


def parse_lines(file):
    line_accumulator = None
    current_page_number = None
    for line in file:
        if not line_accumulator and Utils.is_only_newline(line): # Ignore lines when we have not identified a page.
            continue
        if is_line_start_of_new_page(line): # Start new accumulator if we have found the start of a new page.
            if line_accumulator:
                parse_page(current_page_number, line_accumulator)
            current_page_number = get_page_number(line)
            line_accumulator = []
        else:
            line_accumulator.append(line)


def is_line_start_of_new_page(line):
    return re.match("^NEW_PAGE.*", line)


def get_page_number(line):
    matches = re.search("^NEW_PAGE\s(\d+)", line)
    if not matches:
        raise Utils.ParseError("Could not find page number in string '" + line + "'")
    return int(matches.group(1))


def parse_page(page_number, lines):
    if page_number %2 == 0:
        EvenPageRateParser.parse_even_page(lines)
    else:
        OddPageRateParser.parse_odd_page(lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="RateParser")
    args = parser.parse_args()
    path = 'Datafiles/UPS_Next_Day_Air_Early_AM.txt'
    parse_file(path)
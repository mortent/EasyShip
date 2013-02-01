import argparse, re

import PageRateParser, Utils


def open_file(path):
    """
    Open the file for reading.
    """
    return open(path, 'r')


def print_results_as_yaml(results, arguments):
    """
    Runs through all results and prints them to stdout.
    """
    for (counter, rate) in enumerate(results):
        print "- model: root.rate"
        print "  pk: " + str(arguments.pk + counter)
        print "  fields:"
        print "    weight: " + rate['weight']
        print "    service_level: " + str(arguments.service)
        print "    zone_number: " + rate['zone'].zfill(3)
        print "    price: " + rate['rate']


def parse_file(arguments):
    """
    Coordinating the parser. Opens the file, calls the parse method and then prints the results with the print_results_as_yaml method
    """
    file = open_file(arguments.file)
    results = []
    parse_lines(file, results)
    print_results_as_yaml(results, arguments)


def parse_lines(file, results):
    """
    Runs through the file and identifies when new pages start. Every time it finds the start of a new page, it
    creates an accumulator that collects all lines on the page and call the parse_page method.
    """
    line_accumulator = None
    for line in file:
        if not line_accumulator and Utils.is_only_newline(line): # Ignore lines when we have not identified a page.
            continue
        if is_line_start_of_new_page(line): # Start new accumulator if we have found the start of a new page.
            parse_page(line_accumulator, results)
            line_accumulator = []
        else:
            line_accumulator.append(line)
    else:
        parse_page(line_accumulator, results)


def is_line_start_of_new_page(line):
    return re.match("^NEW_PAGE.*", line)


def parse_page(lines, results):
    """
    Calls the PageRateParser if the page has lines on it.
    """
    if not lines:
        return
    PageRateParser.parse_page(lines, results)

# Main entry point to parser. Uses argparse to collect command line arguments.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="RateParser")
    parser.add_argument("file")
    parser.add_argument('-s', '--service', action="store", type=int, help="Service level id", required=True)
    parser.add_argument('-p', '--pk', action="store", default=1, type=int, help="Start value for primary key")
    args = parser.parse_args()
    parse_file(args)
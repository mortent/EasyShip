import argparse, re

import PageRateParser, Utils


def open_file(path):
    return open(path, 'r')


def print_results_as_yaml(results, arguments):
    for (counter, rate) in enumerate(results):
        print "- model: root.rate"
        print "  pk: " + str(arguments.pk + counter)
        print "  fields:"
        print "    weight: " + rate['weight']
        print "    service_level: " + str(arguments.service)
        print "    zone_number: " + rate['zone'].zfill(3)
        print "    price: " + rate['rate']


def parse_file(arguments):
    file = open_file(arguments.file)
    results = []
    parse_lines(file, results)
    print_results_as_yaml(results, arguments)


def parse_lines(file, results):
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
    if not lines:
        return
    PageRateParser.parse_page(lines, results)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="RateParser")
    parser.add_argument("file")
    parser.add_argument('-s', '--service', action="store", type=int, help="Service level id", required=True)
    parser.add_argument('-p', '--pk', action="store", default=1, type=int, help="Start value for primary key")
    args = parser.parse_args()
    parse_file(args)
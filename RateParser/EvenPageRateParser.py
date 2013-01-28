import re
import Utils as Utils

def parse_even_page(lines):
    weights = None
    column = []
    for line in lines:
        if Utils.is_only_newline(line): # No content in this line, it must separate two columns.
            if column and is_weight_column(column[0]):
                weights = parse_weight_column(column[1:])
            if column and not is_weight_column(column[0]):
                parse_data_rate_column(column, weights)
            column = []
        else:
            column.append(line)


def is_weight_column(line):
    return re.match("^Zones$", line)


def is_letter_weight(line):
    return re.match("^Letter.*", line)


def parse_data_rate_column(column, weights):
    zone = Utils.strip_non_digit_characters(column[0])
    for (counter, line) in enumerate(column[1:]):
        weight = weights[counter]
        rate = Utils.strip_non_digit_characters(line)
        print "Weight: " + weight + ", Rate: " + rate + ", Zone: " + zone


def parse_weight_column(column):
    weights = []
    for line in column:
        if is_letter_weight(line):
            weights.append("Letter")
        else:
            weights.append(Utils.strip_non_digit_characters(line))
    return weights

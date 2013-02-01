import re
import Utils as Utils

def parse_page(lines, results):
    """
    Find each column and identify if it is a column of weights or rates.
    """
    weights = None
    column = []
    for line in lines:
        if Utils.is_only_newline(line): # No content in this line, it must separate two columns.
            if column and is_weight_column(column[0]):
                weights = parse_weight_column(column[1:])
            if column and not is_weight_column(column[0]):
                parse_data_rate_column(column, weights, results)
            column = []
        else:
            column.append(line)
    else:
        parse_data_rate_column(column, weights, results)


def parse_data_rate_column(column, weights, results):
    """
    Parse a column of rates and connect them to the correct column.
    """
    zone = Utils.strip_non_digit_characters(column[0])
    for (counter, line) in enumerate(column[1:]):
        weight = weights[counter]
        rate = Utils.clean_price_string(line)
        results.append({"weight": weight, "zone": zone, "rate": rate})


def parse_weight_column(column):
    """
    Parse a column of weights and put them into a datastructure to be used by parse_data_rate_column
    """
    weights = []
    for line in column:
        if is_letter_weight(line):
            weights.append("Letter")
        else:
            weights.append(Utils.strip_non_digit_characters(line))
    return weights


def is_weight_column(line):
    return re.match("^Zones$", line)


def is_letter_weight(line):
    return re.match("^Letter.*", line)

import argparse

PARAMETERS = {
    "ground": {"index": 1, "service_level_id": str(1)},
    "3_day_select": {"index": 2, "service_level_id": str(2)},
    "2nd_day_air": {"index": 3, "service_level_id": str(3)},
    "2nd_day_air_am": {"index": 4, "service_level_id": str(4)},
    "Next_day_air_saver": {"index": 5, "service_level_id": str(5)},
    "Next_day_air": {"index": 6, "service_level_id": str(6)},
}


def open_file(path):
    return open(path, 'r')


def print_results_as_yaml(results):
    for (counter, zone) in enumerate(results):
        print "- model: root.zone"
        print "  pk: " + str(counter + 1)
        print "  fields:"
        print "    zip_code: " + zone["zip_code"]
        print "    service_level: " + zone["service_level"]
        print "    zone_number: " + zone["zone_number"]


def parse_file(arguments):
    file = open_file(arguments.file)
    results = parse_lines(file)
    print_results_as_yaml(results)


def parse_lines(file):
    results = []
    for line in file:
        if not line or line.startswith("ZIP"):
            continue
        line_values=line.split(',')
        first_value, second_value = split_zip_code(line_values[0])
        for zip_code in range(int(first_value),int(second_value)+1):
            for key in PARAMETERS:
                param = PARAMETERS[key]
                zone_number = line_values[param["index"]]
                if zone_number.isdigit():
                    results.append({"zip_code": str(zip_code).zfill(3), "service_level": param["service_level_id"],
                                "zone_number": line_values[param["index"]]})
    return results


def split_zip_code(string):
    values = string.split('-')
    if len(values) < 2:
        return [values[0],values[0]]
    return values


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="ZoneParser")
    parser.add_argument("file")
    args = parser.parse_args()
    parse_file(args)


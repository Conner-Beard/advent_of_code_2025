import os


def extract_valid_range(line):
    """
    create a range object from a string "<int>-<int>"
    :param line: line to parse
    :returns: range object of input string
    """
    split_line = line.strip().split('-')
    min = int(split_line[0])
    max = int(split_line[1])
    id_range = range(min, max+1)

    return id_range


def extract_id(line):
    """
    Parse an integer from a string
    :param line: string to parse
    :returns: int verson of the input string
    """
    return int(line.strip())


def generate_input(input_file):
    """
    This is a generator function

    :param input_file:
    :returns: generator, first item is a list of valid ids, next are ids one at
    a time
    """
    current_file_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file_path)
    input_file_path = f'{current_directory}/{input_file}'

    assert os.path.exists(input_file_path)

    with open(input_file_path, 'r') as file:
        lines = file.readlines()
        processing_ids = True
        valid_ids = []

        for line in lines:
            if line.strip() == '':
                processing_ids = False
                yield valid_ids

            elif processing_ids:
                valid_ids.append(extract_valid_range(line))

            elif not processing_ids:
                yield extract_id(line)


def check_valid(valid_ids, id):
    """
    Check if id is in a list of ranges, return True if found, else False
    :param valid_ids: list of range objects to search in
    :param id: int to search for
    """
    for id_range in valid_ids:
        if id in id_range:
            return True

    return False


def solve_part1(input_file):
    input = generate_input(input_file)
    total = 0

    valid_ids = next(input)

    for id in input:
        if check_valid(valid_ids, id):
            total = total + 1

    return total


def sort_by_start(ids):
    """
    Sort list of ranges by starting value ascending
    """
    sorted = []
    while len(ids) > 0:
        min_id = None
        min_index = None
        for index, id_range in enumerate(ids):
            if min_id is None:
                min_id = id_range.start
                min_index = index

            elif min_id > id_range.start:
                min_id = id_range.start
                min_index = index

        sorted.append(ids.pop(min_index))
    return sorted


def merge_ranges(range_1, range_2):
    """
    Merge two overlapping ranges
    """
    range_1_in_2 = (range_1.start in range_2) | (range_1.stop in range_2)
    range_2_in_1 = (range_2.start in range_1) | (range_2.stop in range_1)
    assert range_1_in_2 | range_2_in_1

    start = min(range_1.start, range_2.start)
    stop = max(range_1.stop, range_2.stop)

    return range(start, stop)


def optimize_valid_ids(valid_ids):
    """
    Take a list of ranges and remove/combine to elminate overlaps
    """
    sorted_ids = sort_by_start(valid_ids)

    previous_range = None
    optimized_ids = []
    for id_range in sorted_ids:
        if previous_range is None:
            previous_range = id_range
        elif id_range.start in previous_range:
            previous_range = merge_ranges(previous_range, id_range)
        elif id_range.start not in previous_range:
            optimized_ids.append(previous_range)
            previous_range = id_range

    optimized_ids.append(previous_range)

    return optimized_ids


def get_range_range(id_range):
    return id_range.stop - id_range.start


def count_valid_ids(ids):
    count = 0
    for id_range in ids:
        count = count + get_range_range(id_range)
    return count


def solve_part2(input_file):
    input = generate_input(input_file)

    valid_ids = next(input)

    optimized_ids = optimize_valid_ids(valid_ids)

    return count_valid_ids(optimized_ids)


if __name__ == '__main__':
    print(f'Solving {__file__}')

    # Part 1 Example
    value = solve_part1('example.example')
    assert value == 3

    # Part 1
    value = solve_part1('input.input')
    print(value)

    # Part 2 Example
    value = solve_part2('example.example')
    assert value == 14

    # Part 2
    value = solve_part2('input.input')
    print(value)

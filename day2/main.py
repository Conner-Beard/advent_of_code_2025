import os


def check_valid_input(string):
    """
    Check that input value matches the problem rules
    :input string: input value in the fromat '(int)-(int)'
    """
    split = string.split('-')

    assert len(split) == 2, 'Input is not a range'
    assert split[0][0] != '0', 'Range has leading zeros'
    assert split[1][0] != '0', 'Range has leading zeros'
    assert split[0].isdigit(), 'Range is not an int'
    assert split[1].isdigit(), 'Range is not an int'


def range_from_chunk(chunk):
    """
    Convert a text range in the format '(int)-(int)' to a python range object
    :input string: Range specifier '(int1)-(int2)'
    :returns: range(int1, int2+1)
    """
    split = chunk.split('-')
    return range(int(split[0]), int(split[1])+1)


def generate_input(input_file):
    """
    This is a generator function

    :input input_file:
    :output :
    """
    current_file_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file_path)
    input_file_path = f'{current_directory}/{input_file}'

    assert os.path.exists(input_file_path)

    with open(input_file_path, 'r') as file:
        for line in file.readlines():
            chunks = line.strip().split(',')
            for chunk in chunks:
                if chunk == '':
                    continue
                check_valid_input(chunk)

                chunk_range = range_from_chunk(chunk)
                yield chunk_range


def test_id_valid_part1(id):
    """
    Returns False for any integers made up of two repeating
    numbers, ex. 1212, 2222, 345345, ..., but not 121212
    :input id: integer to be tested
    :returns: True/False depending on check
    """
    id_str = str(id)
    length = len(id_str)

    # only even length numbers can be invalid
    if (length % 2) == 1:
        return True

    half = int(length/2)
    first_half = id_str[0:half]
    second_half = id_str[half:]
    if first_half == second_half:
        return False

    return True


def test_id_valid_part2(id):
    """
    Returns False for any integers made up of repeating
    numbers, ex. 121212, 12341234, 756756, ...
    :input id: integer to be tested
    :returns: True/False depending on check
    """
    id_str = str(id)
    length = len(id_str)

    pattern = ''
    for index, number in enumerate(id_str):
        if index+1 > (length/2 + 1):
            break
        if index+1 == length:
            break

        pattern = pattern + number

        times = length / len(pattern)

        if times.is_integer():
            if pattern*int(times) == id_str:
                return False
        else:
            continue

    return True


def solve_part1(input_file):
    inputs = generate_input(input_file)

    invalid_total = 0

    for id_range in inputs:
        for product_id in id_range:
            if test_id_valid_part1(product_id) is False:
                invalid_total = invalid_total + product_id

    return invalid_total


def solve_part2(input_file):
    inputs = generate_input(input_file)

    invalid_total = 0

    for id_range in inputs:
        for product_id in id_range:
            if test_id_valid_part2(product_id) is False:
                invalid_total = invalid_total + product_id

    return invalid_total


if __name__ == '__main__':
    print(f'Solving {__file__}')

    # Part 1 Example
    value = solve_part1('example.example')
    assert value == 1227775554

    # Part 1
    value = solve_part1('input.input')
    print(value)

    # Part 2 Example
    value = solve_part2('example.example')
    assert value == 4174379265

    # Part 2
    value = solve_part2('input.input')
    print(value)

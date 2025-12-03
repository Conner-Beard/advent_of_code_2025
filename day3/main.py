import os


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
            bank_str = line.strip()
            yield [int(i) for i in bank_str]


def find_largest_two(bank):
    """
    find the two numbers in a list of ints that
    produce the largest total value when combined
    sequentialy
    :input bank: list of ints
    :output total: largest combo of two ints in sequence
    """
    largest = 0
    for base_index, battery in enumerate(bank):
        base = battery * 10
        for battery in bank[base_index+1:]:
            total = base + battery
            if total > largest:
                largest = total
    return largest


def merge_sequence(sequence):

    string = ''.join([str(i) for i in sequence])

    return int(string)


def find_largest_x(x, bank, debug=False):
    """
    find the x numbers in a list of ints that
    produce the largest total value when combined
    sequentialy
    :input bank: list of ints
    :output total: largest combo of x ints in sequence
    """
    # index, number
    sorted = [(-1, 0)]

    if debug:
        print(''.join([str(i) for i in bank]))

    for digit in range(x):
        start = sorted[-1][0] + 1
        end = len(bank) - x + digit

        top_pair = (None, 0)
        for index, number in enumerate(bank):
            # already narrowed
            if index < start:
                continue
            # impossible to make an x digit number
            if index > end:
                break

            if number > top_pair[1]:
                top_pair = (index, number)

        if top_pair[0] is None:
            raise Exception("Top pair not found!")

        if debug:
            print(' ' * top_pair[0] + '^')
        sorted.append(top_pair)

    # first element is a dummy, pop it
    sorted.pop(0)

    assert len(sorted) == x

    total = merge_sequence([i[1] for i in sorted])

    return total


def solve_part1(input_file):
    banks = generate_input(input_file)

    total = 0
    for bank in banks:
        largest = find_largest_x(2, bank)
        total = total + largest

    return total


def solve_part2(input_file):
    banks = generate_input(input_file)

    total = 0
    for bank in banks:
        largest = find_largest_x(12, bank)
        total = total + largest

    return total


if __name__ == '__main__':
    print(f'Solving {__file__}')

    # Part 1 Example
    value = solve_part1('example.example')
    assert value == 357

    # Part 1
    value = solve_part1('input.input')
    print(value)

    # Part 2 Example
    value = solve_part2('example.example')
    assert value == 3121910778619

    # Part 2
    value = solve_part2('input.input')
    print(value)

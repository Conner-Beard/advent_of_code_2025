import os


def parse_row(row_str):

    # list bounded by dead space
    row = ['x'] + list(row_str.strip()) + ['x']

    return row


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
        start_row = parse_row(file.readline())
        empty_row = parse_row('x' * (len(start_row) - 2))
        previous_row = empty_row
        current_row = empty_row
        next_row = start_row

        for line in file.readlines():
            previous_row = current_row
            current_row = next_row
            next_row = parse_row(line)

            yield [previous_row, current_row, next_row]

        previous_row = current_row
        current_row = next_row
        next_row = empty_row
        yield [previous_row, current_row, next_row]


def solve_part1(input_file):
    shelves = generate_input(input_file)

    total = 0
    for shelf in shelves:
        current_shelf = shelf[1]

        for column, item in enumerate(current_shelf):
            if item == '@':
                columns = slice(column-1, column+2)
                adjacent_items = []
                for row in shelf:
                    adjacent_items = adjacent_items + row[columns]

                adjacent_paper = [x for x in adjacent_items if x == '@']

                if (len(adjacent_paper)-1) < 4:
                    total = total + 1

    return total

def solve_part2(input_file):
    """
    Way too slow!

    don't store removed paper as a list, feed it back in as
    a new input.
    """

    total = 0
    iterations = 0
    removed_paper = []

    repeat_flag = True
    while repeat_flag is True:
        iterations = iterations + 1
        repeat_flag = False
        removed_paper_current = []

        shelves = generate_input(input_file)
        for shelf_index, shelf in enumerate(shelves):

            for index, row in enumerate(shelf):
                real_shelf_index = shelf_index - 1 + index

                for column, value in enumerate(row):
                    if (real_shelf_index, column) in removed_paper:
                        shelf[index][column] = '~'

            current_shelf = shelf[1]

            for column, item in enumerate(current_shelf):
                if item == '@':
                    adjacent_paper = 0
                    for row in shelf:
                        for adjacent_col in [column-1, column, column+1]:
                            if row[adjacent_col] == '@':
                                adjacent_paper = adjacent_paper + 1

                    if (adjacent_paper-1) < 4:
                        repeat_flag = True
                        removed_paper_current.append((shelf_index, column))
                        total = total + 1

        removed_paper = removed_paper + removed_paper_current

        print(iterations)
        print(len(removed_paper_current))

    return total




if __name__ == '__main__':
    print(f'Solving {__file__}')

    # Part 1 Example
    value = solve_part1('example.example')
    assert value == 13

    # Part 1
    value = solve_part1('input.input')
    print(value)

    # Part 2 Example
    value = solve_part2('example.example')
    assert value == 43

    # Part 2
    value = solve_part2('input.input')
    print(value)

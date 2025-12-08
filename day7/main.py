import os


def generate_input(input_file):
    """
    This is a generator function

    :param input_file:
    :returns:
    """
    current_file_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file_path)
    input_file_path = f'{current_directory}/{input_file}'

    assert os.path.exists(input_file_path)

    first_line = True

    with open(input_file_path, 'r') as file:
        for line in file:
            line_list = list(line.strip())
            line_list = ['x', *line_list, 'x']

            if first_line:
                yield ['x' for x in line_list]
                first_line = False

            yield line_list
    yield ['x' for x in line_list]


def process_row(input_row=None, row=None):
    """
    Take the state of the input row and use it to transoform the given row
    based on the puzzle rules
    """
    split_counter = 0
    if input_row is None:
        return split_counter, row
    # new_row is transformed version of row given input_row
    new_row = [column for column in row]
    for column, entity in enumerate(input_row):
        # source beam
        if entity == 'S':
            new_row[column] = '|'
        # extend beam
        elif entity == '|':
            # split beam
            if row[column] == '^':
                split_counter = split_counter + 1
                new_row[column-1] = '|'
                new_row[column+1] = '|'
            # extend beam
            else:
                new_row[column] = '|'
        elif entity == '.':
            if row[column] == '^':
                new_row[column] = '.'

    return split_counter, new_row


def solve_part1(input_file):
    input = generate_input(input_file)

    previous_row = None
    total = 0
    for row in input:
        split_count, new_row = process_row(previous_row, row)
        previous_row = new_row
        total = total + split_count
    return total


class SplitterMap():
    def __init__(self, file):

        self.read_map(file)

    def read_map(self, file):
        input = generate_input(file)

        self.map = []
        for row_num, row in enumerate(input):
            self.map.append(row)
            for column_num, entity in enumerate(row):
                if entity == 'S':
                    self.start = (row_num, column_num)

    def get_entity(self, coordinate):
        return self.map[coordinate[0]][coordinate[1]]

found_count = 0

def send_beam(coordinate, direction='L', map=None):
    next_entity = map.get_entity((coordinate[0]+1, coordinate[1]))
    global found_count

    # split
    if next_entity == '^':
        # split left
        if direction == 'L':
            next_beam = (coordinate[0]+1, coordinate[1]-1)
        # split rigth
        elif direction == 'R':
            next_beam = (coordinate[0]+1, coordinate[1]+1)

    # don't split
    elif next_entity == '.':
        next_beam = (coordinate[0]+1, coordinate[1])
    # found end
    elif next_entity == 'x':
        found_count = found_count + 1
        return True

    for direction in ['L', 'R']:
        send_beam(next_beam, direction=direction, map=map)


def solve_part2(input_file):
    map = SplitterMap(input_file)
    global found_count

    print(map.map)

    print(map.get_entity(map.start))

    for direction in ['L', 'R']:
        send_beam(map.start, direction=direction, map=map)

    print(found_count)


if __name__ == '__main__':
    print(f'Solving {__file__}')

    # Part 1 Example
    value = solve_part1('example.example')
    assert value == 21

    # # Part 1
    # value = solve_part1('input.input')
    # print(value)

    # Part 2 Example
    value = solve_part2('example.example')
    assert value == 40

    # # Part 2
    # value = solve_part2('input.input')
    # print(value)

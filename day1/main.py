import os


class Lock():
    """
    A 100 state combinational lock that starts at position 50
    contains numbers 0-99 and wraps around
    rotating left decreases the number
    rotating right increases the number
    """
    def __init__(self):
        self.state = 50

    def rotate_left(self):
        self.state = self.state - 1

        if self.state < 0:
            self.state = 99

    def rotate_right(self):
        self.state = self.state + 1

        if self.state > 99:
            self.state = 0


def generate_input(input_file):
    """
    This is a generator function

    Extract input from a text file in the form of direction, step size pairs
    :input input_file: Puzzle input in the form of direction, step size pairs
    :output (direction, step): direction one of 'L', 'R', step any positive
    integer
    """
    current_file_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file_path)
    input_file_path = f'{current_directory}/{input_file}'

    assert os.path.exists(input_file_path)

    with open(input_file_path, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            direction = line[0]
            step = int(line[1:])
            yield (direction, step)


def solve_part1(input_file):
    """
    Count the number of times Lock lands on 0 when stimulated with an input
    file.
    :input input_file: Puzzle input in the form of direction, step size pairs
    """
    lock = Lock()
    password_counter = 0

    input = generate_input(input_file)

    for direction, step in input:
        for _ in range(step):
            if direction == 'R':
                lock.rotate_right()
            elif direction == 'L':
                lock.rotate_left()

        if lock.state == 0:
            password_counter = password_counter + 1

    return password_counter


def solve_part2(input_file):
    """
    Count the number of times Lock passes 0 when stimulated with an input
    file.
    :input input_file: Puzzle input in the form of direction, step size pairs
    """
    lock = Lock()
    password_counter = 0

    input = generate_input(input_file)

    for direction, step in input:
        for _ in range(step):
            if direction == 'R':
                lock.rotate_right()
            elif direction == 'L':
                lock.rotate_left()
            else:
                raise Exception("Lock must rotate in a direction!")

            if lock.state == 0:
                password_counter = password_counter + 1

    return password_counter


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
    assert value == 6

    # Part 2
    value = solve_part2('input.input')
    print(value)

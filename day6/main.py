import os


def addition_operator(*args):
    total = 0
    for number in args:
        assert type(number) is int

        total = total + number

    return total


def multiplication_operator(*args):
    total = 1
    for number in args:
        assert type(number) is int

        total = total * number

    return total


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

    with open(input_file_path, 'r') as file:
        all_operands = []
        for line in file:
            row = line.strip().split()

            if row[0].strip().isdigit():
                all_operands.append(row)
            else:
                all_operators = row
                break

    for index, operator in enumerate(all_operators):
        if operator.strip() == '+':
            operation = addition_operator
        elif operator.strip() == '*':
            operation = multiplication_operator
        else:
            raise Exception(f'Unrecognized operator {operator}')

        operands = []
        for row in all_operands:
            operands.append(int(row[index].strip()))

        yield operands, operation


def solve_part1(input_file):
    input = generate_input(input_file)

    total = 0
    for operands, operator in input:
        total = total + operator(*operands)

    return total


def generate_input_2(input_file):
    """
    This is a generator function

    :param input_file:
    :returns:
    """
    current_file_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file_path)
    input_file_path = f'{current_directory}/{input_file}'

    assert os.path.exists(input_file_path)

    with open(input_file_path, 'r') as file:
        lines = file.readlines()

        max_length = 0
        for index, line in enumerate(lines):
            line = line.replace('\n', '')

            if len(line) > max_length:
                max_length = len(line)

            lines[index] = line

        # match line lengths and terminate with an 'x'
        for index, line in enumerate(lines):
            if len(line) != max_length:
                line = line + ' ' * (max_length - len(line))
            line = line + 'x'

            lines[index] = line

        numbers = []
        for index, line in enumerate(lines[0]):

            chars = []
            for char_lines in lines[0:-1]:
                chars.append(char_lines[index])

            operator = lines[-1][index]

            if operator in ['+']:
                current_operator = addition_operator
            elif operator in ['*']:
                current_operator = multiplication_operator

            if all([char == ' ' for char in [*chars, operator]]):
                yield numbers, current_operator
                numbers = []
            elif all([char == 'x' for char in [*chars, operator]]):
                yield numbers, current_operator
            else:
                numbers.append([*chars])


def solve_part2(input_file):
    input = generate_input_2(input_file)

    total = 0
    for numbers, operator in input:
        result = operator(*[int(''.join(number).strip())
                            for number in numbers])

        total = total + result

    return total


if __name__ == '__main__':
    print(f'Solving {__file__}')

    # Part 1 Example
    value = solve_part1('example.example')
    assert value == 4277556

    # Part 1
    value = solve_part1('input.input')
    print(value)

    # Part 2 Example
    value = solve_part2('example.example')
    assert value == 3263827

    # Part 2
    value = solve_part2('input.input')
    print(value)

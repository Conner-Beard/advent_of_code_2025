from .. import main


def test_generate_input():
    for file in ["example.example", "input.input"]:
        input = main.generate_input(file)
        valid_ids = next(input)

        # check that valid_ids is a list of ranges
        for valid_id in valid_ids:
            assert isinstance(valid_id, range)

        # check that ids are positive integers
        for id in input:
            assert type(id) is int
            assert id > 0

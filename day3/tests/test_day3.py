from .. import main


def test_generate_input():
    """
    Verify input file is parsed correctly
    """
    for file in ['example.example', 'input.input']:
        inputs = main.generate_input(file)

        for input in inputs:
            for i in input:
                assert type(i) is int
                assert i > 0


def test_find_largest_two():
    """
    Verify largest two numbers are found
    """
    assert 34 == main.find_largest_two([1,2,3,4])
    assert 19 == main.find_largest_two([1,1,1,9])
    assert 89 == main.find_largest_two([8,1,1,9])
    assert 92 == main.find_largest_two([8,1,9,2])


def test_merge_sequence():
    """
    Check list merging
    """
    assert 1234 == main.merge_sequence([1,2,3,4])


def test_find_largest_x():
    """
    Verify largest x numbers are found
    """
    assert 34 == main.find_largest_x(2, [1,2,3,4])
    assert 19 == main.find_largest_x(2, [1,1,1,9])
    assert 89 == main.find_largest_x(2, [8,1,1,9])
    assert 92 == main.find_largest_x(2, [8,1,9,2])

    assert 234 == main.find_largest_x(3, [1,2,3,4])
    assert 119 == main.find_largest_x(3, [1,1,1,9])
    assert 819 == main.find_largest_x(3, [8,1,1,9])
    assert 892 == main.find_largest_x(3, [8,1,9,2])

from .. import main


def test_lock():
    """
    Test the lock operates as expected
    """
    lock = main.Lock()

    assert lock.state == 50

    initial_state = lock.state
    for i in range(1000):
        target_value = (initial_state + i + 1) % 100
        lock.rotate_right()

        assert lock.state == target_value

    initial_state = lock.state
    for i in range(1000):
        target_value = (initial_state - i - 1) % 100
        lock.rotate_left()

        assert lock.state == target_value


def test_generate_input():
    """
    Test input parser generates data in the correct format
    """
    files = ['example.example', 'input.input']
    for file in files:
        for direction, value in main.generate_input(file):
            assert direction in ['L', 'R']
            assert type(value) is int
            assert value > -1

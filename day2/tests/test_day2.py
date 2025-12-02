from .. import main
import pytest


def test_generate_input():
    inputs = main.generate_input('example.example')
    for input in inputs:
        assert type(input) is range



def test_check_valid_input():
    """
    Test some possible invalid inputs against input checker
    """
    with pytest.raises(AssertionError):
        main.check_valid_input('')

    with pytest.raises(AssertionError):
        main.check_valid_input('010-10')

    with pytest.raises(AssertionError):
        main.check_valid_input('-010-10')

    with pytest.raises(AssertionError):
        main.check_valid_input(' 010-10')

    main.check_valid_input('1-10')


def test_range_from_chunk():
    """
    Test that range object is correctly generated
    """

    with pytest.raises(AssertionError):
        assert main.range_from_chunk('12-40') == range(12, 40)

    assert main.range_from_chunk('12-40') == range(12, 41)

    for i in main.range_from_chunk('12-40'):
        ...


def test_test_id_valid_part1():
    """
    Test that the id checker only passes valid ids
    """
    assert main.test_id_valid_part1('11') is False
    assert main.test_id_valid_part1('22') is False
    assert main.test_id_valid_part1('99') is False
    assert main.test_id_valid_part1('1010') is False
    assert main.test_id_valid_part1('1188511885') is False
    assert main.test_id_valid_part1('222222') is False
    assert main.test_id_valid_part1('446446') is False
    assert main.test_id_valid_part1('38593859') is False

    assert main.test_id_valid_part1('1234') is True


def test_test_id_valid_part2():
    """
    Test that the id checker only passes valid ids
    """
    assert main.test_id_valid_part2('11') is False
    assert main.test_id_valid_part2('22') is False
    assert main.test_id_valid_part2('99') is False
    assert main.test_id_valid_part2('999') is False
    assert main.test_id_valid_part2('1010') is False
    assert main.test_id_valid_part2('1188511885') is False
    assert main.test_id_valid_part2('222222') is False
    assert main.test_id_valid_part2('446446') is False
    assert main.test_id_valid_part2('38593859') is False
    assert main.test_id_valid_part2('565656') is False
    assert main.test_id_valid_part2('824824824') is False
    assert main.test_id_valid_part2('2121212121') is False

    assert main.test_id_valid_part2('1234') is True

from .. import main


def test_operator():
    func = main.multiplication_operator

    assert func(1, 2, 3) == 1*2*3

    func = main.addition_operator

    assert func(1, 2, 3) == 1+2+3


#def test_generate_input():
#
#    for file in ['example.example', 'input.input']:
#        inputs = main.generate_input(file)
#
#        for operands, operation in inputs:
#            for operand in operands:
#                assert type(operand) is int

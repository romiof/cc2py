#import pytest

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#@pytest.mark.parametrize("n, valor_esperado", [
#        (4, 3),
#        (2, 1),
#        (5, 5)
#        ])
#
#def test_f(n, valor_esperado):
#    assert fibonacci(n) == valor_esperado


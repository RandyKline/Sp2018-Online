"""
test_generator.py

tests the solution to the generator lab

can be run with py.test or nosetests
"""
from unittest import TestCase
import generator_solution as gen

class GeneratorTest(TestCase):
    def test_intsum(self):

        g = gen.intsum(10)

        assert next(g) == 0
        assert next(g) == 1
        assert next(g) == 3
        assert next(g) == 6
        assert next(g) == 10
        assert next(g) == 15


    def test_doubler(self):

        g = gen.doubler(1000)

        assert next(g) == 1
        assert next(g) == 2
        assert next(g) == 4
        assert next(g) == 8
        assert next(g) == 16
        assert next(g) == 32

        for i in range(100):
            j = next(g)

        assert j == 2**15


    def test_fib(self):
        g = gen.fib(100)
        assert [next(g) for i in range(9)] == [1, 1, 2, 3, 5, 8, 13, 21, 34]


    def test_prime(self):
        g = gen.prime(100)
        for val in [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
            assert next(g) == val

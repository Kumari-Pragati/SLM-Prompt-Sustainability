import unittest
from mbpp_445_code import index_multiplication

class TestIndexMultiplication(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(index_multiplication((1, 2), (3, 4)), ((1*3, 1*4), (2*3, 2*4)))

    def test_empty_inputs(self):
        self.assertEqual(index_multiplication((), ()), ())
        self.assertEqual(index_multiplication((1, 2), ()), ())
        self.assertEqual(index_multiplication((), (1, 2)), ())

    def test_single_element_tuples(self):
        self.assertEqual(index_multiplication((1,), (2,)), ((1*2),))
        self.assertEqual(index_multiplication((1, 2), (3,)), ((1*3), (2*3)))

    def test_negative_numbers(self):
        self.assertEqual(index_multiplication((-1, 2), (3, 4)), ((-1*3, -1*4), (2*3, 2*4)))

    def test_zero(self):
        self.assertEqual(index_multiplication((0, 2), (3, 4)), ((0*3, 0*4), (2*3, 2*4)))

    def test_large_numbers(self):
        self.assertEqual(index_multiplication((100, 200), (300, 400)), ((100*300, 100*400), (200*300, 200*400)))

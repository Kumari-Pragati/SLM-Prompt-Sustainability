import unittest
from mbpp_445_code import index_multiplication

class TestIndexMultiplication(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(index_multiplication((1, 2, 3), (4, 5, 6)), ((4, 10, 18),))

    def test_edge_conditions(self):
        self.assertEqual(index_multiplication((), ()), ())
        self.assertEqual(index_multiplication((1,), (1,)), ((1,)))
        self.assertEqual(index_multiplication((1, 2, 3), (0, 0, 0)), ((0, 0, 0),))

    def test_complex_cases(self):
        self.assertEqual(index_multiplication((-1, 2, -3), (4, -5, 6)), ((-4, -10, -18),))
        self.assertEqual(index_multiplication((1, 2, 3), (10, 20, 30)), ((10, 40, 90),))

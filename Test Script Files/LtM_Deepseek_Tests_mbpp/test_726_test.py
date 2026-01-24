import unittest
from mbpp_726_code import multiply_elements

class TestMultiplyElements(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(multiply_elements((1, 2, 3)), (2, 6))

    def test_edge_conditions(self):
        self.assertEqual(multiply_elements((1,)), ())
        self.assertEqual(multiply_elements(()), ())

    def test_complex_cases(self):
        self.assertEqual(multiply_elements((0, 1, 2, 3)), (0, 2, 6))
        self.assertEqual(multiply_elements((-1, 1, -1, 1)), (1, -1))

import unittest
from mbpp_798_code import _sum

class TestSumFunction(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(_sum([1, 2, 3, 4, 5]), 15)

    def test_edge_cases(self):
        self.assertEqual(_sum([-1, 2, 3, 4, 5]), 13)
        self.assertEqual(_sum([1, 2, 3, -4, 5]), 7)
        self.assertEqual(_sum([1, 2, -3, 4, 5]), 9)

    def test_empty_input(self):
        self.assertEqual(_sum([]), 0)

    def test_single_element_input(self):
        self.assertEqual(_sum([10]), 10)

    def test_negative_numbers(self):
        self.assertEqual(_sum([-1, -2, -3, -4, -5]), -15)

    def test_mixed_numbers(self):
        self.assertEqual(_sum([1, 2, -3, 4, 5]), 9)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            _sum("Invalid input")

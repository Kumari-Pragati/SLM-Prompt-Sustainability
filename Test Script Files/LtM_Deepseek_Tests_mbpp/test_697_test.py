import unittest
from mbpp_697_code import count_even

class TestCountEven(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(count_even([1, 2, 3, 4]), 2)
        self.assertEqual(count_even([2, 4, 6, 8]), 4)
        self.assertEqual(count_even([1, 3, 5, 7]), 0)

    def test_edge_conditions(self):
        self.assertEqual(count_even([]), 0)
        self.assertEqual(count_even([0]), 1)
        self.assertEqual(count_even([-1, -2, -3, -4]), 2)

    def test_boundary_conditions(self):
        self.assertEqual(count_even([-2147483648]), 1)  # Minimum integer value
        self.assertEqual(count_even([2147483647]), 0)   # Maximum integer value

    def test_complex_cases(self):
        self.assertEqual(count_even([-1, -2, -3, -4, 0]), 3)
        self.assertEqual(count_even([10, 20, 30, 40, 50]), 5)
        self.assertEqual(count_even([1, 3, 5, 7, 9]), 0)

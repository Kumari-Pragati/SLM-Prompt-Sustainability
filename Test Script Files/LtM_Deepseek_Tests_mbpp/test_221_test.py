import unittest
from mbpp_221_code import first_even

class TestFirstEven(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(first_even([1, 2, 3]), 2)
        self.assertEqual(first_even([2, 3, 4]), 2)
        self.assertEqual(first_even([1, 3, 5]), -1)

    def test_edge_conditions(self):
        self.assertEqual(first_even([]), -1)
        self.assertEqual(first_even([1]), -1)
        self.assertEqual(first_even([1, 3, 5, 7, 9]), -1)
        self.assertEqual(first_even([2]), 2)

    def test_complex_cases(self):
        self.assertEqual(first_even([1, 3, 5, 7, 9, 10]), 10)
        self.assertEqual(first_even([1, 3, 5, 7, 9, 11, 12]), 12)

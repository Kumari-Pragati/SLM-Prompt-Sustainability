import unittest
from mbpp_221_code import first_even

class TestFirstEven(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(first_even([1, 2, 3, 4]), 2)
        self.assertEqual(first_even([2, 4, 6, 8]), 2)
        self.assertEqual(first_even([1, 3, 5, 7]), -1)

    def test_edge_cases(self):
        self.assertEqual(first_even([]), -1)
        self.assertEqual(first_even([1]), -1)
        self.assertEqual(first_even([1, 3, 5, 7, 9]), -1)

    def test_boundary_cases(self):
        self.assertEqual(first_even([0]), 0)
        self.assertEqual(first_even([2, 0]), 2)
        self.assertEqual(first_even([1, 3, 5, 7, 9, 11]), -1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            first_even(123)
        with self.assertRaises(TypeError):
            first_even('123')
        with self.assertRaises(TypeError):
            first_even(None)

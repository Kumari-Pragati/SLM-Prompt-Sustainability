import unittest
from mbpp_221_code import first_even

class TestFirstEven(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(first_even([1, 2, 3, 4]), 2)

    def test_edge_condition(self):
        self.assertEqual(first_even([]), -1)

    def test_boundary_condition(self):
        self.assertEqual(first_even([1]), -1)
        self.assertEqual(first_even([2]), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            first_even('1234')
        with self.assertRaises(TypeError):
            first_even(1234)

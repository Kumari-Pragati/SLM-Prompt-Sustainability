import unittest
from mbpp_697_code import count_even

class TestCountEven(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_even([1, 2, 3, 4, 5, 6]), 3)

    def test_edge_condition(self):
        self.assertEqual(count_even([2]), 1)
        self.assertEqual(count_even([1]), 0)

    def test_boundary_condition(self):
        self.assertEqual(count_even([]), 0)
        self.assertEqual(count_even([2, 2, 2, 2]), 4)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_even("1, 2, 3, 4, 5, 6")
        with self.assertRaises(TypeError):
            count_even(123456)

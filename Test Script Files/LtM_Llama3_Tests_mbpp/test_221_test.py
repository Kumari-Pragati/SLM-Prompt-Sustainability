import unittest
from mbpp_221_code import first_even

class TestFirstEven(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(first_even([2, 4, 6, 8]), 2)
        self.assertEqual(first_even([10, 12, 14, 16]), 10)
        self.assertEqual(first_even([2, 4, 6, 8, 10, 12, 14, 16]), 2)

    def test_edge(self):
        self.assertEqual(first_even([]), -1)
        self.assertEqual(first_even([1, 3, 5, 7]), -1)
        self.assertEqual(first_even([2, 4, 6, 8, 10, 12, 14, 16, 18]), 2)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            first_even("abc")
        with self.assertRaises(TypeError):
            first_even(None)

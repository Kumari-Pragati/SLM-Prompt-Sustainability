import unittest
from mbpp_221_code import first_even

class TestFirstEven(unittest.TestCase):

    def test_first_even_positive(self):
        self.assertEqual(first_even([1, 3, 5, 4, 2]), 2)

    def test_first_even_negative(self):
        self.assertEqual(first_even([1, 3, 5, 7]), -1)

    def test_first_even_empty(self):
        self.assertEqual(first_even([]), -1)

    def test_first_even_mixed(self):
        self.assertEqual(first_even([1, 3, 5, 0]), 0)

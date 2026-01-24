import unittest
from mbpp_250_code import count_X

class TestCountX(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_X((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 5), 1)

    def test_no_occurrence(self):
        self.assertEqual(count_X((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 11), 0)

    def test_empty_tuple(self):
        self.assertEqual(count_X((), 5), 0)

    def test_single_element_tuple(self):
        self.assertEqual(count_X((5,), 5), 1)
        self.assertEqual(count_X((5,), 6), 0)

    def test_multiple_occurrences(self):
        self.assertEqual(count_X((1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10), 5), 3)

    def test_negative_numbers(self):
        self.assertEqual(count_X((1, -2, 3, -4, 5, -5, 6, -7, 8, -9, 10), -5), 1)

    def test_zero(self):
        self.assertEqual(count_X((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 0), 1)

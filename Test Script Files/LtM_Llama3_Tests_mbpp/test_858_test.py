import unittest
from mbpp_858_code import count_list

class TestCountList(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_list([1, 2, 3]), 9)
        self.assertEqual(count_list([5, 5, 5]), 25)
        self.assertEqual(count_list([10, 10, 10, 10]), 100)

    def test_empty_list(self):
        self.assertEqual(count_list([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count_list([1]), 1)

    def test_large_list(self):
        self.assertEqual(count_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 100)

    def test_negative_numbers(self):
        self.assertEqual(count_list([-1, -2, -3]), 9)

    def test_mixed_numbers(self):
        self.assertEqual(count_list([1, 2, -3, 4]), 25)

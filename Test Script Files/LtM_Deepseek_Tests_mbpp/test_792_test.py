import unittest
from mbpp_792_code import count_list

class TestCountList(unittest.TestCase):
    def test_simple_list(self):
        self.assertEqual(count_list([1, 2, 3]), 3)

    def test_empty_list(self):
        self.assertEqual(count_list([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count_list([42]), 1)

    def test_large_list(self):
        self.assertEqual(count_list(list(range(1, 1001))), 1000)

    def test_list_with_duplicates(self):
        self.assertEqual(count_list([1, 2, 2, 3, 3, 3]), 6)

    def test_list_with_negative_numbers(self):
        self.assertEqual(count_list([-1, -2, -3]), 3)

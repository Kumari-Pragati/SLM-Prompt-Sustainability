import unittest
from mbpp_62_code import smallest_num

class TestSmallestNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(smallest_num([1, 2, 3, 4, 5]), 1)

    def test_empty_list(self):
        self.assertEqual(smallest_num([]), None)

    def test_single_element_list(self):
        self.assertEqual(smallest_num([4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(smallest_num([-1, -2, -3]), -3)

    def test_duplicates(self):
        self.assertEqual(smallest_num([1, 1, 2, 3]), 1)

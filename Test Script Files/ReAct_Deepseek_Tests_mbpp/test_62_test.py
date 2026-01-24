import unittest
from mbpp_62_code import smallest_num

class TestSmallestNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(smallest_num([5, 3, 9, 1]), 1)

    def test_single_element(self):
        self.assertEqual(smallest_num([7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(smallest_num([-2, -1, -5]), -5)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            smallest_num([])

    def test_duplicate_smallest(self):
        self.assertEqual(smallest_num([2, 3, 1, 1]), 1)

    def test_large_numbers(self):
        self.assertEqual(smallest_num([1000000, 2000000, 3000000]), 1000000)

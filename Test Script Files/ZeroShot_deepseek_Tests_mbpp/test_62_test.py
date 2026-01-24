import unittest
from mbpp_62_code import smallest_num

class TestSmallestNum(unittest.TestCase):

    def test_smallest_num_positive_numbers(self):
        self.assertEqual(smallest_num([3, 2, 1]), 1)

    def test_smallest_num_negative_numbers(self):
        self.assertEqual(smallest_num([-3, -2, -1]), -3)

    def test_smallest_num_mixed_numbers(self):
        self.assertEqual(smallest_num([-3, 2, 1]), -3)

    def test_smallest_num_single_number(self):
        self.assertEqual(smallest_num([5]), 5)

    def test_smallest_num_empty_list(self):
        with self.assertRaises(ValueError):
            smallest_num([])

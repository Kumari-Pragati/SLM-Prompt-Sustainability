import unittest
from mbpp_572_code import two_unique_nums

class TestTwoUniqueNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(two_unique_nums([1, 2, 3, 2, 1]), [3])

    def test_empty_list(self):
        self.assertEqual(two_unique_nums([]), [])

    def test_all_unique_numbers(self):
        self.assertEqual(two_unique_nums([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_all_duplicate_numbers(self):
        self.assertEqual(two_unique_nums([1, 1, 1, 1, 1]), [])

    def test_single_number(self):
        self.assertEqual(two_unique_nums([1]), [1])

    def test_negative_numbers(self):
        self.assertEqual(two_unique_nums([-1, -2, -1]), [-2])

    def test_zero(self):
        self.assertEqual(two_unique_nums([0, 0, 1]), [1])

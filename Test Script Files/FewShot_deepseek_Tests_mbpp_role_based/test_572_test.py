import unittest
from mbpp_572_code import two_unique_nums

class TestTwoUniqueNums(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(two_unique_nums([1, 2, 1, 3, 2, 5]), [3, 5])

    def test_empty_list(self):
        self.assertEqual(two_unique_nums([]), [])

    def test_single_element(self):
        self.assertEqual(two_unique_nums([1]), [1])

    def test_all_duplicates(self):
        self.assertEqual(two_unique_nums([1, 1, 1, 1]), [])

    def test_large_list(self):
        self.assertEqual(two_unique_nums(list(range(1, 1001)) + list(range(1, 1001))), list(range(1, 1001)))

    def test_negative_numbers(self):
        self.assertEqual(two_unique_nums([-1, -1, 1, 1, 2, 2]), [-1, 1, 2])

    def test_zero(self):
        self.assertEqual(two_unique_nums([0, 0, 1, 1]), [0, 1])

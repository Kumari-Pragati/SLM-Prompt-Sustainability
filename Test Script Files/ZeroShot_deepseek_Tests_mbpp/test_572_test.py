import unittest
from mbpp_572_code import two_unique_nums

class TestTwoUniqueNums(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(two_unique_nums([]), [])

    def test_single_element(self):
        self.assertEqual(two_unique_nums([1]), [1])

    def test_all_unique(self):
        self.assertEqual(two_unique_nums([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_all_duplicates(self):
        self.assertEqual(two_unique_nums([1, 1, 1, 1]), [])

    def test_mixed_duplicates(self):
        self.assertEqual(two_unique_nums([1, 2, 2, 3]), [1, 3])

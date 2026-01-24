import unittest
from mbpp_572_code import two_unique_nums

class TestTwoUniqueNums(unittest.TestCase):

    def test_single_unique_num(self):
        self.assertEqual(two_unique_nums([1, 2, 2]), [1])

    def test_multiple_unique_nums(self):
        self.assertEqual(two_unique_nums([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_no_unique_nums(self):
        self.assertEqual(two_unique_nums([1, 1, 1, 1, 1]), [])

    def test_empty_list(self):
        self.assertEqual(two_unique_nums([]), [])

    def test_single_element_list(self):
        self.assertEqual(two_unique_nums([1]), [])

    def test_duplicates(self):
        self.assertEqual(two_unique_nums([1, 1, 2, 2, 3, 3]), [])

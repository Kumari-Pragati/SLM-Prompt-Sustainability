import unittest
from mbpp_572_code import two_unique_nums

class TestTwoUniqueNums(unittest.TestCase):
    def test_two_unique_nums_with_two_unique_elements(self):
        self.assertEqual(two_unique_nums([1, 2, 3]), [1, 2])

    def test_two_unique_nums_with_one_unique_element(self):
        self.assertEqual(two_unique_nums([1, 1, 2]), [2])

    def test_two_unique_nums_with_no_unique_elements(self):
        self.assertEqual(two_unique_nums([1, 1, 1]), [])

    def test_two_unique_nums_with_empty_list(self):
        self.assertEqual(two_unique_nums([]), [])

    def test_two_unique_nums_with_single_element_list(self):
        self.assertEqual(two_unique_nums([1]), [])

    def test_two_unique_nums_with_duplicate_elements(self):
        self.assertEqual(two_unique_nums([1, 1, 1, 2]), [2])

import unittest
from mbpp_572_code import two_unique_nums

class TestTwoUniqueNums(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(two_unique_nums([]), [])

    def test_single_element_list(self):
        self.assertListEqual(two_unique_nums([1]), [])

    def test_single_unique_element_list(self):
        self.assertListEqual(two_unique_nums([1, 2]), [1])

    def test_multiple_unique_elements_list(self):
        self.assertListEqual(two_unique_nums([1, 2, 3]), [1, 2, 3])

    def test_multiple_duplicate_elements_list(self):
        self.assertListEqual(two_unique_nums([1, 1, 2, 2, 3]), [3])

    def test_multiple_unique_and_duplicate_elements_list(self):
        self.assertListEqual(two_unique_nums([1, 1, 2, 3, 3]), [2])

import unittest
from mbpp_572_code import two_unique_nums

class TestTwoUniqueNums(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(two_unique_nums([]), [])

    def test_single_element_list(self):
        self.assertListEqual(two_unique_nums([1]), [1])
        self.assertListEqual(two_unique_nums([0]), [0])

    def test_duplicate_elements(self):
        self.assertListEqual(two_unique_nums([1, 1, 2, 2]), [2])
        self.assertListEqual(two_unique_nums([0, 0, 1, 1]), [])

    def test_multiple_unique_elements(self):
        self.assertListEqual(two_unique_nums([1, 2, 3]), [1, 2, 3])
        self.assertListEqual(two_unique_nums([0, 1, 0]), [1])

    def test_single_unique_element_list(self):
        self.assertListEqual(two_unique_nums([1, 2]), [1, 2])

    def test_invalid_input(self):
        self.assertRaises(TypeError, two_unique_nums, 'string')

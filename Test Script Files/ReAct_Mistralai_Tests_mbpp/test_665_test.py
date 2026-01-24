import unittest
from mbpp_665_code import move_last

class TestMoveLast(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(move_last([]), [])

    def test_single_element_list(self):
        self.assertListEqual(move_last([1]), [])
        self.assertListEqual(move_last([2]), [2])

    def test_multiple_elements_with_single_unique_element(self):
        self.assertListEqual(move_last([1, 1]), [1])
        self.assertListEqual(move_last([2, 2]), [2])

    def test_multiple_elements_with_multiple_unique_elements(self):
        self.assertListEqual(move_last([1, 2, 1]), [2, 1])
        self.assertListEqual(move_last([2, 1, 2]), [1, 2])

    def test_multiple_elements_with_repeated_elements(self):
        self.assertListEqual(move_last([1, 1, 2, 1, 2]), [2, 1, 2])

    def test_list_with_duplicate_first_element(self):
        self.assertListEqual(move_last([1, 1, 1]), [1, 1])

    def test_list_with_multiple_duplicate_first_elements(self):
        self.assertListEqual(move_last([1, 1, 1, 1]), [1, 1, 1])

    def test_list_with_no_first_element(self):
        self.assertRaises(IndexError, move_last, [2, 1])

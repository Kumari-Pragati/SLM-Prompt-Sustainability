import unittest
from mbpp_665_code import move_last

class TestMoveLast(unittest.TestCase):
    def test_single_element_list(self):
        self.assertEqual(move_last([1]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(move_last([1, 2, 1, 3, 1]), [3, 2, 1])

    def test_empty_list(self):
        self.assertEqual(move_last([]), [])

    def test_list_with_only_one_element(self):
        self.assertEqual(move_last([1]), [1])

    def test_list_with_duplicates_and_no_duplicates(self):
        self.assertEqual(move_last([1, 2, 1, 3, 1, 2]), [3, 1, 2])

    def test_list_with_only_duplicates(self):
        self.assertEqual(move_last([1, 1, 1]), [1, 1, 1])

    def test_list_with_no_duplicates(self):
        self.assertEqual(move_last([2, 3, 4]), [2, 3, 4])

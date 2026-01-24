import unittest
from mbpp_272_code import rear_extract

class TestRearExtract(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(rear_extract([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[3], [6], [9]])

    def test_empty_list(self):
        self.assertEqual(rear_extract([]), [])

    def test_single_element_list(self):
        self.assertEqual(rear_extract([[1]]), [[1]])

    def test_list_of_empty_lists(self):
        self.assertEqual(rear_extract([[], [], []]), [[], [], []])

    def test_list_of_lists_with_one_element(self):
        self.assertEqual(rear_extract([[1], [2], [3]]), [[1], [2], [3]])

    def test_list_of_lists_with_multiple_elements(self):
        self.assertEqual(rear_extract([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[3], [6], [9]])

    def test_list_of_lists_with_mixed_lengths(self):
        self.assertEqual(rear_extract([[1, 2, 3], [4], [5, 6, 7, 8, 9]]), [[3], [4], [9]])

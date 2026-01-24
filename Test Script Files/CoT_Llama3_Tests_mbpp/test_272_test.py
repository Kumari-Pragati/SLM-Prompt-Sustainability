import unittest
from mbpp_272_code import rear_extract

class TestRearExtract(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(rear_extract([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [3, 6, 9])

    def test_empty_list(self):
        self.assertEqual(rear_extract([]), [])

    def test_single_element_list(self):
        self.assertEqual(rear_extract([[1]]), [1])

    def test_single_element_sublist(self):
        self.assertEqual(rear_extract([[1, 2, 3], [4]]), [3, 4])

    def test_list_of_single_element_sublists(self):
        self.assertEqual(rear_extract([[1], [2], [3]]), [1, 2, 3])

    def test_list_of_empty_sublists(self):
        self.assertEqual(rear_extract([[], [], []]), [])

    def test_list_with_mixed_sublist_lengths(self):
        self.assertEqual(rear_extract([[1, 2, 3], [4, 5], [6]]), [3, 5, 6])

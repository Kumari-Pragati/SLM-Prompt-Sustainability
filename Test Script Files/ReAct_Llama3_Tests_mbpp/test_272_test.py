import unittest
from mbpp_272_code import rear_extract

class TestRearExtract(unittest.TestCase):

    def test_typical_case(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(rear_extract(test_list), [3, 6, 9])

    def test_empty_list(self):
        test_list = []
        self.assertEqual(rear_extract(test_list), [])

    def test_single_element_list(self):
        test_list = [[1]]
        self.assertEqual(rear_extract(test_list), [1])

    def test_list_with_single_element_sublists(self):
        test_list = [[1], [2], [3]]
        self.assertEqual(rear_extract(test_list), [1, 2, 3])

    def test_list_with_multiple_element_sublists(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(rear_extract(test_list), [3, 6, 9])

    def test_list_with_mixed_length_sublists(self):
        test_list = [[1, 2, 3], [4], [5, 6, 7, 8, 9]]
        self.assertEqual(rear_extract(test_list), [3, 4, 9])

import unittest
from mbpp_754_code import extract_index_list

class TestExtractIndexList(unittest.TestCase):

    def test_typical_case(self):
        l1 = [1, 2, 3, 4, 5]
        l2 = [1, 2, 3, 4, 5]
        l3 = [1, 2, 3, 4, 5]
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(extract_index_list(l1, l2, l3), expected_output)

    def test_empty_lists(self):
        l1 = []
        l2 = []
        l3 = []
        expected_output = []
        self.assertEqual(extract_index_list(l1, l2, l3), expected_output)

    def test_unequal_lengths(self):
        l1 = [1, 2, 3]
        l2 = [1, 2, 3, 4]
        l3 = [1, 2, 3, 4]
        expected_output = []
        self.assertEqual(extract_index_list(l1, l2, l3), expected_output)

    def test_different_elements(self):
        l1 = [1, 2, 3]
        l2 = [4, 5, 6]
        l3 = [7, 8, 9]
        expected_output = []
        self.assertEqual(extract_index_list(l1, l2, l3), expected_output)

    def test_same_elements(self):
        l1 = [1, 1, 1]
        l2 = [1, 1, 1]
        l3 = [1, 1, 1]
        expected_output = [1, 1, 1]
        self.assertEqual(extract_index_list(l1, l2, l3), expected_output)

    def test_mixed_types(self):
        l1 = [1, 'a', 3]
        l2 = [1, 'a', 3]
        l3 = [1, 'a', 3]
        expected_output = [1, 'a', 3]
        self.assertEqual(extract_index_list(l1, l2, l3), expected_output)

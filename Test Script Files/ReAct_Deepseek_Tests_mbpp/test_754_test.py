import unittest
from mbpp_754_code import extract_index_list

class TestExtractIndexList(unittest.TestCase):

    def test_typical_case(self):
        l1 = [1, 2, 3, 4, 5]
        l2 = [1, 2, 3, 4, 5]
        l3 = [1, 2, 3, 4, 5]
        result = extract_index_list(l1, l2, l3)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_empty_lists(self):
        l1 = []
        l2 = []
        l3 = []
        result = extract_index_list(l1, l2, l3)
        self.assertEqual(result, [])

    def test_unequal_length_lists(self):
        l1 = [1, 2, 3]
        l2 = [1, 2, 3, 4]
        l3 = [1, 2, 3, 4]
        result = extract_index_list(l1, l2, l3)
        self.assertEqual(result, [])

    def test_different_elements(self):
        l1 = [1, 2, 3]
        l2 = [4, 5, 6]
        l3 = [7, 8, 9]
        result = extract_index_list(l1, l2, l3)
        self.assertEqual(result, [])

    def test_equal_elements(self):
        l1 = [1, 2, 3]
        l2 = [1, 2, 3]
        l3 = [1, 2, 3]
        result = extract_index_list(l1, l2, l3)
        self.assertEqual(result, [1, 2, 3])

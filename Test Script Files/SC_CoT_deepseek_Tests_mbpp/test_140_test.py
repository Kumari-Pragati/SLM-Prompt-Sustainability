import unittest
from mbpp_140_code import extract_singly

class TestExtractSingly(unittest.TestCase):

    def test_typical_case(self):
        test_list = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]
        self.assertEqual(extract_singly(test_list), [1, 2, 3, 4, 5, 6])

    def test_empty_list(self):
        test_list = []
        self.assertEqual(extract_singly(test_list), [])

    def test_single_element(self):
        test_list = [[1]]
        self.assertEqual(extract_singly(test_list), [1])

    def test_duplicate_elements(self):
        test_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        self.assertEqual(extract_singly(test_list), [1, 2, 3])

    def test_negative_numbers(self):
        test_list = [[-1, -2, -3], [-2, -3, -4], [-4, -5, -6]]
        self.assertEqual(extract_singly(test_list), [-1, -2, -3, -4, -5, -6])

    def test_mixed_numbers(self):
        test_list = [[1, 2, 3], [2, 3, -4], [-4, 5, 6]]
        self.assertEqual(extract_singly(test_list), [1, 2, 3, -4, 5, 6])

    def test_empty_inner_lists(self):
        test_list = [[]]
        self.assertEqual(extract_singly(test_list), [])

    def test_single_inner_list(self):
        test_list = [[1, 2, 3]]
        self.assertEqual(extract_singly(test_list), [1, 2, 3])

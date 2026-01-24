import unittest
from mbpp_140_code import extract_singly

class TestExtractSingly(unittest.TestCase):

    def test_typical_case(self):
        test_list = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
        expected_output = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(extract_singly(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = []
        self.assertEqual(extract_singly(test_list), expected_output)

    def test_single_element_lists(self):
        test_list = [[1], [2], [3]]
        expected_output = [1, 2, 3]
        self.assertEqual(extract_singly(test_list), expected_output)

    def test_duplicate_elements(self):
        test_list = [[1, 2, 2], [2, 3, 3], [3, 4, 4]]
        expected_output = [1, 2, 3, 4]
        self.assertEqual(extract_singly(test_list), expected_output)

    def test_duplicate_elements_in_sublists(self):
        test_list = [[1, 1, 2], [2, 2, 3], [3, 3, 4]]
        expected_output = [1, 2, 3, 4]
        self.assertEqual(extract_singly(test_list), expected_output)

    def test_empty_sublists(self):
        test_list = [[], [], []]
        expected_output = []
        self.assertEqual(extract_singly(test_list), expected_output)

    def test_single_sublist(self):
        test_list = [[1, 2, 3]]
        expected_output = [1, 2, 3]
        self.assertEqual(extract_singly(test_list), expected_output)

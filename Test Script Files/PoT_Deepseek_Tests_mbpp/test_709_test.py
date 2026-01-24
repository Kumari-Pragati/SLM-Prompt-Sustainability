import unittest
from mbpp_709_code import get_unique

class TestGetUnique(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('a', 1), ('b', 1), ('c', 2), ('d', 2)]
        expected_output = "{'1': 2, '2': 1}"
        self.assertEqual(get_unique(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = "{}"
        self.assertEqual(get_unique(test_list), expected_output)

    def test_single_element(self):
        test_list = [('a', 1)]
        expected_output = "{'1': 1}"
        self.assertEqual(get_unique(test_list), expected_output)

    def test_duplicate_elements(self):
        test_list = [('a', 1), ('b', 1), ('c', 1), ('d', 1)]
        expected_output = "{'1': 1}"
        self.assertEqual(get_unique(test_list), expected_output)

    def test_large_list(self):
        test_list = [('a', i) for i in range(1, 1001)]
        expected_output = "{'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '10': 1}"
        self.assertEqual(get_unique(test_list), expected_output)

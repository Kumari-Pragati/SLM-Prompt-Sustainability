import unittest
from mbpp_709_code import get_unique

class TestGetUnique(unittest.TestCase):

    def test_get_unique(self):
        test_list = [('apple', 1), ('banana', 2), ('cherry', 1), ('date', 2), ('elderberry', 3)]
        expected_output = "{'1': 2, '2': 2, '3': 1}"
        self.assertEqual(get_unique(test_list), expected_output)

    def test_get_unique_empty_list(self):
        test_list = []
        expected_output = "{}"
        self.assertEqual(get_unique(test_list), expected_output)

    def test_get_unique_single_element(self):
        test_list = [('apple', 1)]
        expected_output = "{'1': 1}"
        self.assertEqual(get_unique(test_list), expected_output)

    def test_get_unique_multiple_elements(self):
        test_list = [('apple', 1), ('banana', 2), ('cherry', 1), ('date', 2), ('elderberry', 3), ('fig', 1), ('grape', 2), ('kiwi', 3)]
        expected_output = "{'1': 2, '2': 2, '3': 2}"
        self.assertEqual(get_unique(test_list), expected_output)

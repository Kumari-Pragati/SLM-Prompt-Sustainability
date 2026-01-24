import unittest
from mbpp_709_code import get_unique

class TestGetUnique(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('apple', 1), ('banana', 1), ('cherry', 2), ('date', 2)]
        expected_output = "{'1': 2, '2': 1}"
        self.assertEqual(get_unique(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = "{}"
        self.assertEqual(get_unique(test_list), expected_output)

    def test_single_element(self):
        test_list = [('apple', 1)]
        expected_output = "{'1': 1}"
        self.assertEqual(get_unique(test_list), expected_output)

    def test_duplicate_elements(self):
        test_list = [('apple', 1), ('banana', 1), ('cherry', 1), ('date', 1)]
        expected_output = "{'1': 1}"
        self.assertEqual(get_unique(test_list), expected_output)

    def test_invalid_input(self):
        test_list = [('apple', 'one'), ('banana', 1), ('cherry', 2), ('date', 2)]
        with self.assertRaises(TypeError):
            get_unique(test_list)

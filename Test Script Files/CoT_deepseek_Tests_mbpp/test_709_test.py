import unittest
from mbpp_709_code import get_unique

class TestGetUnique(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('a', 1), ('b', 1), ('c', 2), ('d', 2), ('e', 3)]
        expected_output = "{'1': 2, '2': 2, '3': 1}"
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

    def test_large_input(self):
        test_list = [(str(i), i % 10) for i in range(1000)]
        expected_output = "{'0': 100, '1': 100, '2': 100, '3': 100, '4': 100, '5': 100, '6': 100, '7': 100, '8': 100, '9': 100}"
        self.assertEqual(get_unique(test_list), expected_output)

    def test_invalid_input(self):
        test_list = [('a', '1'), ('b', 1), ('c', 2), ('d', 2), ('e', 3)]
        with self.assertRaises(TypeError):
            get_unique(test_list)

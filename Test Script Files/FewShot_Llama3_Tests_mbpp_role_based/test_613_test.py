import unittest
from mbpp_613_code import maximum_value

class TestMaximumValue(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [('a', [1, 2, 3]), ('b', [4, 5, 6])]
        expected_result = [('a', 3), ('b', 6)]
        self.assertEqual(maximum_value(test_list), expected_result)

    def test_empty_list(self):
        test_list = []
        expected_result = []
        self.assertEqual(maximum_value(test_list), expected_result)

    def test_single_element_list(self):
        test_list = [('a', [1])]
        expected_result = [('a', 1)]
        self.assertEqual(maximum_value(test_list), expected_result)

    def test_list_with_duplicates(self):
        test_list = [('a', [1, 2, 2, 3])]
        expected_result = [('a', 3)]
        self.assertEqual(maximum_value(test_list), expected_result)

import unittest
from mbpp_613_code import maximum_value

class TestMaximumValue(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('a', [1, 2, 3]), ('b', [4, 5, 6]), ('c', [7, 8, 9])]
        expected_output = [('a', 3), ('b', 6), ('c', 9)]
        self.assertEqual(maximum_value(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = []
        self.assertEqual(maximum_value(test_list), expected_output)

    def test_single_element(self):
        test_list = [('a', [1])]
        expected_output = [('a', 1)]
        self.assertEqual(maximum_value(test_list), expected_output)

    def test_negative_numbers(self):
        test_list = [('a', [-1, -2, -3]), ('b', [-4, -5, -6])]
        expected_output = [('a', -1), ('b', -4)]
        self.assertEqual(maximum_value(test_list), expected_output)

    def test_duplicate_maximums(self):
        test_list = [('a', [1, 2, 3]), ('b', [3, 2, 1])]
        expected_output = [('a', 3), ('b', 3)]
        self.assertEqual(maximum_value(test_list), expected_output)

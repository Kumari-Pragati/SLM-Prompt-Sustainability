import unittest
from mbpp_613_code import maximum_value

class TestMaximumValue(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('a', [1, 2, 3]), ('b', [4, 5, 6]), ('c', [7, 8, 9])]
        expected_result = [('a', 3), ('b', 6), ('c', 9)]
        self.assertEqual(maximum_value(test_list), expected_result)

    def test_empty_list(self):
        test_list = []
        expected_result = []
        self.assertEqual(maximum_value(test_list), expected_result)

    def test_single_list(self):
        test_list = [('a', [1, 2, 3])]
        expected_result = [('a', 3)]
        self.assertEqual(maximum_value(test_list), expected_result)

    def test_negative_numbers(self):
        test_list = [('a', [-1, -2, -3]), ('b', [-4, -5, -6]), ('c', [-7, -8, -9])]
        expected_result = [('a', -1), ('b', -4), ('c', -7)]
        self.assertEqual(maximum_value(test_list), expected_result)

    def test_duplicate_max_values(self):
        test_list = [('a', [1, 2, 3]), ('b', [3, 3, 3]), ('c', [4, 5, 6])]
        expected_result = [('a', 3), ('b', 3), ('c', 6)]
        self.assertEqual(maximum_value(test_list), expected_result)

    def test_empty_sublists(self):
        test_list = [('a', []), ('b', [4, 5, 6]), ('c', [])]
        expected_result = [('a', None), ('b', 6), ('c', None)]
        self.assertEqual(maximum_value(test_list), expected_result)

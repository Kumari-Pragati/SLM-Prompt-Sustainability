import unittest
from mbpp_613_code import maximum_value

class TestMaximumValue(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('a', [1, 2, 3]), ('b', [4, 5, 6]), ('c', [7, 8, 9])]
        expected_output = [('a', 3), ('b', 6), ('c', 9)]
        self.assertEqual(maximum_value(test_list), expected_output)

    def test_single_list(self):
        test_list = [('single', [1, 2, 3])]
        expected_output = [('single', 3)]
        self.assertEqual(maximum_value(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = []
        self.assertEqual(maximum_value(test_list), expected_output)

    def test_negative_numbers(self):
        test_list = [('negative', [-1, -2, -3])]
        expected_output = [('negative', -1)]
        self.assertEqual(maximum_value(test_list), expected_output)

    def test_duplicate_max(self):
        test_list = [('duplicate', [1, 2, 2])]
        expected_output = [('duplicate', 2)]
        self.assertEqual(maximum_value(test_list), expected_output)

    def test_empty_sublists(self):
        test_list = [('empty', [])]
        expected_output = [('empty', None)]
        self.assertEqual(maximum_value(test_list), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            maximum_value('not a list')

import unittest
from mbpp_357_code import find_max

class TestFindMax(unittest.TestCase):

    def test_typical_case(self):
        test_list = [['1', '2', '3'], ['4', '5', '6']]
        self.assertEqual(find_max(test_list), 6)

    def test_empty_list(self):
        test_list = []
        self.assertIsNone(find_max(test_list))

    def test_single_element(self):
        test_list = [['1']]
        self.assertEqual(find_max(test_list), 1)

    def test_negative_numbers(self):
        test_list = [['-1', '-2', '-3'], ['-4', '-5', '-6']]
        self.assertEqual(find_max(test_list), -1)

    def test_mixed_numbers(self):
        test_list = [['1', '2', '-3'], ['-4', '5', '6']]
        self.assertEqual(find_max(test_list), 6)

    def test_non_numeric_elements(self):
        test_list = [['1', '2', 'a'], ['4', '5', '6']]
        with self.assertRaises(ValueError):
            find_max(test_list)

    def test_empty_string_in_list(self):
        test_list = [['1', '', '3'], ['4', '5', '6']]
        with self.assertRaises(ValueError):
            find_max(test_list)

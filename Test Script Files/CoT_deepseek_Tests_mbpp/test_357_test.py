import unittest
from mbpp_357_code import find_max

class TestFindMax(unittest.TestCase):

    def test_typical_case(self):
        test_list = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.assertEqual(find_max(test_list), 9)

    def test_single_digit(self):
        test_list = [['1'], ['2'], ['3']]
        self.assertEqual(find_max(test_list), 3)

    def test_negative_numbers(self):
        test_list = [['-1', '-2', '-3'], ['-4', '-5', '-6'], ['-7', '-8', '-9']]
        self.assertEqual(find_max(test_list), -1)

    def test_mixed_numbers(self):
        test_list = [['1', '-2', '3'], ['-4', '5', '-6'], ['7', '-8', '9']]
        self.assertEqual(find_max(test_list), 9)

    def test_empty_list(self):
        test_list = []
        self.assertIsNone(find_max(test_list))

    def test_invalid_input(self):
        test_list = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9a']]
        with self.assertRaises(ValueError):
            find_max(test_list)

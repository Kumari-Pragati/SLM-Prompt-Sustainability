import unittest
from mbpp_357_code import find_max

class TestFindMax(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.assertEqual(find_max(test_list), 9)

    def test_edge_case_with_single_digit(self):
        test_list = [['0'], ['1'], ['2']]
        self.assertEqual(find_max(test_list), 2)

    def test_boundary_case_with_negative_numbers(self):
        test_list = [['-1', '-2', '-3'], ['-4', '-5', '-6'], ['-7', '-8', '-9']]
        self.assertEqual(find_max(test_list), -1)

    def test_invalid_input_with_non_string_elements(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        with self.assertRaises(TypeError):
            find_max(test_list)

    def test_invalid_input_with_non_list_elements(self):
        test_list = '123456789'
        with self.assertRaises(TypeError):
            find_max(test_list)

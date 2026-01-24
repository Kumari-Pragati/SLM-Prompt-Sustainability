import unittest
from mbpp_237_code import check_occurences

class TestCheckOccurrences(unittest.TestCase):

    def test_typical_case(self):
        test_list = [['a', 'b', 'c'], ['b', 'c', 'a'], ['c', 'a', 'b']]
        expected_output = {'('a', 'b', 'c')': 3}
        self.assertEqual(check_occurences(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = {}
        self.assertEqual(check_occurences(test_list), expected_output)

    def test_single_element(self):
        test_list = [['a']]
        expected_output = {'('a')': 1}
        self.assertEqual(check_occurences(test_list), expected_output)

    def test_duplicate_elements(self):
        test_list = [['a', 'a', 'b'], ['b', 'a', 'a']]
        expected_output = {'('a', 'b')': 2, '('a', 'a'): 2}
        self.assertEqual(check_occurences(test_list), expected_output)

    def test_sorted_elements(self):
        test_list = [['b', 'a'], ['a', 'b']]
        expected_output = {'('a', 'b')': 2}
        self.assertEqual(check_occurences(test_list), expected_output)

    def test_none_elements(self):
        test_list = [None, None]
        with self.assertRaises(TypeError):
            check_occurences(test_list)

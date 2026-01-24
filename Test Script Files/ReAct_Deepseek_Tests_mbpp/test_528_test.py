import unittest
from mbpp_528_code import min_length

class TestMinLength(unittest.TestCase):

    def test_typical_case(self):
        list1 = ['hello', 'world', 'unittest']
        expected_output = (5, 'world')
        self.assertEqual(min_length(list1), expected_output)

    def test_empty_list(self):
        list1 = []
        expected_output = (0, '')
        self.assertEqual(min_length(list1), expected_output)

    def test_single_element(self):
        list1 = ['single']
        expected_output = (6, 'single')
        self.assertEqual(min_length(list1), expected_output)

    def test_all_same_length(self):
        list1 = ['aaaaa', 'bbbbb', 'ccccc']
        expected_output = (5, 'aaaaa')
        self.assertEqual(min_length(list1), expected_output)

    def test_all_different_length(self):
        list1 = ['a', 'ab', 'abc', 'abcd', 'abcde']
        expected_output = (1, 'a')
        self.assertEqual(min_length(list1), expected_output)

    def test_empty_strings(self):
        list1 = ['', 'abc', '']
        expected_output = (3, '')
        self.assertEqual(min_length(list1), expected_output)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            min_length(None)

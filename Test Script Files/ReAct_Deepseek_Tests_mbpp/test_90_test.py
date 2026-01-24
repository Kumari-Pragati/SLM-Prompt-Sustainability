import unittest
from mbpp_90_code import len_log

class TestLenLog(unittest.TestCase):

    def test_typical_case(self):
        list1 = ['abc', 'defgh', 'ijkl']
        self.assertEqual(len_log(list1), 5)

    def test_empty_list(self):
        list1 = []
        self.assertEqual(len_log(list1), 0)

    def test_single_element_list(self):
        list1 = ['abc']
        self.assertEqual(len_log(list1), 3)

    def test_all_same_length_elements(self):
        list1 = ['abcd', 'efgh', 'ijkl']
        self.assertEqual(len_log(list1), 4)

    def test_empty_strings(self):
        list1 = ['', 'abc', '']
        self.assertEqual(len_log(list1), 3)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            len_log(None)

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            len_log('abc')

    def test_list_with_non_string_elements(self):
        with self.assertRaises(TypeError):
            len_log([1, 'abc', 'def'])

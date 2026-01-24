import unittest
from mbpp_947_code import len_log

class TestLenLog(unittest.TestCase):

    def test_typical_case(self):
        list1 = ['abc', 'defgh', 'ijkl']
        self.assertEqual(len_log(list1), 3)

    def test_single_element_list(self):
        list1 = ['abc']
        self.assertEqual(len_log(list1), len(list1[0]))

    def test_empty_list(self):
        list1 = []
        with self.assertRaises(IndexError):
            len_log(list1)

    def test_all_same_length_elements(self):
        list1 = ['abcd', 'efgh', 'ijkl']
        self.assertEqual(len_log(list1), len(list1[0]))

    def test_all_different_length_elements(self):
        list1 = ['a', 'ab', 'abc']
        self.assertEqual(len_log(list1), 1)

    def test_list_with_empty_string(self):
        list1 = ['abc', '', 'def']
        self.assertEqual(len_log(list1), 0)

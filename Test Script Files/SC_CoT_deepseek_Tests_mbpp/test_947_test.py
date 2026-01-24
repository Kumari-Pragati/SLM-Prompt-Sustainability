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

    def test_longest_string_at_end(self):
        list1 = ['abc', 'defgh', 'ijklmnop']
        self.assertEqual(len_log(list1), len(list1[-1]))

    def test_empty_strings(self):
        list1 = ['', 'defgh', 'ijkl']
        self.assertEqual(len_log(list1), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            len_log(123)

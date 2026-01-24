import unittest
from mbpp_90_code import len_log

class TestLenLog(unittest.TestCase):

    def test_typical_case(self):
        list1 = ['abc', 'defgh', 'ijklmn']
        self.assertEqual(len_log(list1), 5)

    def test_single_element_list(self):
        list1 = ['abc']
        self.assertEqual(len_log(list1), 3)

    def test_empty_list(self):
        list1 = []
        self.assertRaises(ValueError, len_log, list1)

    def test_list_with_empty_string(self):
        list1 = ['abc', '', 'def']
        self.assertEqual(len_log(list1), 3)

    def test_list_with_none_element(self):
        list1 = ['abc', None, 'def']
        self.assertRaises(TypeError, len_log, list1)

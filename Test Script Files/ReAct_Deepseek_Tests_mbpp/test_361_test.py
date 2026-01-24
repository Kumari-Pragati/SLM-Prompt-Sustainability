import unittest
from mbpp_361_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):

    def test_typical_case(self):
        list1 = ['a', 'b', 'c', '']
        expected_output = ['a', 'b', 'c']
        self.assertEqual(remove_empty(list1), expected_output)

    def test_empty_list(self):
        list1 = []
        expected_output = []
        self.assertEqual(remove_empty(list1), expected_output)

    def test_list_with_empty_strings(self):
        list1 = ['', '']
        expected_output = []
        self.assertEqual(remove_empty(list1), expected_output)

    def test_list_with_one_empty_string(self):
        list1 = ['a', '']
        expected_output = ['a']
        self.assertEqual(remove_empty(list1), expected_output)

    def test_list_with_all_empty_strings(self):
        list1 = ['', '', '']
        expected_output = []
        self.assertEqual(remove_empty(list1), expected_output)

    def test_list_with_none_empty_strings(self):
        list1 = ['a', 'b', 'c']
        expected_output = ['a', 'b', 'c']
        self.assertEqual(remove_empty(list1), expected_output)

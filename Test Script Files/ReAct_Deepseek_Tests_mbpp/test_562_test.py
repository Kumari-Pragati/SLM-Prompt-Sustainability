import unittest
from mbpp_562_code import Find_Max_Length

class TestFindMaxLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Find_Max_Length(['abc', 'defgh', 'ijklm']), 5)

    def test_empty_list(self):
        self.assertEqual(Find_Max_Length([]), 0)

    def test_list_with_single_element(self):
        self.assertEqual(Find_Max_Length(['abc']), 3)

    def test_list_with_same_length_elements(self):
        self.assertEqual(Find_Max_Length(['abcd', 'efgh', 'ijkl']), 4)

    def test_list_with_empty_string(self):
        self.assertEqual(Find_Max_Length(['abc', '', 'def']), 3)

    def test_list_with_none_elements(self):
        with self.assertRaises(TypeError):
            Find_Max_Length(['abc', None, 'def'])

import unittest
from mbpp_562_code import Find_Max_Length

class TestFindMaxLength(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(Find_Max_Length(['abc', 'defgh', 'ijkl']), 5)

    def test_empty_list(self):
        self.assertEqual(Find_Max_Length([]), 0)

    def test_single_element_list(self):
        self.assertEqual(Find_Max_Length(['abc']), 3)

    def test_all_same_length_elements(self):
        self.assertEqual(Find_Max_Length(['abc', 'def', 'ghi']), 3)

    def test_empty_strings(self):
        self.assertEqual(Find_Max_Length(['', '']), 0)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            Find_Max_Length(None)

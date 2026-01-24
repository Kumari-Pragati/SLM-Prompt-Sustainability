import unittest

from mbpp_95_code import Find_Min_Length

class TestFindMinLength(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(Find_Min_Length(['hello', 'world', 'python']), 5)

    def test_empty_list(self):
        self.assertEqual(Find_Min_Length([]), 0)

    def test_single_element_list(self):
        self.assertEqual(Find_Min_Length(['python']), 6)

    def test_list_with_empty_string(self):
        self.assertEqual(Find_Min_Length(['hello', '', 'python']), 0)

    def test_list_with_numeric_strings(self):
        self.assertEqual(Find_Min_Length(['123', '456', '789']), 3)

    def test_list_with_numeric_strings_and_empty(self):
        self.assertEqual(Find_Min_Length(['123', '456', '', '789']), 0)

    def test_list_with_non_string_elements(self):
        with self.assertRaises(TypeError):
            Find_Min_Length([123, '456', '789'])

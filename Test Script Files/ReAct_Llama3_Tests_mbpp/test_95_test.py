import unittest
from mbpp_95_code import Find_Min_Length

class TestFind_Min_Length(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(Find_Min_Length([]), 0)

    def test_single_element_list(self):
        self.assertEqual(Find_Min_Length(['hello']), 5)

    def test_multiple_elements_list(self):
        self.assertEqual(Find_Min_Length(['hello', 'world', 'python']), 5)

    def test_list_with_empty_string(self):
        self.assertEqual(Find_Min_Length(['hello', '', 'world']), 5)

    def test_list_with_mixed_length_strings(self):
        self.assertEqual(Find_Min_Length(['hello', 'world', 'python','short']), 5)

    def test_list_with_all_empty_strings(self):
        self.assertEqual(Find_Min_Length(['', '', '', '']), 0)

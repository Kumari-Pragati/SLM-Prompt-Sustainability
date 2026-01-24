import unittest
from mbpp_95_code import Find_Min_Length

class TestFindMinLength(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(Find_Min_Length([]), 0)

    def test_single_element_list(self):
        self.assertEqual(Find_Min_Length(['hello']), 5)

    def test_multiple_elements_list(self):
        self.assertEqual(Find_Min_Length(['hello', 'world', 'abc']), 3)

    def test_list_with_empty_string(self):
        self.assertEqual(Find_Min_Length(['hello', '', 'world']), 0)

    def test_list_with_mixed_lengths(self):
        self.assertEqual(Find_Min_Length(['hello', 'world', 'abc','short']), 3)

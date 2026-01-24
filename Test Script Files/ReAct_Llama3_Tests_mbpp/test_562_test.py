import unittest
from mbpp_562_code import Find_Max_Length

class TestFind_Max_Length(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(Find_Max_Length([]), 0)

    def test_single_element_list(self):
        self.assertEqual(Find_Max_Length(['hello']), 5)

    def test_multiple_element_list(self):
        self.assertEqual(Find_Max_Length(['hello', 'world', 'python']), 7)

    def test_list_with_empty_string(self):
        self.assertEqual(Find_Max_Length(['hello', '', 'world']), 6)

    def test_list_with_longest_string(self):
        self.assertEqual(Find_Max_Length(['hello', 'world', 'pythonprogramming']), 24)

    def test_list_with_ties(self):
        self.assertEqual(Find_Max_Length(['hello', 'world', 'pythonprogramming']), 24)

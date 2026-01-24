import unittest
from mbpp_204_code import count

class TestCountFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count('abcabc', 'a'), 2)
        self.assertEqual(count('hello world', 'l'), 3)

    def test_edge_case_empty_string(self):
        self.assertEqual(count('', 'a'), 0)

    def test_edge_case_no_occurrence(self):
        self.assertEqual(count('abcabc', 'd'), 0)

    def test_edge_case_single_character(self):
        self.assertEqual(count('a', 'a'), 1)
        self.assertEqual(count('a', 'b'), 0)

    def test_edge_case_case_sensitivity(self):
        self.assertEqual(count('Abcabc', 'a'), 0)

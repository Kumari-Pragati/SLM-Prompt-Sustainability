import unittest
from mbpp_202_code import remove_even

class TestRemoveEven(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_even('abcdefg'), 'acfg')

    def test_edge_case_odd_length(self):
        self.assertEqual(remove_even('a'), 'a')

    def test_edge_case_even_length(self):
        self.assertEqual(remove_even('ab'), 'b')

    def test_boundary_case_empty_string(self):
        self.assertEqual(remove_even(''), '')

    def test_boundary_case_single_character(self):
        self.assertEqual(remove_even('x'), 'x')

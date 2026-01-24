import unittest
from mbpp_53_code import check_Equality

class TestCheckEquality(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(check_Equality('abcba'), 'Equal')

    def test_edge_case_empty_string(self):
        self.assertEqual(check_Equality(''), 'Equal')

    def test_edge_case_single_character(self):
        self.assertEqual(check_Equality('a'), 'Equal')

    def test_boundary_case_two_characters(self):
        self.assertEqual(check_Equality('ab'), 'Not Equal')

    def test_complex_case_different_characters(self):
        self.assertEqual(check_Equality('abcd'), 'Not Equal')

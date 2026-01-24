import unittest
from mbpp_647_code import split_upperstring

class TestSplitUpperstring(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(split_upperstring('HelloWorldThisIsATest'), ['Hello', 'World', 'This', 'Is', 'A', 'Test'])

    def test_edge_case_single_uppercase(self):
        self.assertEqual(split_upperstring('A'), ['A'])

    def test_edge_case_no_uppercase(self):
        self.assertEqual(split_upperstring('hello world'), [])

    def test_boundary_case_empty_string(self):
        self.assertEqual(split_upperstring(''), [])

    def test_corner_case_multiple_uppercase_in_a_row(self):
        self.assertEqual(split_upperstring('HELLOAWORLD'), ['HELLO', 'AWORLD'])

    def test_corner_case_uppercase_at_the_end(self):
        self.assertEqual(split_upperstring('HelloWorldA'), ['Hello', 'World', 'A'])

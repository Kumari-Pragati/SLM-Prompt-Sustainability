import unittest
from mbpp_482_code import match

class TestMatchFunction(unittest.TestCase):
    def test_match_valid_input(self):
        self.assertEqual(match('HelloWorld'), 'Yes')

    def test_match_invalid_input(self):
        self.assertEqual(match('123'), 'No')

    def test_match_edge_case(self):
        self.assertEqual(match('Hello'), 'No')

    def test_match_edge_case2(self):
        self.assertEqual(match('HelloWorld123'), 'Yes')

    def test_match_edge_case3(self):
        self.assertEqual(match('HELLO'), 'Yes')

    def test_match_edge_case4(self):
        self.assertEqual(match('hello'), 'No')

    def test_match_edge_case5(self):
        self.assertEqual(match(''), 'No')

    def test_match_edge_case6(self):
        self.assertEqual(match('HelloWorld123abc'), 'Yes')

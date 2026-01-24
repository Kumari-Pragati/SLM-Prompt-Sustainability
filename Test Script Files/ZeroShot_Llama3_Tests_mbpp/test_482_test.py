import unittest
from mbpp_482_code import match

class TestMatchFunction(unittest.TestCase):

    def test_match_positive(self):
        self.assertEqual(match('HelloWorld'), 'Yes')

    def test_match_negative(self):
        self.assertEqual(match('hello'), 'No')

    def test_match_edge_case(self):
        self.assertEqual(match('ABCdef'), 'Yes')

    def test_match_edge_case2(self):
        self.assertEqual(match('ABC'), 'No')

    def test_match_edge_case3(self):
        self.assertEqual(match('Hello'), 'No')

    def test_match_edge_case4(self):
        self.assertEqual(match('HelloWorld123'), 'Yes')

    def test_match_edge_case5(self):
        self.assertEqual(match('Hello123'), 'No')

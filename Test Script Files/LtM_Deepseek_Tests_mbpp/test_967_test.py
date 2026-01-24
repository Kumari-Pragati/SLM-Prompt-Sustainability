import unittest
from mbpp_967_code import check

class TestCheckFunction(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(check("aeiou"), 'accepted')
        self.assertEqual(check("AEIOU"), 'accepted')
        self.assertEqual(check("aeiouy"), 'accepted')
        self.assertEqual(check("AEIOUY"), 'accepted')

    def test_edge_conditions(self):
        self.assertEqual(check(""), 'not accepted')
        self.assertEqual(check("bcdfghjklmnpqrstvwxyz"), 'not accepted')
        self.assertEqual(check("AEIOUaeiouy"), 'accepted')
        self.assertEqual(check("AEIOUYaeiou"), 'accepted')

    def test_complex_cases(self):
        self.assertEqual(check("AEIOUaeiouAEIOUaeiou"), 'accepted')
        self.assertEqual(check("AEIOUaeiouAEIOUaeiouy"), 'accepted')
        self.assertEqual(check("AEIOUaeiouyAEIOUaeiou"), 'accepted')
        self.assertEqual(check("AEIOUaeiouyAEIOUaeiouy"), 'accepted')

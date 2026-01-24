import unittest
from mbpp_668_code import replace

class TestReplaceFunction(unittest.TestCase):

    def test_simple_replace(self):
        self.assertEqual(replace('aabbcc', 'b'), 'acc')
        self.assertEqual(replace('aaabbbccc', 'a'), 'bbcc')

    def test_edge_conditions(self):
        self.assertEqual(replace('', 'a'), '')
        self.assertEqual(replace('a', 'a'), 'a')
        self.assertEqual(replace('aaaa', 'a'), 'a')

    def test_boundary_conditions(
        self):
        self.assertEqual(replace('a' * 10000 + 'b', 'b'), 'a' * 10000)

    def test_complex_cases(self):
        self.assertEqual(replace('aabbaabb', 'a'), 'bb')
        self.assertEqual(replace('aabbcc', 'd'), 'aabbcc')
        self.assertEqual(replace('aabbcc', ''), 'aabbcc')

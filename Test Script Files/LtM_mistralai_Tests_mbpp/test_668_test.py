import unittest
from mbpp_668_code import replace

class TestReplace(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(replace('aa', 'a'), 'aa')
        self.assertEqual(replace('aaa', 'a'), 'aaa')
        self.assertEqual(replace('aaaa', 'a'), 'aaaa')

    def test_edge_cases(self):
        self.assertEqual(replace('', 'a'), '')
        self.assertEqual(replace('a', 'a'), 'a')
        self.assertEqual(replace('aaa...', 'a'), 'aaa...')
        self.assertEqual(replace('aaaaaa', 'a'), 'aaaaaa')

    def test_complex(self):
        self.assertEqual(replace('aaaAaa', 'a'), 'aaaAaa')
        self.assertEqual(replace('aaaAaaBbb', 'a'), 'aaaAaaBbb')
        self.assertEqual(replace('aaaAaaBbbCcc', 'a'), 'aaaAaaBbbCcc')
        self.assertEqual(replace('aaaAaaBbbCccDdd', 'a'), 'aaaAaaBbbCccDdd')

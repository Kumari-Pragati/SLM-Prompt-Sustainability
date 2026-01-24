import unittest
from mbpp_202_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(remove_even('abcdefg'), 'acfg')
        self.assertEqual(remove_even('ABCDEFG'), 'ABCG')
        self.assertEqual(remove_even('1234567'), '1357')

    def test_edge_cases(self):
        self.assertEqual(remove_even(''), '')
        self.assertEqual(remove_even('a'), 'a')
        self.assertEqual(remove_even('ab'), 'b')
        self.assertEqual(remove_even('abc'), 'ac')
        self.assertEqual(remove_even('abcdef'), 'acde')
        self.assertEqual(remove_even('abcdefg'), 'acfg')
        self.assertEqual(remove_even('ABCDEFG'), 'ABCG')
        self.assertEqual(remove_even('12345678'), '13578')

    def test_boundary_cases(self):
        self.assertEqual(remove_even('a'), 'a')
        self.assertEqual(remove_even('ab'), 'b')
        self.assertEqual(remove_even('abc'), 'ac')
        self.assertEqual(remove_even('abcdef'), 'acde')
        self.assertEqual(remove_even('abcdefg'), 'acfg')
        self.assertEqual(remove_even('ABCDEFG'), 'ABCG')
        self.assertEqual(remove_even('12345678'), '13578')
        self.assertEqual(remove_even('123456789'), '135789')

import unittest
from mbpp_668_code import replace

class TestReplace(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(replace('aaa', 'x'), 'xxxx')
        self.assertEqual(replace('xxxx', 'y'), 'yyyy')
        self.assertEqual(replace('xyz', 'a'), 'aaaa')

    def test_edge_case_single_char(self):
        self.assertEqual(replace('a', 'x'), 'x')
        self.assertEqual(replace('x', 'y'), 'y')

    def test_edge_case_empty_string(self):
        self.assertEqual(replace('', 'x'), '')

    def test_edge_case_single_char_repeated(self):
        self.assertEqual(replace('xx', 'y'), 'yy')

    def test_corner_case_single_char_at_start_and_end(self):
        self.assertEqual(replace('xa', 'y'), 'yya')
        self.assertEqual(replace('ay', 'z'), 'zzz')

    def test_corner_case_single_char_in_middle(self):
        self.assertEqual(replace('axb', 'y'), 'ayby')
        self.assertEqual(replace('yzc', 'x'), 'xxcx')

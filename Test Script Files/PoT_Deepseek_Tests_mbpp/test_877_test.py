import unittest
from mbpp_877_code import sort_String

class TestSortString(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sort_String('cba'), 'abc')
        self.assertEqual(sort_String('123'), '123')
        self.assertEqual(sort_String('zyx'), 'xyz')

    def test_edge_cases(self):
        self.assertEqual(sort_String(''), '')
        self.assertEqual(sort_String('a'), 'a')
        self.assertEqual(sort_String('aa'), 'aa')

    def test_corner_cases(self):
        self.assertEqual(sort_String('aaaabbb'), 'abababab')
        self.assertEqual(sort_String('112233'), '112233')
        self.assertEqual(sort_String('!@#$%^&*('), '!()%&*#$%@^')

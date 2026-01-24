import unittest
from mbpp_923_code import super_seq

class TestSuperSeq(unittest.TestCase):

    def test_super_seq(self):
        self.assertEqual(super_seq('AGGTAB', 'GXTXAYB', 6, 6), 6)
        self.assertEqual(super_seq('ABCDGH', 'AEDFHR', 5, 5), 5)
        self.assertEqual(super_seq('ABC', 'AC', 2, 2), 2)
        self.assertEqual(super_seq('AXYZ', 'XYZ', 3, 3), 3)
        self.assertEqual(super_seq('ABC', 'DEF', 3, 3), 0)

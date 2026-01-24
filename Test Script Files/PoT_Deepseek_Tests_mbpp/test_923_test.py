import unittest
from mbpp_923_code import super_seq

class TestSuperSeq(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(super_seq('ABCDGH', 'AEDFHR', 6, 6), 3)
        self.assertEqual(super_seq('AGGTAB', 'GXTXAYB', 6, 6), 4)

    def test_edge_cases(self):
        self.assertEqual(super_seq('', 'AEDFHR', 0, 6), 6)
        self.assertEqual(super_seq('ABCDGH', '', 6, 0), 6)
        self.assertEqual(super_seq('', '', 0, 0), 0)

    def test_boundary_cases(self):
        self.assertEqual(super_seq('A', 'A', 1, 1), 1)
        self.assertEqual(super_seq('AB', 'AB', 2, 2), 2)

    def test_corner_cases(self):
        self.assertEqual(super_seq('ABC', 'DEF', 3, 3), 0)
        self.assertEqual(super_seq('ABC', 'ABC', 3, 3), 3)

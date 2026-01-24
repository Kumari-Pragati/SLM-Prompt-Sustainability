import unittest
from mbpp_923_code import super_seq

class TestSuperSeq(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(super_seq('ABCDGH', 'AEDFHR', 6, 6), 3)
        self.assertEqual(super_seq('ABC', 'AC', 3, 2), 2)

    def test_edge_conditions(self):
        self.assertEqual(super_seq('', 'AEDFHR', 0, 6), 6)
        self.assertEqual(super_seq('ABCDGH', '', 6, 0), 6)
        self.assertEqual(super_seq('', '', 0, 0), 0)

    def test_boundary_conditions(self):
        self.assertEqual(super_seq('A', 'A', 1, 1), 1)
        self.assertEqual(super_seq('AB', 'AB', 2, 2), 2)

    def test_complex_cases(self):
        self.assertEqual(super_seq('AGGTAB', 'GXTXAYB', 6, 6), 4)
        self.assertEqual(super_seq('XMJYAUZ', 'MZJAWXU', 6, 6), 5)

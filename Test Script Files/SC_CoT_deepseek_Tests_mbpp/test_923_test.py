import unittest
from mbpp_923_code import super_seq

class TestSuperSeq(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(super_seq('AGGTAB', 'GXTXAYB', 6, 6), 6)

    def test_edge_case(self):
        self.assertEqual(super_seq('', 'GXTXAYB', 0, 6), 6)
        self.assertEqual(super_seq('AGGTAB', '', 6, 0), 6)
        self.assertEqual(super_seq('', '', 0, 0), 0)

    def test_corner_case(self):
        self.assertEqual(super_seq('A', 'A', 1, 1), 1)
        self.assertEqual(super_seq('AGGTAB', 'GXTXAYB', 6, 6), 6)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            super_seq(123, 'GXTXAYB', 6, 6)
        with self.assertRaises(TypeError):
            super_seq('AGGTAB', 123, 6, 6)
        with self.assertRaises(TypeError):
            super_seq('AGGTAB', 'GXTXAYB', 'six', 6)
        with self.assertRaises(TypeError):
            super_seq('AGGTAB', 'GXTXAYB', 6, 'six')

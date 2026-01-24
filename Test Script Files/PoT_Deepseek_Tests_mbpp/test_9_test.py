import unittest
from mbpp_9_code import find_Rotations

class TestFindRotations(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_Rotations('abc'), 0)
        self.assertEqual(find_Rotations('abcdabcd'), 4)
        self.assertEqual(find_Rotations('abcabcabc'), 6)

    def test_edge_cases(self):
        self.assertEqual(find_Rotations(''), 0)
        self.assertEqual(find_Rotations('a'), 0)

    def test_boundary_conditions(self):
        self.assertEqual(find_Rotations('a' * 10000), 0)
        self.assertEqual(find_Rotations('b' * 10000 + 'a'), 10000)

    def test_corner_cases(self):
        self.assertEqual(find_Rotations('abcabcabcabc'), 6)
        self.assertEqual(find_Rotations('abcabcabcabca'), 6)
        self.assertEqual(find_Rotations('abcabcabcabcab'), 6)

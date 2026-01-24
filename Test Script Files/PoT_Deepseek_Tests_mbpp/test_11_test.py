import unittest
from mbpp_11_code import remove_Occ

class TestRemoveOcc(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(remove_Occ('hello', 'l'), 'heo')
        self.assertEqual(remove_Occ('aabbcc', 'b'), 'aac')
        self.assertEqual(remove_Occ('122333', '2'), '133')

    def test_edge_cases(self):
        self.assertEqual(remove_Occ('', 'a'), '')
        self.assertEqual(remove_Occ('a', 'a'), '')
        self.assertEqual(remove_Occ('aaa', 'a'), '')

    def test_boundary_cases(self):
        self.assertEqual(remove_Occ('a' * 10000, 'a'), '')
        self.assertEqual(remove_Occ('b' * 9999 + 'a', 'a'), 'b' * 9999)

    def test_corner_cases(self):
        self.assertEqual(remove_Occ('abc', 'd'), 'abc')
        self.assertEqual(remove_Occ('aabbcc', 'd'), 'aabbcc')

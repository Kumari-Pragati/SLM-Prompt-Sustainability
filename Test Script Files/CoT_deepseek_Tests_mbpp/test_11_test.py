import unittest
from mbpp_11_code import remove_Occ

class TestRemoveOcc(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_Occ('abcabc', 'b'), 'acac')

    def test_edge_case(self):
        self.assertEqual(remove_Occ('', 'a'), '')
        self.assertEqual(remove_Occ('a', 'a'), '')
        self.assertEqual(remove_Occ('aaaa', 'a'), '')

    def test_boundary_case(self):
        self.assertEqual(remove_Occ('a'*10000, 'a'), '')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_Occ(123, 'a')
        with self.assertRaises(TypeError):
            remove_Occ('abc', 123)

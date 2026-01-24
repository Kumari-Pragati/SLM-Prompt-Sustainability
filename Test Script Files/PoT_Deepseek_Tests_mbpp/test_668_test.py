import unittest
from mbpp_668_code import replace

class TestReplace(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace('aabbcc', 'b'), 'acc')

    def test_edge_case(self):
        self.assertEqual(replace('a', 'b'), 'a')

    def test_boundary_case(self):
        self.assertEqual(replace('aaaa', 'a'), 'a')

    def test_corner_case(self):
        self.assertEqual(replace('aabbaabb', 'a'), 'b')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            replace(123, 'b')

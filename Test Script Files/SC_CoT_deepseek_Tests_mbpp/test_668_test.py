import unittest
from mbpp_668_code import replace

class TestReplace(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace('aabbcc', 'b'), 'acc')

    def test_edge_case(self):
        self.assertEqual(replace('', 'b'), '')
        self.assertEqual(replace('aabbcc', ''), 'aabbcc')

    def test_corner_case(self):
        self.assertEqual(replace('aabbbcc', 'b'), 'acc')
        self.assertEqual(replace('aabbcc', 'c'), 'aabb')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            replace(123, 'b')
        with self.assertRaises(TypeError):
            replace('aabbcc', 123)

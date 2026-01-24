import unittest
from mbpp_27_code import remove

class TestRemoveFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove(['abc123', 'def456']), ['abc', 'def'])

    def test_edge_case(self):
        self.assertEqual(remove(['123456']), [''])

    def test_corner_case(self):
        self.assertEqual(remove(['']), [''])

    def test_special_case(self):
        self.assertEqual(remove(['a1b2c3d4e5f6']), ['abcdef'])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove(123456)

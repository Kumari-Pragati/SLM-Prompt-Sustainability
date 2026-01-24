import unittest
from mbpp_59_code import is_octagonal

class TestIsOctagonal(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(is_octagonal(1), 0)
        self.assertEqual(is_octagonal(2), 4)
        self.assertEqual(is_octagonal(3), 15)
        self.assertEqual(is_octagonal(4), 32)

    def test_edge_cases(self):
        self.assertEqual(is_octagonal(0), 0)
        self.assertEqual(is_octagonal(100), 29900)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_octagonal("1")
        with self.assertRaises(TypeError):
            is_octagonal(None)
        with self.assertRaises(TypeError):
            is_octagonal([])

import unittest
from mbpp_59_code import is_octagonal

class TestIsOctagonal(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(is_octagonal(1), 2)
        self.assertEqual(is_octagonal(2), 8)
        self.assertEqual(is_octagonal(3), 18)

    def test_edge_cases(self):
        self.assertEqual(is_octagonal(0), 0)
        self.assertEqual(is_octagonal(100), 30002)
        self.assertEqual(is_octagonal(-1), -2)
        self.assertEqual(is_octagonal(-2), -8)
        self.assertEqual(is_octagonal(-3), -18)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_octagonal(3.14)
        with self.assertRaises(TypeError):
            is_octagonal([1, 2, 3])

import unittest
from mbpp_59_code import is_octagonal

class TestIsOctagonal(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(is_octagonal(1), 1)
        self.assertEqual(is_octagonal(2), 5)
        self.assertEqual(is_octagonal(3), 19)

    def test_edge_cases(self):
        self.assertEqual(is_octagonal(-1), None)
        self.assertEqual(is_octagonal(0), None)
        self.assertEqual(is_octagonal(4), 37)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_octagonal("a")

    def test_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            is_octagonal(1.5)

    def test_negative_inputs(self):
        with self.assertRaises(TypeError):
            is_octagonal(-4)

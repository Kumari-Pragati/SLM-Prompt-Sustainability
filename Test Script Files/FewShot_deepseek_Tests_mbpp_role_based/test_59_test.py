import unittest
from mbpp_59_code import is_octagonal

class TestIsOctagonal(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(is_octagonal(1), 2)
        self.assertEqual(is_octagonal(2), 14)
        self.assertEqual(is_octagonal(3), 34)

    def test_edge_conditions(self):
        self.assertEqual(is_octagonal(0), 0)
        self.assertEqual(is_octagonal(1), 2)

    def test_boundary_conditions(self):
        self.assertEqual(is_octagonal(100), 30200)
        self.assertEqual(is_octagonal(1000), 3002000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_octagonal('a')
        with self.assertRaises(TypeError):
            is_octagonal(None)
        with self.assertRaises(TypeError):
            is_octagonal([])

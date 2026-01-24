import unittest
from mbpp_346_code import zigzag

class TestZigzag(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(zigzag(3, 2), 3)

    def test_boundary_conditions(self):
        self.assertEqual(zigzag(0, 0), 1)
        self.assertEqual(zigzag(3, 0), 0)
        self.assertEqual(zigzag(0, 3), 0)

    def test_edge_conditions(self):
        self.assertEqual(zigzag(1, 1), 1)
        self.assertEqual(zigzag(2, 2), 1)
        self.assertEqual(zigzag(3, 3), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            zigzag("3", 2)
        with self.assertRaises(TypeError):
            zigzag(3, "2")
        with self.assertRaises(ValueError):
            zigzag(-1, 2)
        with self.assertRaises(ValueError):
            zigzag(3, -1)

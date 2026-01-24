import unittest
from mbpp_346_code import zigzag

class TestZigzag(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(zigzag(3, 2), 3)
        self.assertEqual(zigzag(4, 3), 4)
        self.assertEqual(zigzag(2, 1), 1)

    def test_edge_cases(self):
        self.assertEqual(zigzag(0, 0), 1)
        self.assertEqual(zigzag(0, 1), 0)
        self.assertEqual(zigzag(1, 0), 0)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            zigzag("3", 2)
        with self.assertRaises(TypeError):
            zigzag(3, "2")
        with self.assertRaises(ValueError):
            zigzag(-1, 2)
        with self.assertRaises(ValueError):
            zigzag(3, -1)

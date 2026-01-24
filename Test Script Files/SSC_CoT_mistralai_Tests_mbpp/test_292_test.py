import unittest
from mbpp_292_code import find

class TestFindFunction(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(find(12, 4), 3)
        self.assertEqual(find(48, 16), 3)

    def test_edge_input(self):
        self.assertEqual(find(0, 2), 0)
        self.assertEqual(find(1, 1), 1)
        self.assertEqual(find(2, 1), 2)

    def test_boundary_input(self):
        self.assertEqual(find(2147483647, 1), 2147483647)
        self.assertEqual(find(-2147483648, 1), -2147483647)
        self.assertEqual(find(2147483647, 2), 1073741823)
        self.assertEqual(find(-2147483648, 2), -1073741829)

    def test_invalid_input(self):
        self.assertRaises(TypeError, find, "n", 2)
        self.assertRaises(TypeError, find, 2, "m")
        self.assertRaises(TypeError, find, "n", "m")

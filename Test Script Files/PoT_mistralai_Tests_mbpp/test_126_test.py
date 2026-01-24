import unittest
from mbpp_126_code import sum

class TestSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum(12, 18), 6)
        self.assertEqual(sum(18, 12), 6)
        self.assertEqual(sum(12, 12), 0)
        self.assertEqual(sum(18, 12), 6)

    def test_edge_case(self):
        self.assertEqual(sum(1, 1), 0)
        self.assertEqual(sum(2, 1), 1)
        self.assertEqual(sum(1, 2), 1)

    def test_boundary_case(self):
        self.assertEqual(sum(0, 1), 0)
        self.assertEqual(sum(1, 0), 0)
        self.assertEqual(sum(0, 0), 0)

    def test_invalid_input(self):
        self.assertRaises(TypeError, sum, "a", 1)
        self.assertRaises(TypeError, sum, 1, "b")

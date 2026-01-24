import unittest
from mbpp_126_code import sum

class TestSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum(10, 20), 10)

    def test_boundary_case(self):
        self.assertEqual(sum(1, 1), 1)

    def test_edge_case(self):
        self.assertEqual(sum(1, 2), 1)
        self.assertEqual(sum(100, 200), 100)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum("10", 20)
        with self.assertRaises(TypeError):
            sum(10, "20")
        with self.assertRaises(TypeError):
            sum("10", "20")
        with self.assertRaises(ValueError):
            sum(0, 20)
        with self.assertRaises(ValueError):
            sum(20, 0)

import unittest
from mbpp_112_code import perimeter

class TestPerimeter(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(perimeter(5, 3), 18)
        self.assertEqual(perimeter(10, 20), 60)

    def test_edge_cases(self):
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(5, 0), 10)
        self.assertEqual(perimeter(1, 1), 5)

    def test_negative_inputs(self):
        self.assertRaises(TypeError, perimeter, -5, 3)
        self.assertRaises(TypeError, perimeter, 5, -3)

    def test_zero_inputs(self):
        self.assertRaises(ValueError, perimeter, 0, 0)

import unittest
from mbpp_355_code import count_Rectangles

class TestCountRectangles(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_Rectangles(1), 5)

    def test_boundary_conditions(self):
        self.assertEqual(count_Rectangles(0), 0)
        self.assertEqual(count_Rectangles(2), 29)

    def test_large_radius(self):
        self.assertGreater(count_Rectangles(10), 1000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Rectangles("radius")

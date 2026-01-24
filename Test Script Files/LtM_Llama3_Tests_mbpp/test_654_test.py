import unittest
from mbpp_654_code import rectangle_perimeter

class TestRectanglePerimeter(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(rectangle_perimeter(5, 3), 16)
        self.assertEqual(rectangle_perimeter(2, 4), 12)
        self.assertEqual(rectangle_perimeter(1, 1), 8)

    def test_edge_cases(self):
        self.assertEqual(rectangle_perimeter(0, 0), 0)
        self.assertEqual(rectangle_perimeter(10, 0), 20)
        self.assertEqual(rectangle_perimeter(0, 10), 20)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            rectangle_perimeter('a', 3)
        with self.assertRaises(TypeError):
            rectangle_perimeter(5, 'b')

import unittest
from mbpp_654_code import rectangle_perimeter

class TestRectanglePerimeter(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rectangle_perimeter(5, 3), 16)

    def test_edge_case(self):
        self.assertEqual(rectangle_perimeter(0, 0), 0)

    def test_edge_case2(self):
        self.assertEqual(rectangle_perimeter(10, 0), 20)

    def test_edge_case3(self):
        self.assertEqual(rectangle_perimeter(0, 10), 20)

    def test_edge_case4(self):
        self.assertEqual(rectangle_perimeter(10, 10), 40)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rectangle_perimeter('a', 3)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            rectangle_perimeter(5, 'b')

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            rectangle_perimeter('a', 'b')

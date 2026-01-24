import unittest
from mbpp_17_code import square_perimeter

class TestSquarePerimeter(unittest.TestCase):

    def test_typical(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_edge(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_edge2(self):
        self.assertEqual(square_perimeter(-5), 20)

    def test_edge3(self):
        self.assertEqual(square_perimeter(10), 40)

    def test_edge4(self):
        self.assertEqual(square_perimeter(-10), 40)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            square_perimeter('a')

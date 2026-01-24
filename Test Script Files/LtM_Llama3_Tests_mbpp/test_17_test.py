import unittest
from mbpp_17_code import square_perimeter

class TestSquarePerimeter(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(square_perimeter(1), 4)
        self.assertEqual(square_perimeter(2), 8)
        self.assertEqual(square_perimeter(3), 12)

    def test_edge_cases(self):
        self.assertEqual(square_perimeter(0), 0)
        self.assertEqual(square_perimeter(-1), 0)
        self.assertEqual(square_perimeter(10), 40)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            square_perimeter(None)
        with self.assertRaises(TypeError):
            square_perimeter("a")

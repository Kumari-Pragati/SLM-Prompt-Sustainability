import unittest
from mbpp_112_code import perimeter

class TestPerimeter(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(perimeter(10, 5), 30)

    def test_edge_cases(self):
        self.assertEqual(perimeter(0, 0), 0)
        self.assertEqual(perimeter(10, 0), 20)
        self.assertEqual(perimeter(0, 10), 20)

    def test_negative_inputs(self):
        with self.assertRaises(TypeError):
            perimeter(-10, 5)

        with self.assertRaises(TypeError):
            perimeter(10, -5)

    def test_non_numeric_inputs(self):
        with self.assertRaises(TypeError):
            perimeter('a', 5)

        with self.assertRaises(TypeError):
            perimeter(10, 'b')

    def test_mixed_type_inputs(self):
        with self.assertRaises(TypeError):
            perimeter(10, 'a')

        with self.assertRaises(TypeError):
            perimeter('a', 5)

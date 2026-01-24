import unittest
from mbpp_112_code import perimeter

class TestPerimeter(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(perimeter(10, 5), 30)
        self.assertEqual(perimeter(5, 10), 30)
        self.assertEqual(perimeter(10, 10), 40)

    def test_edge_cases(self):
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(10, 0), 20)
        self.assertEqual(perimeter(10, 10), 40)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            perimeter(None, 5)
        with self.assertRaises(TypeError):
            perimeter(10, None)
        with self.assertRaises(TypeError):
            perimeter(None, None)

import unittest
from mbpp_112_code import perimeter

class TestPerimeter(unittest.TestCase):

    def test_perimeter(self):
        self.assertEqual(perimeter(10, 5), 20)
        self.assertEqual(perimeter(5, 3), 16)
        self.assertEqual(perimeter(20, 10), 60)
        self.assertEqual(perimeter(0, 0), 0)
        self.assertEqual(perimeter(10, 0), 20)
        self.assertEqual(perimeter(0, 10), 20)

    def test_perimeter_negative(self):
        with self.assertRaises(TypeError):
            perimeter(-10, 5)
        with self.assertRaises(TypeError):
            perimeter(10, -5)

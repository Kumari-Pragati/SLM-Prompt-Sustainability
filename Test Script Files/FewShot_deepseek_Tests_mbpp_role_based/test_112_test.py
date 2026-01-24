import unittest
from mbpp_112_code import perimeter

class TestPerimeter(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(perimeter(10, 5), 30)

    def test_boundary_conditions(self):
        self.assertEqual(perimeter(0, 0), 0)
        self.assertEqual(perimeter(10, 0), 20)
        self.assertEqual(perimeter(0, 5), 10)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            perimeter('10', 5)
        with self.assertRaises(TypeError):
            perimeter(10, '5')
        with self.assertRaises(TypeError):
            perimeter('10', '5')

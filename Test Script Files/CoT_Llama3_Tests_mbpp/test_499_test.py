import unittest
from mbpp_499_code import diameter_circle

class TestDiameterCircle(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(diameter_circle(5), 10)
        self.assertEqual(diameter_circle(10), 20)
        self.assertEqual(diameter_circle(15), 30)

    def test_edge_cases(self):
        self.assertEqual(diameter_circle(0), 0)
        self.assertEqual(diameter_circle(-5), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            diameter_circle('a')
        with self.assertRaises(TypeError):
            diameter_circle(None)

    def test_boundary_conditions(self):
        self.assertEqual(diameter_circle(float('inf')), float('inf'))
        self.assertEqual(diameter_circle(-float('inf')), float('inf'))

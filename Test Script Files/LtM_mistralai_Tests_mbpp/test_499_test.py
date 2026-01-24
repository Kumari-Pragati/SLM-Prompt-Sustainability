import unittest
from mbpp_499_code import diameter_circle

class TestDiameterCircle(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(diameter_circle(1), 2)
        self.assertEqual(diameter_circle(3.14), 6.28)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(diameter_circle(0), 0)
        self.assertEqual(diameter_circle(-1), 2)
        self.assertEqual(diameter_circle(float('inf')), float('inf'))
        self.assertEqual(diameter_circle(complex(0, 0)), 0)

    def test_complex_input(self):
        self.assertEqual(diameter_circle(-3.14), 6.28)
        self.assertEqual(diameter_circle(complex(1, 2)), 4 + 2j + 2j)

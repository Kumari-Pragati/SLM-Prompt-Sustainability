import unittest
from mbpp_112_code import perimeter

class TestPerimeter(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(perimeter(5, 3), 18)

    def test_edge_case_zero(self):
        self.assertEqual(perimeter(0, 3), 6)
        self.assertEqual(perimeter(3, 0), 6)

    def test_edge_case_negative(self):
        self.assertEqual(perimeter(-5, 3), 10)
        self.assertEqual(perimeter(5, -3), 10)

    def test_edge_case_infinity(self):
        self.assertEqual(perimeter(float('inf'), 3), 6 + 2 * float('inf'))
        self.assertEqual(perimeter(3, float('inf')), 6 + 2 * float('inf'))

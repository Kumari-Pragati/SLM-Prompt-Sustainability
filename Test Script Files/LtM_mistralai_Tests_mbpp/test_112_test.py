import unittest
from mbpp_112_code import perimeter

class TestPerimeter(unittest.TestCase):

    def test_simple_positive(self):
        self.assertEqual(perimeter(2, 3), 12)

    def test_typical_positive(self):
        self.assertEqual(perimeter(5, 7), 28)

    def test_edge_zero(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_edge_negative(self):
        self.assertEqual(perimeter(-1, 2), 8)
        self.assertEqual(perimeter(2, -1), 8)

    def test_edge_large_positive(self):
        self.assertEqual(perimeter(1000000, 1000000), 4000004)

    def test_edge_large_negative(self):
        self.assertEqual(perimeter(-1000000, 1000000), 4000004)
        self.assertEqual(perimeter(1000000, -1000000), 4000004)

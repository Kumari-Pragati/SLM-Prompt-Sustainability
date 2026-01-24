import unittest
from mbpp_112_code import perimeter

class TestPerimeter(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(perimeter(10, 5), 20)

    def test_edge(self):
        self.assertEqual(perimeter(0, 0), 0)
        self.assertEqual(perimeter(10, 0), 20)
        self.assertEqual(perimeter(0, 10), 20)

    def test_edge2(self):
        self.assertEqual(perimeter(10, 10), 40)

    def test_edge3(self):
        self.assertEqual(perimeter(10, -5), 20)
        self.assertEqual(perimeter(-10, 5), 20)

    def test_edge4(self):
        self.assertEqual(perimeter(10, float('inf')), float('inf'))
        self.assertEqual(perimeter(float('inf'), 5), float('inf'))

    def test_edge5(self):
        self.assertEqual(perimeter(10, -float('inf')), float('inf'))
        self.assertEqual(perimeter(-10, 5), float('inf'))

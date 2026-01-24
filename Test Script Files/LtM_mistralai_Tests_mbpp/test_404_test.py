import unittest
from mbpp_404_code import minimum

class TestMinimum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(minimum(1, 2), 1)
        self.assertEqual(minimum(2, 1), 2)
        self.assertEqual(minimum(0, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(minimum(-10, -20), -10)
        self.assertEqual(minimum(20, 30), 20)
        self.assertEqual(minimum(float('inf'), 0), 0)
        self.assertEqual(minimum(0, float('inf')), float('inf'))

    def test_complex(self):
        self.assertEqual(minimum(-1, -2), -2)
        self.assertEqual(minimum(0, -1), -1)
        self.assertEqual(minimum(1.1, 1.2), 1.1)
        self.assertEqual(minimum(1.2, 1.1), 1.1)

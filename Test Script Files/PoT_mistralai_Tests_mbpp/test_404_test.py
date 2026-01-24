import unittest
from mbpp_404_code import minimum

class TestMinimum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(minimum(1, 2), 1)
        self.assertEqual(minimum(2, 1), 1)
        self.assertEqual(minimum(0, 0), 0)
        self.assertEqual(minimum(-1, 0), -1)
        self.assertEqual(minimum(0, -1), -1)

    def test_edge_cases(self):
        self.assertEqual(minimum(0, float('-inf')), 0)
        self.assertEqual(minimum(float('inf'), 0), 0)
        self.assertEqual(minimum(float('-inf'), float('-inf')), float('-inf'))
        self.assertEqual(minimum(float('inf'), float('inf')), float('inf'))

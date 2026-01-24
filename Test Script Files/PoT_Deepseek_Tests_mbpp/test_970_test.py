import unittest
from mbpp_970_code import min_of_two

class TestMinOfTwo(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(min_of_two(1, 2), 1)
        self.assertEqual(min_of_two(3, 2), 2)
        self.assertEqual(min_of_two(0, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(min_of_two(float('-inf'), 1), float('-inf'))
        self.assertEqual(min_of_two(1, float('-inf')), 1)
        self.assertEqual(min_of_two(float('inf'), 1), 1)
        self.assertEqual(min_of_two(1, float('inf')), 1)

    def test_corner_cases(self):
        self.assertEqual(min_of_two(float('-inf'), float('-inf')), float('-inf'))
        self.assertEqual(min_of_two(float('inf'), float('inf')), float('inf'))
        self.assertEqual(min_of_two(float('inf'), float('-inf')), float('-inf'))
        self.assertEqual(min_of_two(float('-inf'), float('inf')), float('-inf'))

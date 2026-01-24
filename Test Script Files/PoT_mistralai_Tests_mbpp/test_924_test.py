import unittest
from mbpp_924_code import max_of_two

class TestMaxOfTwo(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(max_of_two(5, 3), 5)
        self.assertEqual(max_of_two(-2, -5), -2)
        self.assertEqual(max_of_two(0, 1), 1)
        self.assertEqual(max_of_two(100, 100), 100)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(max_of_two(0, 0), 0)
        self.assertEqual(max_of_two(-1, 0), 0)
        self.assertEqual(max_of_two(0, -1), 0)
        self.assertEqual(max_of_two(-1, -1), -1)
        self.assertEqual(max_of_two(float('inf'), 0), float('inf'))
        self.assertEqual(max_of_two(0, float('inf')), float('inf'))

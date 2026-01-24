import unittest
from mbpp_901_code import smallest_multiple

class TestSmallestMultiple(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(smallest_multiple(3), 6)
        self.assertEqual(smallest_multiple(5), 10)
        self.assertEqual(smallest_multiple(7), 14)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(smallest_multiple(1), 1)
        self.assertEqual(smallest_multiple(2), 2)
        self.assertEqual(smallest_multiple(0), None)  # Assuming the function returns None for invalid input

    def test_corner_cases(self):
        self.assertEqual(smallest_multiple(30), 60)
        self.assertEqual(smallest_multiple(40), 80)
        self.assertEqual(smallest_multiple(50), 100)

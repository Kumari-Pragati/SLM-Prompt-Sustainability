import unittest
from mbpp_856_code import find_Min_Swaps

class TestFindMinSwaps(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(find_Min_Swaps([0, 1, 0, 1], 4), 2)

    def test_boundary_conditions(self):
        self.assertEqual(find_Min_Swaps([], 0), 0)
        self.assertEqual(find_Min_Swaps([0], 1), 0)
        self.assertEqual(find_Min_Swaps([1], 1), 0)

    def test_edge_cases(self):
        self.assertEqual(find_Min_Swaps([0, 0, 0, 0], 4), 0)
        self.assertEqual(find_Min_Swaps([1, 1, 1, 1], 4), 0)
        self.assertEqual(find_Min_Swaps([0, 1, 0, 1, 1, 0, 1, 0], 8), 2)

    def test_complex_cases(self):
        self.assertEqual(find_Min_Swaps([1, 0, 1, 0, 1, 0], 6), 2)
        self.assertEqual(find_Min_Swaps([0, 1, 0, 1, 1, 0, 0, 1, 0, 1], 10), 3)

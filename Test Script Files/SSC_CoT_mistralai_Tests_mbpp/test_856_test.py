import unittest
from mbpp_856_code import find_Min_Swaps

class TestFindMinSwaps(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(find_Min_Swaps([0, 1, 0, 1, 0], 5), 3)
        self.assertEqual(find_Min_Swaps([1, 0, 1, 1, 0], 5), 2)
        self.assertEqual(find_Min_Swaps([0, 1, 0, 1, 1], 5), 2)

    def test_edge_cases(self):
        self.assertEqual(find_Min_Swaps([0, 0, 0], 3), 0)
        self.assertEqual(find_Min_Swaps([1, 1, 1], 3), 0)
        self.assertEqual(find_Min_Swaps([0, 1, 0, 1, 0, 1], 6), 3)
        self.assertEqual(find_Min_Swaps([1, 0, 1, 0, 1, 0], 6), 3)

    def test_boundary_conditions(self):
        self.assertEqual(find_Min_Swaps([], 0), 0)
        self.assertEqual(find_Min_Swaps([0], 1), 0)
        self.assertEqual(find_Min_Swaps([1], 1), 0)
        self.assertEqual(find_Min_Swaps([0, 0], 2), 1)
        self.assertEqual(find_Min_Swaps([1, 1], 2), 1)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, find_Min_Swaps, ["a", "b"], 2)
        self.assertRaises(ValueError, find_Min_Swaps, [0, 1], -1)

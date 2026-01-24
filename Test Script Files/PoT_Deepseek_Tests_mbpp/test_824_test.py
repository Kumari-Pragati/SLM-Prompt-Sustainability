import unittest
from mbpp_824_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(remove_even([1, 2, 3, 4]), [1, 3])
        self.assertEqual(remove_even([10, 20, 30, 40]), [])
        self.assertEqual(remove_even([1, 3, 5, 7]), [1, 3, 5, 7])

    def test_edge_cases(self):
        self.assertEqual(remove_even([]), [])
        self.assertEqual(remove_even([2]), [])
        self.assertEqual(remove_even([1, 2, 3, 4, 5, 6]), [1, 3, 5])

    def test_boundary_cases(self):
        self.assertEqual(remove_even([0]), [])
        self.assertEqual(remove_even([-2]), [])
        self.assertEqual(remove_even([2, 4, 6, 8]), [])

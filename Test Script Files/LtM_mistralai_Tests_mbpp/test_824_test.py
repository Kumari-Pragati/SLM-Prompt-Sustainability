import unittest
from mbpp_824_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(remove_even([1, 2, 3, 4, 5]), [1, 3, 5])
        self.assertListEqual(remove_even([2, 4, 6]), [])
        self.assertListEqual(remove_even([0]), [])
        self.assertListEqual(remove_even([1, 1, 3]), [3])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(remove_even([-2, -4, -6]), [])
        self.assertListEqual(remove_even([2147483646, 2147483644]), [2147483644])
        self.assertListEqual(remove_even([-2147483646]), [-2147483646])
        self.assertListEqual(remove_even([-2147483648]), [])
        self.assertListEqual(remove_even([2147483647]), [2147483647])

    def test_complex_scenarios(self):
        self.assertListEqual(remove_even([0, 1, 2, 3, 4, 5]), [1, 3, 5])
        self.assertListEqual(remove_even([-1, 0, 1, 2, -2]), [1, -2])
        self.assertListEqual(remove_even([-1, 0, 1, -2, 2]), [1, -2])
        self.assertListEqual(remove_even([-1, 0, 1, 2, -2, 2]), [1, -2])

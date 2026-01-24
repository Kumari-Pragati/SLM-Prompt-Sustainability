import unittest
from mbpp_824_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(remove_even([1, 2, 3, 4, 5, 6]), [1, 3, 5])
        self.assertListEqual(remove_even([-1, -2, -3, -4, -5, -6]), [-1, -3, -5])
        self.assertListEqual(remove_even([0]), [])

    def test_edge_input(self):
        self.assertListEqual(remove_even([1, 0, 3]), [1, 3])
        self.assertListEqual(remove_even([2, 2]), [])
        self.assertListEqual(remove_even([-2, -2]), [])
        self.assertListEqual(remove_even([float('inf'), 2]), [float('inf')])
        self.assertListEqual(remove_even([-float('inf'), -2]), [-float('inf')])
        self.assertListEqual(remove_even([]), [])

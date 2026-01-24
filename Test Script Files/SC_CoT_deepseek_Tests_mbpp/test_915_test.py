import unittest
from mbpp_915_code import rearrange_numbs

class TestRearrangeNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rearrange_numbs([3, 2, 1]), [1, 2, 3])

    def test_edge_case(self):
        self.assertEqual(rearrange_numbs([0, 1, 2]), [0, 1, 2])

    def test_boundary_case(self):
        self.assertEqual(rearrange_numbs([0, 0, 0]), [0, 0, 0])

    def test_negative_numbers(self):
        self.assertEqual(rearrange_numbs([-3, -2, -1]), [-1, -2, -3])

    def test_zero_and_negative(self):
        self.assertEqual(rearrange_numbs([0, -1, 1]), [0, -1, 1])

    def test_large_numbers(self):
        self.assertEqual(rearrange_numbs([100, 200, 300]), [100, 200, 300])

    def test_with_duplicates(self):
        self.assertEqual(rearrange_numbs([3, 2, 2]), [2, 2, 3])

    def test_with_one_element(self):
        self.assertEqual(rearrange_numbs([1]), [1])

    def test_with_zero(self):
        self.assertEqual(rearrange_numbs([0]), [0])

    def test_with_negative_zero(self):
        self.assertEqual(rearrange_numbs([-0]), [-0])

    def test_with_empty_list(self):
        self.assertEqual(rearrange_numbs([]), [])

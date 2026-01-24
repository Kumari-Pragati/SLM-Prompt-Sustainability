import unittest
from mbpp_915_code import rearrange_numbs

class TestRearrangeNums(unittest.TestCase):

    def test_rearrange_numbs(self):
        self.assertEqual(rearrange_numbs([0, 1, 2, 3, 4]), [0, 4, 3, 2, 1])
        self.assertEqual(rearrange_numbs([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])
        self.assertEqual(rearrange_numbs([5, 6, 7, 8, 9]), [0, 9, 8, 7, 6])
        self.assertEqual(rearrange_numbs([-1, 0, 1]), [0, 1, -1])
        self.assertEqual(rearrange_numbs([1, 2, 3, 4, 5]), [0, 5, 4, 3, 2])
        self.assertEqual(rearrange_numbs([0, -1, -2, -3, -4]), [0, -1, -2, -3, -4])
        self.assertEqual(rearrange_numbs([0]), [0])
        self.assertEqual(rearrange_numbs([]), [])

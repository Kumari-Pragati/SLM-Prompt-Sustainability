import unittest
from mbpp_895_code import max_sum_subseq

class TestMaxSumSubseq(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(max_sum_subseq([1]), 1)

    def test_two_elements(self):
        self.assertEqual(max_sum_subseq([1, 2]), 2)
        self.assertEqual(max_sum_subseq([-1, -2]), -1)

    def test_typical_case(self):
        self.assertEqual(max_sum_subseq([3, 4, 5, 6]), 15)

    def test_edge_case(self):
        self.assertEqual(max_sum_subseq([-1, -2, -3, -4]), 0)

    def test_corner_case(self):
        self.assertEqual(max_sum_subseq([-1, -2, -3, -4, 10]), 10)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_sum_subseq("1,2,3")

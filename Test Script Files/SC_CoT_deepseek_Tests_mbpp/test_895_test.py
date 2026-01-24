import unittest
from mbpp_895_code import max_sum_subseq

class TestMaxSumSubseq(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(max_sum_subseq([5]), 5)

    def test_two_elements(self):
        self.assertEqual(max_sum_subseq([5, 10]), 15)
        self.assertEqual(max_sum_subseq([10, 5]), 15)

    def test_typical_case(self):
        self.assertEqual(max_sum_subseq([3, 5, 8, 9]), 17)

    def test_edge_cases(self):
        self.assertEqual(max_sum_subseq([-1, -2, -3]), -1)
        self.assertEqual(max_sum_subseq([0, 0, 0]), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_sum_subseq("1, 2, 3")
        with self.assertRaises(TypeError):
            max_sum_subseq(None)
        with self.assertRaises(TypeError):
            max_sum_subseq(1)

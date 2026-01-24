import unittest
from mbpp_682_code import mul_list

class TestMulList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(mul_list([1, 2, 3], [4, 5, 6]), [4, 10, 18])
        self.assertEqual(mul_list([0], [1, 2, 3]), [0, 0, 0])
        self.assertEqual(mul_list([1, 0, 3], [4, 0, 5]), [0, 0, 15])

    def test_edge_case_empty_lists(self):
        self.assertEqual(mul_list([], []), [])
        self.assertEqual(mul_list([1], []), [])
        self.assertEqual(mul_list([], [1]), [])

    def test_edge_case_single_element(self):
        self.assertEqual(mul_list([1], [2]), [2])
        self.assertEqual(mul_list([2], [1]), [2])

    def test_corner_case_mixed_zeros(self):
        self.assertEqual(mul_list([0, 1, 0], [2, 0, 3]), [0, 0, 0])
        self.assertEqual(mul_list([2, 0, 3], [0, 1, 0]), [0, 0, 0])

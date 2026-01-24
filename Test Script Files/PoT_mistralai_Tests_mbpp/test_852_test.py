import unittest
from mbpp_852_code import remove_negs

class TestRemoveNegs(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_negs([]), [])

    def test_positive_list(self):
        self.assertEqual(remove_negs([1, 2, 3, -1, 4, -2]), [1, 3, 4])

    def test_negative_list(self):
        self.assertEqual(remove_negs([-1, -2, -3]), [])

    def test_mixed_list(self):
        self.assertEqual(remove_negs([0, -1, 2, -3, 4, -5]), [0, 2, 4])

    def test_boundary_zero(self):
        self.assertEqual(remove_negs([0]), [0])

    def test_edge_case_min_int(self):
        self.assertEqual(remove_negs([-2147483648]), [-2147483647])

    def test_edge_case_max_int(self):
        self.assertEqual(remove_negs([2147483647]), [2147483647])

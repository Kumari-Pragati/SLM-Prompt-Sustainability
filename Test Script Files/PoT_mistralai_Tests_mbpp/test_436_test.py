import unittest
from mbpp_436_code import neg_nos

class TestNegNos(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(neg_nos([-1, 0, 2, -3]), [-1, -3])

    def test_edge_case_empty_list(self):
        self.assertIsNone(neg_nos([]))

    def test_edge_case_single_positive_number(self):
        self.assertIsNone(neg_nos([2]))

    def test_edge_case_single_zero(self):
        self.assertIsNone(neg_nos([0]))

    def test_edge_case_single_negative_number(self):
        self.assertEqual(neg_nos([-1]), -1)

    def test_corner_case_negative_numbers_only(self):
        self.assertEqual(neg_nos([-1, -2, -3]), [-1, -2, -3])

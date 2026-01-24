import unittest
from mbpp_672_code import max_of_three

class TestMaxOfThree(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_of_three(1, 2, 3), 3)

    def test_edge_case_equal(self):
        self.assertEqual(max_of_three(1, 1, 1), 1)

    def test_edge_case_reverse_order(self):
        self.assertEqual(max_of_three(3, 2, 1), 3)

    def test_edge_case_reverse_order_with_duplicates(self):
        self.assertEqual(max_of_three(3, 2, 2), 3)

    def test_edge_case_reverse_order_with_duplicates_and_zero(self):
        self.assertEqual(max_of_three(3, 2, 0), 3)

    def test_edge_case_reverse_order_with_duplicates_and_negative(self):
        self.assertEqual(max_of_three(3, 2, -1), 3)

    def test_edge_case_reverse_order_with_duplicates_and_negative_and_zero(self):
        self.assertEqual(max_of_three(3, 2, -1), 3)

    def test_edge_case_reverse_order_with_duplicates_and_negative_and_zero_and_negative(self):
        self.assertEqual(max_of_three(3, 2, -1, -2), 3)

    def test_edge_case_reverse_order_with_duplicates_and_negative_and_zero_and_negative_and_zero(self):
        self.assertEqual(max_of_three(3, 2, -1, -2, 0), 3)

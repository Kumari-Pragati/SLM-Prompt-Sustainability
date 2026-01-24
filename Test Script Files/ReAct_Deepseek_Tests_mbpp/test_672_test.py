import unittest
from mbpp_672_code import max_of_three

class TestMaxOfThree(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_of_three(10, 20, 15), 20)

    def test_edge_case_equal_numbers(self):
        self.assertEqual(max_of_three(10, 10, 10), 10)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(max_of_three(-10, -20, -15), -10)

    def test_edge_case_max_first(self):
        self.assertEqual(max_of_three(30, 10, 20), 30)

    def test_edge_case_max_last(self):
        self.assertEqual(max_of_three(10, 20, 30), 30)

    def test_edge_case_max_middle(self):
        self.assertEqual(max_of_three(10, 30, 20), 30)

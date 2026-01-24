import unittest
from mbpp_672_code import max_of_three

class TestMaxOfThree(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_of_three(5, 3, 1), 5)
        self.assertEqual(max_of_three(-2, -5, -8), -2)
        self.assertEqual(max_of_three(10, 9, 8), 10)

    def test_edge_case_zero(self):
        self.assertEqual(max_of_three(0, 3, 1), 3)
        self.assertEqual(max_of_three(3, 0, 1), 3)
        self.assertEqual(max_of_three(0, 0, 1), 1)

    def test_edge_case_equal(self):
        self.assertEqual(max_of_three(3, 3, 3), 3)
        self.assertEqual(max_of_three(-3, -3, -3), -3)

    def test_boundary_case_min_positive(self):
        self.assertEqual(max_of_three(1, 2, 0), 2)

    def test_boundary_case_min_negative(self):
        self.assertEqual(max_of_three(-1, -2, -3), -1)

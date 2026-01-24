import unittest
from mbpp_404_code import minimum

class TestMinimum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(minimum(2, 3), 2)

    def test_edge_case_a_smaller_than_b(self):
        self.assertEqual(minimum(1, 5), 1)

    def test_edge_case_b_smaller_than_a(self):
        self.assertEqual(minimum(5, 1), 1)

    def test_edge_case_a_equal_to_b(self):
        self.assertEqual(minimum(2, 2), 2)

    def test_edge_case_b_equal_to_a(self):
        self.assertEqual(minimum(2, 2), 2)

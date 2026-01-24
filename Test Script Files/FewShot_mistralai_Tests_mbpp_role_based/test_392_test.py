import unittest
from mbpp_392_code import get_max_sum

class TestGetMaxSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(get_max_sum(10), 27)

    def test_edge_case_small(self):
        self.assertEqual(get_max_sum(1), 1)

    def test_edge_case_large(self):
        self.assertEqual(get_max_sum(100), 354224)

    def test_boundary_case_zero(self):
        self.assertEqual(get_max_sum(0), 0)

    def test_boundary_case_negative(self):
        self.assertEqual(get_max_sum(-1), TraceError)

import unittest
from mbpp_568_code import empty_list

class TestEmptyList(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(empty_list(1), [{}]),

    def test_typical_case(self):
        self.assertEqual(empty_list(3), [{}, {}, {}])

    def test_edge_case_zero(self):
        self.assertEqual(empty_list(0), [])

    def test_edge_case_negative(self):
        self.assertEqual(empty_list(-1), [])

    def test_boundary_case_max(self):
        self.assertEqual(len(empty_list(1000)), 1000)

    def test_complex_case(self):
        self.assertEqual(empty_list(10), [{}]*10)

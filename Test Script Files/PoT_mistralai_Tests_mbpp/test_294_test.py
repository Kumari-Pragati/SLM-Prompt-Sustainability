import unittest
from mbpp_294_code import max_val

class TestMaxVal(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5]), 5)

    def test_edge_case_empty_list(self):
        self.assertEqual(max_val([]), None)

    def test_edge_case_single_element(self):
        self.assertEqual(max_val([1]), 1)

    def test_edge_case_all_non_int(self):
        self.assertEqual(max_val(['a', 'b', 'c']), None)

    def test_edge_case_all_negative_int(self):
        self.assertEqual(max_val([-1, -2, -3]), -1)

    def test_corner_case_mixed_types(self):
        self.assertEqual(max_val([1, '2', 3]), 3)

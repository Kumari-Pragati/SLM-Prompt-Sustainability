import unittest
from mbpp_410_code import min_val

class TestMinVal(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_val([1, 2, 3, 4, 5]), 1)
        self.assertEqual(min_val([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(min_val([0, 0, 0]), 0)

    def test_edge_case_empty_list(self):
        self.assertIsNone(min_val([]))

    def test_edge_case_single_item(self):
        self.assertEqual(min_val([1]), 1)
        self.assertEqual(min_val([-1]), -1)

    def test_edge_case_non_integer(self):
        self.assertIsNone(min_val(['a', 1, 'b', 2]))

    def test_corner_case_mixed_types(self):
        self.assertIsNone(min_val([1, 'a', 2, 'b', 3]))

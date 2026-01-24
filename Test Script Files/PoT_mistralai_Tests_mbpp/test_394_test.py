import unittest
from mbpp_394_code import check_distinct

class TestCheckDistinct(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_distinct((1, 2, 3, 4, 5)))
        self.assertTrue(check_distinct((5, 4, 3, 2, 1)))
        self.assertTrue(check_distinct((1.0, 2.0, 3.0, 4.0, 5.0)))

    def test_edge_case_empty(self):
        self.assertTrue(check_distinct([]))

    def test_edge_case_single_element(self):
        self.assertTrue(check_distinct((1,)))

    def test_edge_case_duplicate(self):
        self.assertFalse(check_distinct((1, 1, 2, 3)))
        self.assertFalse(check_distinct((1.0, 1.0, 2.0, 3.0)))

    def test_corner_case_mixed_types(self):
        self.assertFalse(check_distinct((1, "2", 3)))
        self.assertFalse(check_distinct((1, 2, "3")))

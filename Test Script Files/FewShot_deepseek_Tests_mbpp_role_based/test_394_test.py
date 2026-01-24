import unittest
from mbpp_394_code import check_distinct

class TestCheckDistinct(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(check_distinct((1, 2, 3)))

    def test_edge_condition(self):
        self.assertTrue(check_distinct(()))

    def test_boundary_condition(self):
        self.assertTrue(check_distinct((1,)))
        self.assertFalse(check_distinct((1, 1)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_distinct(123)
        with self.assertRaises(TypeError):
            check_distinct('123')

import unittest
from mbpp_222_code import check_type

class TestCheckType(unittest.TestCase):
    def test_simple_valid(self):
        self.assertTrue(check_type((1, 1)))
        self.assertTrue(check_type((1, 1.0)))
        self.assertTrue(check_type((1, '1')))

    def test_edge_empty(self):
        self.assertFalse(check_type(()))

    def test_edge_single_element(self):
        self.assertTrue(check_type((1,)))

    def test_edge_mixed_types(self):
        self.assertFalse(check_type((1, '2', 3.0)))

    def test_edge_all_same_type(self):
        self.assertTrue(check_type((1, 1, 1)))

    def test_edge_all_same_type_with_non_integer(self):
        self.assertTrue(check_type((1.0, 1.0, 1.0)))

    def test_edge_all_same_type_with_non_string(self):
        self.assertTrue(check_type((1.0, 1.0, 1.0)))

    def test_edge_all_same_type_with_non_int(self):
        self.assertTrue(check_type((1.0, 1.0, 1.0)))

    def test_edge_mixed_types_with_non_integer(self):
        self.assertFalse(check_type((1, '2', 3.0)))

    def test_edge_mixed_types_with_non_string(self):
        self.assertFalse(check_type((1, 2, '3')))

    def test_edge_mixed_types_with_non_int(self):
        self.assertFalse(check_type((1, 2, 3.0)))

import unittest
from mbpp_222_code import check_type

class TestCheckType(unittest.TestCase):

    def test_typical_case_same_type(self):
        self.assertTrue(check_type((1, 2, 3)))

    def test_typical_case_different_type(self):
        self.assertTrue(check_type((1, '2', 3)))

    def test_edge_case_single_element(self):
        self.assertTrue(check_type((1,)))

    def test_edge_case_empty_tuple(self):
        self.assertTrue(check_type(()))

    def test_error_case_mixed_types(self):
        self.assertFalse(check_type((1, '2', None)))

    def test_error_case_mixed_types_with_different_base_type(self):
        self.assertFalse(check_type((1, '2', 3.0)))

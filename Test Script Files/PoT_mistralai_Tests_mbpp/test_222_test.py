import unittest
from mbpp_222_code import check_type

class TestCheckType(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_type((1, 2, 3)))
        self.assertTrue(check_type(('a', 'b', 'c')))
        self.assertTrue(check_type([1, 2, 3]))

    def test_edge_case_mixed_types(self):
        self.assertFalse(check_type((1, 'a', 3)))
        self.assertFalse(check_type(('a', 1, 'b')))
        self.assertFalse(check_type([1, 'a', 3]))

    def test_boundary_case_empty_tuple(self):
        self.assertTrue(check_type(()))

    def test_boundary_case_single_element(self):
        self.assertTrue(check_type((1,)))
        self.assertTrue(check_type(('a',)))
        self.assertTrue(check_type([1]))

    def test_corner_case_none_type(self):
        self.assertFalse(check_type((None, 1, 2)))
        self.assertFalse(check_type(('a', None, 'b')))
        self.assertFalse(check_type([None, 1, 2]))

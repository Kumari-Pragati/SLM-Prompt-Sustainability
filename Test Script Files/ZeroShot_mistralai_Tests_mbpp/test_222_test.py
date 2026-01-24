import unittest
from mbpp_222_code import check_type

class TestCheckType(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(check_type([]))

    def test_single_element(self):
        self.assertTrue(check_type([1]))
        self.assertTrue(check_type([str("a")]))
        self.assertTrue(check_type([float(3.14)]))
        self.assertTrue(check_type([None]])

    def test_multiple_elements(self):
        self.assertTrue(check_type([1, 1]))
        self.assertTrue(check_type([str("a"), str("a")]))
        self.assertTrue(check_type([float(3.14), float(3.14)]))
        self.assertTrue(check_type([None, None]))

    def test_mixed_types(self):
        self.assertFalse(check_type([1, "a"]))
        self.assertFalse(check_type([1, float(3.14)]))
        self.assertFalse(check_type([str("a"), float(3.14)]))
        self.assertFalse(check_type([1, None]))

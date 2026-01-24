import unittest
from mbpp_222_code import check_type

class TestCheckType(unittest.TestCase):

    def test_same_type(self):
        self.assertTrue(check_type((1, 2, 3)))

    def test_mixed_types(self):
        self.assertFalse(check_type((1, 'a', 3.0)))

    def test_all_strings(self):
        self.assertFalse(check_type(("a", "b", "c")))

    def test_all_integers(self):
        self.assertTrue(check_type((1, 2, 3)))

    def test_all_floats(self):
        self.assertTrue(check_type((1.0, 2.0, 3.0)))

    def test_empty_tuple(self):
        self.assertTrue(check_type(()))

    def test_single_element_tuple(self):
        self.assertTrue(check_type((1,)))

    def test_tuple_with_one_non_matching_element(self):
        self.assertFalse(check_type((1, 2, "a")))

    def test_tuple_with_multiple_non_matching_elements(self):
        self.assertFalse(check_type((1, 2, "a", 3.0)))

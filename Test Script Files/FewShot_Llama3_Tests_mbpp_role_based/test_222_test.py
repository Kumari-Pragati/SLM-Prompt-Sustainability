import unittest
from mbpp_222_code import check_type

class TestCheckType(unittest.TestCase):
    def test_all_integers(self):
        self.assertTrue(check_type((1, 2, 3)))

    def test_all_strings(self):
        self.assertTrue(check_type(("a", "b", "c")))

    def test_mixed_types(self):
        self.assertFalse(check_type((1, "a", 3)))

    def test_empty_tuple(self):
        self.assertTrue(check_type(()))

    def test_single_element_tuple(self):
        self.assertTrue(check_type((1,)))

    def test_tuple_with_duplicates(self):
        self.assertTrue(check_type((1, 1, 1)))

    def test_tuple_with_nonetype(self):
        self.assertFalse(check_type((1, None, 3)))

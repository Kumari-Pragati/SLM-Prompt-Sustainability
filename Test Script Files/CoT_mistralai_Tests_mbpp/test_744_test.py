import unittest
from mbpp_744_code import check_none

class TestCheckNone(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertTrue(check_none(()))

    def test_tuple_with_none(self):
        self.assertTrue(check_none((1, None, 3)))

    def test_tuple_without_none(self):
        self.assertFalse(check_none((1, 2, 3)))

    def test_single_none(self):
        self.assertTrue(check_none(None))

    def test_single_non_none(self):
        self.assertFalse(check_none(1))

    def test_list_with_none(self):
        self.assertTrue(check_none([1, None, 3]))

    def test_list_without_none(self):
        self.assertFalse(check_none([1, 2, 3]))

    def test_mixed_tuple_list(self):
        self.assertTrue(check_none((1, [None, 3])))

    def test_invalid_input_string(self):
        self.assertRaises(TypeError, check_none, "string")

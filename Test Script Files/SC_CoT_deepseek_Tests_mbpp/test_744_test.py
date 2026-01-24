import unittest
from mbpp_744_code import check_none

class TestCheckNone(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_none((1, None, 2)))

    def test_no_none(self):
        self.assertFalse(check_none((1, 2, 3)))

    def test_empty_tuple(self):
        self.assertFalse(check_none(()))

    def test_single_none(self):
        self.assertTrue(check_none((None,)))

    def test_mixed_types(self):
        self.assertTrue(check_none((None, 'test', 123)))

    def test_none_as_first_element(self):
        self.assertTrue(check_none((None, 1, 2)))

    def test_none_as_last_element(self):
        self.assertTrue(check_none((1, 2, None)))

    def test_none_as_only_element(self):
        self.assertTrue(check_none((None,)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_none(123)

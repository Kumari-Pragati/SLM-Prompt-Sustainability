import unittest
from mbpp_878_code import check_tuples

class TestCheckTuples(unittest.TestCase):
    def test_valid_tuples(self):
        self.assertTrue(check_tuples((1, 2, 3), {1, 2, 3}))
        self.assertTrue(check_tuples((4, 5, 6), {4, 5, 6, 7}))
        self.assertTrue(check_tuples((7, 8, 9), {7, 8, 9, 10}))

    def test_invalid_tuples(self):
        self.assertFalse(check_tuples((1, 2, 3), {1, 2, 4}))
        self.assertFalse(check_tuples((4, 5, 6), {4, 5, 9}))
        self.assertFalse(check_tuples((7, 8, 9), {7, 8, 11}))

    def test_empty_tuple(self):
        self.assertTrue(check_tuples((), set()))

    def test_empty_set(self):
        self.assertTrue(check_tuples((1,), {}))

    def test_single_element_tuple(self):
        self.assertTrue(check_tuples((1,), {1}))

    def test_single_element_set(self):
        self.assertTrue(check_tuples((1,), {1}))

    def test_none_tuple(self):
        self.assertRaises(TypeError, check_tuples, (None,))

    def test_none_set(self):
        self.assertRaises(TypeError, check_tuples, (1, None))

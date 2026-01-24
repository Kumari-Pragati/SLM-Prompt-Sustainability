import unittest
from mbpp_878_code import check_tuples

class TestCheckTuples(unittest.TestCase):

    def test_check_tuples_with_elements_in_set(self):
        self.assertTrue(check_tuples((1, 2, 3), {1, 2, 3}))

    def test_check_tuples_with_elements_not_in_set(self):
        self.assertFalse(check_tuples((1, 2, 3), {4, 5, 6}))

    def test_check_tuples_with_empty_tuple(self):
        self.assertTrue(check_tuples((), set()))

    def test_check_tuples_with_empty_set(self):
        self.assertTrue(check_tuples((1,), {}))

    def test_check_tuples_with_single_element(self):
        self.assertTrue(check_tuples((1,), {1}))
        self.assertFalse(check_tuples((2,), {1}))

    def test_check_tuples_with_set_containing_single_element(self):
        self.assertTrue(check_tuples((1,), {1}))
        self.assertFalse(check_tuples((2,), {1}))

    def test_check_tuples_with_none_type_input(self):
        self.assertRaises(TypeError, check_tuples, None, {1, 2, 3})

    def test_check_tuples_with_set_containing_none(self):
        self.assertRaises(TypeError, check_tuples, (1, 2, 3), {None})

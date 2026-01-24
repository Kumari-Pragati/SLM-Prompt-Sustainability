import unittest
from mbpp_878_code import check_tuples

class TestCheckTuples(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertTrue(check_tuples((), set()))

    def test_single_element_tuple(self):
        self.assertTrue(check_tuples((1,), {1}))
        self.assertFalse(check_tuples((1,), {2}))

    def test_multiple_elements_tuples(self):
        self.assertTrue(check_tuples((1, 2, 3), {1, 2, 3}))
        self.assertFalse(check_tuples((1, 2, 3), {1, 2, 4}))

    def test_tuples_with_repeated_elements(self):
        self.assertTrue(check_tuples((1, 1, 2), {1, 2}))
        self.assertFalse(check_tuples((1, 1, 2), {1, 3}))

    def test_tuples_with_empty_set(self):
        self.assertTrue(check_tuples((1,), set()))

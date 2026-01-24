import unittest
from mbpp_878_code import check_tuples

class TestCheckTuples(unittest.TestCase):

    def test_all_elements_in_K(self):
        self.assertTrue(check_tuples((1, 2, 3), {1, 2, 3}))
        self.assertTrue(check_tuples(('a', 'b', 'c'), {'a', 'b', 'c'}))

    def test_some_elements_not_in_K(self):
        self.assertFalse(check_tuples((1, 2, 3), {1, 2}))
        self.assertFalse(check_tuples(('a', 'b', 'c'), {'a', 'b'}))

    def test_empty_tuple(self):
        self.assertTrue(check_tuples((), {}))

    def test_K_is_empty(self):
        self.assertFalse(check_tuples((1, 2, 3), set()))

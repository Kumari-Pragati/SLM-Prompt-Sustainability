import unittest
from mbpp_878_code import check_tuples

class TestCheckTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_tuples((1, 2, 3), {1, 2, 3}))
        self.assertTrue(check_tuples(('a', 'b', 'c'), {'a', 'b', 'c'}))

    def test_empty_tuple(self):
        self.assertTrue(check_tuples((), {}))

    def test_empty_set(self):
        self.assertTrue(check_tuples((1, 2, 3), set()))

    def test_all_elements_in_tuple(self):
        self.assertTrue(check_tuples((1, 2, 3), {1, 2, 3, 4, 5}))

    def test_some_elements_in_tuple(self):
        self.assertFalse(check_tuples((1, 2, 3), {4, 5, 6}))

    def test_no_elements_in_tuple(self):
        self.assertFalse(check_tuples((1, 2, 3), {4, 5, 6, 7, 8, 9}))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_tuples(123, {1, 2, 3})
        with self.assertRaises(TypeError):
            check_tuples((1, 2, 3), 123)

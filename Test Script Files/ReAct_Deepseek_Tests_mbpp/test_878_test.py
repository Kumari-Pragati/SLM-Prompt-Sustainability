import unittest
from mbpp_878_code import check_tuples

class TestCheckTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_tuples((1, 2, 3), {1, 2, 3, 4, 5}))
        self.assertTrue(check_tuples(('a', 'b', 'c'), {'a', 'b', 'c', 'd', 'e'}))

    def test_empty_tuple(self):
        self.assertTrue(check_tuples((), {1, 2, 3, 4, 5}))

    def test_tuple_with_one_element(self):
        self.assertTrue(check_tuples((1,), {1, 2, 3, 4, 5}))
        self.assertFalse(check_tuples((6,), {1, 2, 3, 4, 5}))

    def test_tuple_with_all_elements(self):
        self.assertTrue(check_tuples((1, 2, 3), {1, 2, 3}))

    def test_tuple_with_some_elements(self):
        self.assertFalse(check_tuples((1, 2, 3), {4, 5, 6}))

    def test_empty_set(self):
        self.assertFalse(check_tuples((1, 2, 3), set()))

    def test_none_in_tuple(self):
        with self.assertRaises(TypeError):
            check_tuples(None, {1, 2, 3})

    def test_none_in_set(self):
        with self.assertRaises(TypeError):
            check_tuples((1, 2, 3), None)

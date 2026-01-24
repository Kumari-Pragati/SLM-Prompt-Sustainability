import unittest
from mbpp_878_code import check_tuples

class TestCheckTuples(unittest.TestCase):

    def test_normal(self):
        self.assertTrue(check_tuples((1, 2, 3), {1, 2, 3}))
        self.assertTrue(check_tuples(('a', 'b', 'c'), {'a', 'b', 'c'}))

    def test_edge_cases(self):
        self.assertFalse(check_tuples((1, 2, 3), {1, 2}))
        self.assertFalse(check_tuples((1, 2, 3), {3, 2, 1}))
        self.assertFalse(check_tuples(('a', 'b', 'c'), {'a', 'b', 'd'}))
        self.assertFalse(check_tuples(('a', 'b', 'c'), {'c', 'b', 'a'}))

    def test_empty_inputs(self):
        self.assertFalse(check_tuples((), {}))
        self.assertFalse(check_tuples((), {1, 2, 3}))
        self.assertFalse(check_tuples({}, {}))
        self.assertFalse(check_tuples({}, {1, 2, 3}))

    def test_single_element(self):
        self.assertTrue(check_tuples((1,), {1}))
        self.assertFalse(check_tuples((1,), {2}))
        self.assertFalse(check_tuples({1}, {1}))
        self.assertFalse(check_tuples({1}, {2}))

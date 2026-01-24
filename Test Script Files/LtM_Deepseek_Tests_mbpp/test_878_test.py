import unittest
from mbpp_878_code import check_tuples

class TestCheckTuples(unittest.TestCase):

    def test_simple_case(self):
        self.assertTrue(check_tuples((1, 2, 3), {1, 2, 3}))

    def test_empty_tuple(self):
        self.assertTrue(check_tuples((), {}))

    def test_empty_set(self):
        self.assertFalse(check_tuples((1, 2, 3), set()))

    def test_all_elements_in_set(self):
        self.assertTrue(check_tuples((1, 2, 3), {1, 2, 3, 4, 5}))

    def test_some_elements_in_set(self):
        self.assertFalse(check_tuples((1, 2, 3), {4, 5, 6}))

    def test_duplicate_elements(self):
        self.assertTrue(check_tuples((1, 2, 2), {1, 2}))

    def test_large_tuple(self):
        self.assertTrue(check_tuples(tuple(range(1, 1001)), set(range(1, 1001))))

    def test_large_set(self):
        self.assertFalse(check_tuples(tuple(range(1, 1001)), set(range(1002, 2002))))

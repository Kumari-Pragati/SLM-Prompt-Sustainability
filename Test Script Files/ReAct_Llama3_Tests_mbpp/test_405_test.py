import unittest
from mbpp_405_code import check_tuplex

class TestCheckTuplex(unittest.TestCase):

    def test_true(self):
        self.assertTrue(check_tuplex([1, 2, 3], [1, 2, 3]))

    def test_false(self):
        self.assertFalse(check_tuplex([1, 2, 3], [4, 5, 6]))

    def test_empty(self):
        self.assertFalse(check_tuplex([], [1, 2, 3]))

    def test_single_element(self):
        self.assertTrue(check_tuplex([1], [1]))

    def test_empty_tuple(self):
        self.assertFalse(check_tuplex([1, 2, 3], []))

    def test_tuple_in_tuplex(self):
        self.assertTrue(check_tuplex([1, 2, 3], [1]))

    def test_tuple_not_in_tuplex(self):
        self.assertFalse(check_tuplex([1, 2, 3], [4]))

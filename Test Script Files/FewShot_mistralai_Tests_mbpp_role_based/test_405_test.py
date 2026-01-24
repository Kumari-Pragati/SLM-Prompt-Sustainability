import unittest
from mbpp_405_code import check_tuplex

class TestCheckTuplex(unittest.TestCase):
    def test_contains_valid_tuple(self):
        self.assertTrue(check_tuplex([(1, 2), (3, 4), (5, 6)], (3, 4)))

    def test_does_not_contain_valid_tuple(self):
        self.assertFalse(check_tuplex([(1, 2), (3, 4), (5, 6)], (7, 8)))

    def test_empty_list(self):
        self.assertFalse(check_tuplex([]))

    def test_tuple_not_in_list(self):
        self.assertFalse(check_tuplex([(1, 2), (3, 4), (5, 6)], (1, 2)))

    def test_tuple_not_iterable(self):
        self.assertRaises(TypeError, check_tuplex, [(1, 2), (3, 4), (5, 6)], "not a tuple")

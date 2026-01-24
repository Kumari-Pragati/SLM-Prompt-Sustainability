import unittest
from mbpp_405_code import check_tuplex

class TestCheckTuplex(unittest.TestCase):
    def test_correct_input(self):
        self.assertTrue(check_tuplex([(1, 2), (3, 4), (5, 6)], (3, 4)))
        self.assertTrue(check_tuplex(set([(1, 2), (3, 4), (5, 6)]), (3, 4)))

    def test_empty_input(self):
        self.assertFalse(check_tuplex([], (1, 2)))
        self.assertFalse(check_tuplex(set(), (1, 2)))

    def test_none_input(self):
        self.assertFalse(check_tuplex(None, (1, 2)))

    def test_invalid_input(self):
        self.assertRaises(TypeError, check_tuplex, 'invalid', (1, 2))
        self.assertRaises(TypeError, check_tuplex, [1, 2], 'invalid')

    def test_duplicate_tuples(self):
        self.assertTrue(check_tuplex([(1, 2), (1, 2), (3, 4)], (1, 2)))
        self.assertTrue(check_tuplex(set([(1, 2), (1, 2), (3, 4)]), (1, 2)))

    def test_single_tuple(self):
        self.assertFalse(check_tuplex([(1, 2)], (3, 4)))
        self.assertFalse(check_tuplex(set([(1, 2)]), (3, 4)))

    def test_empty_tuple(self):
        self.assertFalse(check_tuplex([], ()))
        self.assertFalse(check_tuplex(set(), ()))

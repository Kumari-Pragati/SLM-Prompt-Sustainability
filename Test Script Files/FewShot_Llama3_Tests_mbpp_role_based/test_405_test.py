import unittest
from mbpp_405_code import check_tuplex

class TestCheckTuplex(unittest.TestCase):
    def test_true_positive(self):
        self.assertTrue(check_tuplex([1, 2, 3, 4], [1, 2, 3]))

    def test_true_negative(self):
        self.assertFalse(check_tuplex([1, 2, 3, 4], [5, 6]))

    def test_false_positive(self):
        self.assertFalse(check_tuplex([1, 2, 3, 4], [1, 2]))

    def test_false_negative(self):
        self.assertTrue(check_tuplex([1, 2, 3, 4], [1, 2, 3, 4]))

    def test_empty_tuple(self):
        self.assertFalse(check_tuplex([], [1, 2]))

    def test_empty_tuplex(self):
        self.assertFalse(check_tuplex([1, 2], []))

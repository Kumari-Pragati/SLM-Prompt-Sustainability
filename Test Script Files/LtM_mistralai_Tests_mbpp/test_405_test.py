import unittest
from mbpp_405_code import check_tuplex

class TestCheckTuplex(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(check_tuplex([(1, 2), (3, 4)], (1, 2)))
        self.assertFalse(check_tuplex([(1, 2), (3, 4)], (3, 4)))

    def test_edge_cases(self):
        self.assertTrue(check_tuplex([], (1, 2)))
        self.assertFalse(check_tuplex([(1, 2)], (1, 2)))
        self.assertFalse(check_tuplex([(1, 2)], (3, 2)))
        self.assertTrue(check_tuplex([(1, 2), (1, 2)], (1, 2)))

    def test_complex(self):
        self.assertTrue(check_tuplex([(1, 2), (3, 4), (1, 2)], (1, 2)))
        self.assertFalse(check_tuplex([(1, 2), (3, 4), (1, 2)], (3, 4)))
        self.assertTrue(check_tuplex([], (1, 2)))
        self.assertFalse(check_tuplex([(1, 2)], (1, 2)))
        self.assertFalse(check_tuplex([(1, 2)], (3, 2)))
        self.assertTrue(check_tuplex([(1, 2), (1, 2)], (1, 2)))
        self.assertFalse(check_tuplex([(1, 2), (3, 4)], (1, 3)))

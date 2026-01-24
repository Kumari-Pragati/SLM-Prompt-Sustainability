import unittest
from mbpp_405_code import check_tuplex

class TestCheckTuplex(unittest.TestCase):
    def test_normal_input(self):
        self.assertTrue(check_tuplex([(1, 2), (3, 4), (5, 6)], (3, 4)))
        self.assertTrue(check_tuplex({(1, 2), (3, 4), (5, 6)}, (3, 4)))

    def test_edge_input(self):
        self.assertFalse(check_tuplex([(1, 2), (3, 4), (5, 6)], (1, 2)))
        self.assertFalse(check_tuplex([(1, 2), (3, 4), (5, 6)], (7, 8)))
        self.assertFalse(check_tuplex({(1, 2), (3, 4), (5, 6)}, (7, 8)))
        self.assertFalse(check_tuplex({(1, 2), (3, 4), (5, 6)}, (1, 2.0)))

    def test_empty_input(self):
        self.assertFalse(check_tuplex([], (1, 2)))
        self.assertFalse(check_tuplex({}, (1, 2)))

    def test_invalid_input(self):
        self.assertRaises(TypeError, check_tuplex, [1, 2], (3, 4))
        self.assertRaises(TypeError, check_tuplex, "str", (3, 4))

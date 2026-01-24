import unittest
from mbpp_405_code import check_tuplex

class TestCheckTuplex(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_tuplex([(1, 2), (3, 4), (1, 2)], (1, 2)))
        self.assertFalse(check_tuplex([(1, 2), (3, 4), (1, 2)], (3, 4)))

    def test_empty_tuple(self):
        self.assertFalse(check_tuplex([], (1, 2)))

    def test_single_tuple(self):
        self.assertFalse(check_tuplex([(1, 2)], (3, 4)))

    def test_single_element_tuple(self):
        self.assertFalse(check_tuplex([(1,)], (3, 4)))
        self.assertTrue(check_tuplex([(1,)], (1,)))

    def test_multiple_occurrences(self):
        self.assertTrue(check_tuplex([(1, 2), (1, 2), (1, 2)], (1, 2)))

    def test_tuple_with_multiple_elements(self):
        self.assertFalse(check_tuplex([(1, 2), (3, 4)], (1, 3)))

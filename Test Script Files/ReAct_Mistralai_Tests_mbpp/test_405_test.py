import unittest
from mbpp_405_code import check_tuplex

class TestCheckTuplex(unittest.TestCase):

    def test_empty_tuple1(self):
        self.assertFalse(check_tuplex([(1, 2), (3, 4)], ()))

    def test_single_element_tuple1(self):
        self.assertFalse(check_tuplex([(1, 2), (3, 4)], (1,)))
        self.assertTrue(check_tuplex([(1, 2), (3, 4)], (1, 2)))

    def test_multiple_elements_tuple1(self):
        self.assertFalse(check_tuplex([(1, 2), (3, 4)], (1,)))
        self.assertTrue(check_tuplex([(1, 2), (3, 4)], (1, 2)))
        self.assertTrue(check_tuplex([(1, 2), (3, 4)], (3, 4)))

    def test_tuple1_in_tuplex(self):
        self.assertTrue(check_tuplex([(1, 2), (3, 4)], ((1, 2),)))

    def test_tuple1_not_in_tuplex(self):
        self.assertFalse(check_tuplex([(1, 2), (3, 4)], ((5, 6),)))

    def test_empty_tuplex(self):
        self.assertFalse(check_tuplex([], (1, 2)))

    def test_tuplex_with_none(self):
        self.assertFalse(check_tuplex([None], (1, 2)))
        self.assertTrue(check_tuplex([None], (None,)))

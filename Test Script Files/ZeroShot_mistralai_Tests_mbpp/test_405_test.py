import unittest
from mbpp_405_code import check_tuplex

class TestCheckTuplex(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(check_tuplex([], (1, 2, 3)))

    def test_single_element_list(self):
        self.assertFalse(check_tuplex([1], (1, 2, 3)))

    def test_matching_tuple(self):
        self.assertTrue(check_tuplex([(1, 2), (3, 4)], (1, 2)))

    def test_non_matching_tuple(self):
        self.assertFalse(check_tuplex([(1, 2), (3, 4)], (1, 3)))

    def test_matching_tuple_in_list(self):
        self.assertTrue(check_tuplex([(1, 2), (1, 2)], (1, 2)))

    def test_multiple_matching_tuples(self):
        self.assertTrue(check_tuplex([(1, 2), (1, 2), (3, 4)], (1, 2)))

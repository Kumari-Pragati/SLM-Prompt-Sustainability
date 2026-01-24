import unittest
from mbpp_405_code import check_tuplex

class TestCheckTuplex(unittest.TestCase):
    def test_true(self):
        self.assertTrue(check_tuplex([1,2,3], [1,2,3]))

    def test_false(self):
        self.assertFalse(check_tuplex([1,2,3], [4,5,6]))

    def test_empty_tuplex(self):
        self.assertFalse(check_tuplex([], [1,2,3]))

    def test_empty_tuple1(self):
        self.assertFalse(check_tuplex([1,2,3], []))

    def test_single_element_tuplex(self):
        self.assertTrue(check_tuplex([1], [1]))

    def test_single_element_tuple1(self):
        self.assertFalse(check_tuplex([1,2,3], [1]))

    def test_tuplex_with_duplicates(self):
        self.assertTrue(check_tuplex([1,2,2,3], [1,2,3]))

    def test_tuple1_with_duplicates(self):
        self.assertTrue(check_tuplex([1,2,2,3], [1,2,2]))

    def test_tuplex_with_duplicates_and_tuple1_with_duplicates(self):
        self.assertTrue(check_tuplex([1,2,2,3,4,4,5], [1,2,2,3,4,4]))

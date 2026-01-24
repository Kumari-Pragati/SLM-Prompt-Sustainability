import unittest
from mbpp_394_code import check_distinct

class TestCheckDistinct(unittest.TestCase):

    def test_distinct_elements(self):
        self.assertTrue(check_distinct(('a', 'b', 'c')))
        self.assertTrue(check_distinct((1, 2, 3)))
        self.assertTrue(check_distinct((True, False)))
        self.assertTrue(check_distinct((1.2, 3.4, 5.6)))

    def test_non_distinct_elements(self):
        self.assertFalse(check_distinct(('a', 'b', 'a')))
        self.assertFalse(check_distinct((1, 2, 1)))
        self.assertFalse(check_distinct((True, False, True)))
        self.assertFalse(check_distinct((1.2, 3.4, 1.2)))

    def test_empty_tuple(self):
        self.assertTrue(check_distinct(()))

    def test_single_element_tuple(self):
        self.assertTrue(check_distinct(('a',)))
        self.assertTrue(check_distinct((1,)))
        self.assertTrue(check_distinct((True,)))
        self.assertTrue(check_distinct((1.2,)))

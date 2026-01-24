import unittest
from mbpp_115_code import empty_dit

class TestEmptyDit(unittest.TestCase):

    def test_simple_true(self):
        self.assertTrue(empty_dit([False]))

    def test_simple_false(self):
        self.assertFalse(empty_dit([True]))

    def test_mixed(self):
        self.assertFalse(empty_dit([True, False]))
        self.assertTrue(empty_dit([False, False]))

    def test_empty_list(self):
        self.assertTrue(empty_dit([]))

    def test_single_element(self):
        self.assertFalse(empty_dit([1]))

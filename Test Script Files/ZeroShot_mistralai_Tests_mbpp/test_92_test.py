import unittest
from mbpp_92_code import is_undulating

class TestIsUndulating(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(is_undulating([]))

    def test_single_element_list(self):
        self.assertFalse(is_undulating([1]))

    def test_two_elements_list(self):
        self.assertFalse(is_undulating([1, 1]))

    def test_undulating_list(self):
        self.assertTrue(is_undulating([1, 2, 1, 3, 2, 1]))

    def test_non_undulating_list(self):
        self.assertFalse(is_undulating([1, 2, 2, 1]))

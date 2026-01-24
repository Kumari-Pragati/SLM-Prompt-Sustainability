import unittest
from mbpp_775_code import odd_position

class TestOddPosition(unittest.TestCase):

    def test_odd_position_true(self):
        self.assertTrue(odd_position([1, 3, 5, 7, 9]))

    def test_odd_position_false(self):
        self.assertFalse(odd_position([1, 2, 3, 4, 5]))

    def test_odd_position_empty(self):
        self.assertTrue(odd_position([]))

    def test_odd_position_single_element(self):
        self.assertTrue(odd_position([1]))

    def test_odd_position_even_elements(self):
        self.assertFalse(odd_position([1, 2, 3, 4]))

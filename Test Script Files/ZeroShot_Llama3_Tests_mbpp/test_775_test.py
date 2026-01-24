import unittest
from mbpp_775_code import odd_position

class TestOddPosition(unittest.TestCase):

    def test_odd_position(self):
        self.assertTrue(odd_position([1, 2, 3, 4, 5]))
        self.assertFalse(odd_position([1, 2, 3, 4, 6]))
        self.assertTrue(odd_position([1, 3, 5, 7, 9]))
        self.assertFalse(odd_position([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertTrue(odd_position([1, 3, 5, 7, 9, 11, 13, 15]))
        self.assertFalse(odd_position([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

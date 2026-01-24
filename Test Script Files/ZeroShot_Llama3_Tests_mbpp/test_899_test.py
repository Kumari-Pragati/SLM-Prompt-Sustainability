import unittest
from mbpp_899_code import check

class TestCheckFunction(unittest.TestCase):

    def test_check_function(self):
        self.assertTrue(check([1, 2, 3, 4, 5], 5))
        self.assertFalse(check([1, 2, 3, 4, 3], 5))
        self.assertTrue(check([1, 2, 3, 2, 1], 5))
        self.assertFalse(check([1, 2, 3, 4, 5, 4], 6))
        self.assertTrue(check([1, 2, 3, 4, 5, 6], 6))
        self.assertFalse(check([1, 2, 3, 4, 5, 3], 6))
        self.assertTrue(check([1, 2, 3, 4, 5, 6, 7], 7))
        self.assertFalse(check([1, 2, 3, 4, 5, 6, 5], 7))
        self.assertTrue(check([1, 2, 3, 4, 5, 6, 7, 8], 8))
        self.assertFalse(check([1, 2, 3, 4, 5, 6, 7, 6], 8))

import unittest
from mbpp_809_code import check_smaller

class TestCheckSmaller(unittest.TestCase):

    def test_check_smaller(self):
        self.assertTrue(check_smaller((1, 2, 3), (0, 1, 2)))
        self.assertFalse(check_smaller((1, 2, 3), (3, 2, 1)))
        self.assertTrue(check_smaller((1, 2, 3), (1, 2, 3)))
        self.assertFalse(check_smaller((1, 2, 3), (1, 2, 3)))
        self.assertFalse(check_smaller((1, 2, 3), (1, 2, 0)))
        self.assertFalse(check_smaller((1, 2, 3), (1, 0, 2)))
        self.assertFalse(check_smaller((1, 2, 3), (0, 1, 2)))

    def test_check_smaller_empty(self):
        self.assertTrue(check_smaller((), ()))
        self.assertFalse(check_smaller((), (1,)))
        self.assertFalse(check_smaller((1,), ()))

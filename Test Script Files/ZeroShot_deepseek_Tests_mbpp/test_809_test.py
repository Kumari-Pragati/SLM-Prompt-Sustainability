import unittest
from mbpp_809_code import check_smaller

class TestCheckSmaller(unittest.TestCase):

    def test_check_smaller(self):
        self.assertTrue(check_smaller((1, 2, 3), (2, 3, 4)))
        self.assertFalse(check_smaller((3, 2, 1), (2, 3, 4)))
        self.assertFalse(check_smaller((2, 3, 4), (1, 2, 3)))
        self.assertTrue(check_smaller((1, 2, 3, 4), (1, 2, 3, 4)))
        self.assertFalse(check_smaller((5, 5, 5), (4, 4, 4)))

import unittest
from mbpp_695_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_check_greater_positive(self):
        self.assertFalse(check_greater((1, 2, 3), (2, 3, 4)))
        self.assertFalse(check_greater((5, 5, 5), (6, 6, 6)))
        self.assertTrue(check_greater((-1, -2, -3), (-2, -3, -4)))

    def test_check_greater_negative(self):
        self.assertTrue(check_greater((1, 2, 3), (1, 2, 4)))
        self.assertTrue(check_greater((5, 5, 5), (5, 6, 6)))
        self.assertFalse(check_greater((-1, -2, -3), (-1, -2, -4)))

    def test_check_greater_mixed(self):
        self.assertTrue(check_greater((1, -2, 3), (-1, -2, 4)))
        self.assertFalse(check_greater((1, -2, 3), (-1, 2, 4)))
        self.assertTrue(check_greater((1, 2, -3), (1, 2, -4)))
        self.assertFalse(check_greater((1, 2, -3), (1, 2, -2)))

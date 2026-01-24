import unittest
from mbpp_695_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_check_greater(self):
        self.assertTrue(check_greater((1, 2), (1, 2)))
        self.assertFalse(check_greater((1, 2), (2, 1)))
        self.assertTrue(check_greater((1, 2, 3), (1, 2, 3)))
        self.assertFalse(check_greater((1, 2, 3), (3, 2, 1)))
        self.assertTrue(check_greater((1, 2, 3, 4), (1, 2, 3, 4)))
        self.assertFalse(check_greater((1, 2, 3, 4), (4, 3, 2, 1)))
        self.assertTrue(check_greater((1, 2, 3, 4, 5), (1, 2, 3, 4, 5)))
        self.assertFalse(check_greater((1, 2, 3, 4, 5), (5, 4, 3, 2, 1)))
        self.assertTrue(check_greater((1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 5, 6)))
        self.assertFalse(check_greater((1, 2, 3, 4, 5, 6), (6, 5, 4, 3, 2, 1)))

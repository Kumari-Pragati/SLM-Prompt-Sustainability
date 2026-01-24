import unittest
from mbpp_809_code import check_smaller

class TestCheckSmaller(unittest.TestCase):

    def test_check_smaller_same_elements(self):
        self.assertFalse(check_smaller((1, 2, 3), (1, 2, 3)))

    def test_check_smaller_equal_tuples(self):
        self.assertTrue(check_smaller((0, 0, 0), (0, 0, 0)))

    def test_check_smaller_different_lengths(self):
        self.assertFalse(check_smaller((1, 2, 3), (1, 2)))

    def test_check_smaller_reverse_order(self):
        self.assertTrue(check_smaller((1, 2), (1, 2, 3)))

    def test_check_smaller_different_elements(self):
        self.assertTrue(check_smaller((1, 2, 3), (0, 0, 0)))

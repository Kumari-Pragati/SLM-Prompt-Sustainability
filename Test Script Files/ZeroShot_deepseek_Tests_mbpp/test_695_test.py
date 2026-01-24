import unittest
from mbpp_695_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_check_greater_true(self):
        self.assertTrue(check_greater((1, 2, 3), (4, 5, 6)))

    def test_check_greater_false(self):
        self.assertFalse(check_greater((4, 5, 6), (1, 2, 3)))

    def test_check_greater_equal(self):
        self.assertFalse(check_greater((4, 5, 6), (4, 5, 6)))

    def test_check_greater_empty(self):
        self.assertTrue(check_greater((), ()))

    def test_check_greater_diff_length(self):
        self.assertFalse(check_greater((1, 2, 3, 4), (1, 2, 3)))

import unittest
from mbpp_809_code import check_smaller

class TestCheckSmaller(unittest.TestCase):

    def test_smaller_tuples(self):
        self.assertTrue(check_smaller((1, 2, 3), (0, 1, 2)))
        self.assertFalse(check_smaller((1, 2, 3), (2, 1, 3)))
        self.assertFalse(check_smaller((1, 2, 3), (1, 2, 0)))
        self.assertTrue(check_smaller((1, 2, 3), (1, 2, 3)))

    def test_smaller_lists(self):
        self.assertTrue(check_smaller([1, 2, 3], [0, 1, 2]))
        self.assertFalse(check_smaller([1, 2, 3], [2, 1, 3]))
        self.assertFalse(check_smaller([1, 2, 3], [1, 2, 0]))
        self.assertTrue(check_smaller([1, 2, 3], [1, 2, 3]))

    def test_empty_tuples(self):
        self.assertTrue(check_smaller((), ()))
        self.assertFalse(check_smaller((), (1,)))
        self.assertFalse(check_smaller((1,), ()))

    def test_empty_lists(self):
        self.assertTrue(check_smaller([], []))
        self.assertFalse(check_smaller([], [1]))
        self.assertFalse(check_smaller([1], []))

    def test_single_element_tuples(self):
        self.assertTrue(check_smaller((1,), (0,)))
        self.assertFalse(check_smaller((1,), (1,)))
        self.assertFalse(check_smaller((1,), ()))

    def test_single_element_lists(self):
        self.assertTrue(check_smaller([1], [0]))
        self.assertFalse(check_smaller([1], [1]))
        self.assertFalse(check_smaller([1], []))

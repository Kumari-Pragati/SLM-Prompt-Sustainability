import unittest
from mbpp_809_code import check_smaller

class TestCheckSmaller(unittest.TestCase):
    def test_simple_valid(self):
        self.assertTrue(check_smaller((1, 2, 3), (0, 1, 2)))

    def test_empty_inputs(self):
        with self.assertRaises(TypeError):
            check_smaller([], [])

    def test_single_element(self):
        self.assertFalse(check_smaller((1,), (2,)))

    def test_reverse_order(self):
        self.assertFalse(check_smaller((2, 1, 3), (1, 2, 3)))

    def test_all_equal(self):
        self.assertFalse(check_smaller((1, 1, 1), (1, 1, 1)))

    def test_all_greater(self):
        self.assertTrue(check_smaller((1, 2, 3), (0, 1, 2)))

    def test_all_smaller(self):
        self.assertFalse(check_smaller((0, 0, 0), (1, 2, 3)))

    def test_mixed_order(self):
        self.assertFalse(check_smaller((1, 2, 3), (3, 2, 1)))

    def test_mixed_order_reverse(self):
        self.assertFalse(check_smaller((3, 2, 1), (1, 2, 3)))

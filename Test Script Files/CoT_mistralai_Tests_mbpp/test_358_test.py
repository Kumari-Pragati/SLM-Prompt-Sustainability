import unittest
from mbpp_358_code import moddiv_list

class TestModdivList(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(moddiv_list([], []), [])
        self.assertListEqual(moddiv_list([], [1]), [0])
        self.assertListEqual(moddiv_list([1], []), [1])

    def test_single_element_lists(self):
        self.assertListEqual(moddiv_list([1], [2]), [1])
        self.assertListEqual(moddiv_list([2], [1]), [0])

    def test_equal_length_lists(self):
        self.assertListEqual(moddiv_list([1, 2, 3], [4, 2, 3]), [1, 0, 0])
        self.assertListEqual(moddiv_list([4, 2, 3], [1, 2, 3]), [0, 0, 1])

    def test_different_length_lists(self):
        self.assertListEqual(moddiv_list([1, 2, 3], [4, 2]), [1, 2])
        self.assertListEqual(moddiv_list([4, 2], [1, 2, 3]), [0, 2])

    def test_negative_numbers(self):
        self.assertListEqual(moddiv_list([-1, 2, -3], [4, 2]), [-1, 2, -3])
        self.assertListEqual(moddiv_list([4, 2, -3], [-1, 2]), [0, 2, -3])

    def test_zero_division(self):
        self.assertRaises(ZeroDivisionError, lambda: moddiv_list([0], [1]))

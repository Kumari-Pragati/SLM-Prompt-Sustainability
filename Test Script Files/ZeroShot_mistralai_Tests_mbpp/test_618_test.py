import unittest
from mbpp_618_code import div_list

class TestDivList(unittest.TestCase):

    def test_div_list_positive(self):
        self.assertListEqual(div_list([1, 2, 3], [2, 4, 6]), [0.5, 0.5, 0.5])
        self.assertListEqual(div_list([4, 8, 16], [2, 4, 8]), [2.0, 2.0, 2.0])
        self.assertListEqual(div_list([1, 2, 3], [5, 10, 15]), [0.2, 0.2, 0.2])

    def test_div_list_zero(self):
        self.assertRaises(ZeroDivisionError, lambda: div_list([1, 0, 3], [2, 4, 0]))
        self.assertRaises(ZeroDivisionError, lambda: div_list([0, 2, 0], [1, 4, 0]))
        self.assertRaises(ZeroDivisionError, lambda: div_list([0, 0, 3], [2, 0, 4]))

    def test_div_list_lengths(self):
        self.assertRaises(ValueError, lambda: div_list([1, 2, 3], [2, 4]))
        self.assertRaises(ValueError, lambda: div_list([1, 2, 3], [2, 4, 6, 8]))
        self.assertRaises(ValueError, lambda: div_list([1, 2], [2, 4, 6]))

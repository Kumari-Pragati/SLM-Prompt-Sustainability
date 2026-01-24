import unittest
from mbpp_358_code import moddiv_list

class TestModdivList(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(moddiv_list([1, 2, 3, 4], [2, 3]), [1, 2, 0, 1])

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            moddiv_list([1, 0], [2, 3])

    def test_empty_lists(self):
        self.assertListEqual(moddiv_list([], [2, 3]), [])
        self.assertListEqual(moddiv_list([1, 2, 3], []), [])

    def test_negative_numbers(self):
        self.assertEqual(moddiv_list([-1, -2, -3], [-2, -3]), [1, 0, 1])

import unittest
from mbpp_358_code import moddiv_list

class TestModdivList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(moddiv_list([10, 20, 30], [2, 3, 4]), [1, 2, 0])

    def test_zero_divisor(self):
        with self.assertRaises(ZeroDivisionError):
            moddiv_list([10, 20, 30], [0, 3, 4])

    def test_negative_numbers(self):
        self.assertEqual(moddiv_list([-10, 20, 30], [2, 3, 4]), [-1, 2, 0])

    def test_single_element_lists(self):
        self.assertEqual(moddiv_list([10], [2]), [0])
        self.assertEqual(moddiv_list([10], [0]), [0])

    def test_empty_lists(self):
        self.assertEqual(moddiv_list([], []), [])

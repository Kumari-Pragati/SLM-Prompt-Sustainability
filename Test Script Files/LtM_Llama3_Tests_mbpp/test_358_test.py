import unittest
from mbpp_358_code import moddiv_list

class TestModdivList(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(moddiv_list([10, 20, 30], [2, 3, 4]), [1, 2, 0])

    def test_empty_inputs(self):
        self.assertEqual(moddiv_list([], []), [])

    def test_single_input(self):
        self.assertEqual(moddiv_list([10], [2]), [0])

    def test_zero_divisor(self):
        with self.assertRaises(ZeroDivisionError):
            moddiv_list([10], [0])

    def test_negative_numbers(self):
        self.assertEqual(moddiv_list([-10, 20, 30], [2, 3, 4]), [0, 2, 0])

    def test_large_numbers(self):
        self.assertEqual(moddiv_list([1000000, 2000000, 3000000], [200000, 300000, 400000]), [1, 0, 0])

    def test_mixed_signs(self):
        self.assertEqual(moddiv_list([-10, 20, 30], [-2, 3, 4]), [0, 2, 0])

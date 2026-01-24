import unittest
from mbpp_618_code import div_list

class TestDivList(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(div_list([10, 20, 30], [1, 2, 3]), [10, 10, 10])

    def test_single_number(self):
        self.assertAlmostEqual(div_list([10], [1]), [10])

    def test_empty_lists(self):
        self.assertEqual(div_list([], []), [])

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([10, 20], [0, 5])

    def test_different_lengths(self):
        self.assertAlmostEqual(div_list([10, 20, 30, 40], [1, 2]), [10, 10])

    def test_negative_numbers(self):
        self.assertAlmostEqual(div_list([-10, -20, -30], [1, 2, 3]), [-10, -10, -10])

    def test_decimal_numbers(self):
        self.assertAlmostEqual(div_list([10.5, 20.5], [1, 2]), [10.5, 10.25])

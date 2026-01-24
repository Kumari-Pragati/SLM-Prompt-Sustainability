import unittest
from mbpp_618_code import div_list

class TestDivList(unittest.TestCase):
    def test_simple_division(self):
        self.assertEqual(div_list([1, 2, 3], [1, 2, 3]), [1.0, 1.0, 1.0])

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([1, 2, 3], [0, 0, 0])

    def test_division_by_nonzero(self):
        self.assertEqual(div_list([1, 2, 3], [2, 3, 4]), [0.5, 0.6666666666666666, 0.75])

    def test_division_by_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([1, 2, 3], [])

    def test_division_by_empty_list2(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([], [])

    def test_division_by_single_element(self):
        self.assertEqual(div_list([1], [1]), [1.0])

    def test_division_by_single_element2(self):
        self.assertEqual(div_list([1], [2]), [0.5])

    def test_division_by_single_element3(self):
        self.assertEqual(div_list([1], [0]), [float('inf')])

    def test_division_by_single_element4(self):
        self.assertEqual(div_list([1], [3]), [0.3333333333333333])

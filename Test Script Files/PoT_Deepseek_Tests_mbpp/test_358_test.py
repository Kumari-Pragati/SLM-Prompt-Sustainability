import unittest
from mbpp_358_code import moddiv_list

class TestModdivList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(moddiv_list([10, 20, 30], [3, 5, 7]), [1, 4, 4])

    def test_edge_case_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            moddiv_list([10, 20, 30], [0, 5, 7])

    def test_boundary_case_large_numbers(self):
        self.assertEqual(moddiv_list(
            [10**10, 20**10, 30**10], [10**9, 20**9, 30**9]),
            [10, 20, 30])

    def test_corner_case_negative_numbers(self):
        self.assertEqual(moddiv_list([-10, -20, -30], [3, 5, 7]), [-1, -4, -4])

    def test_corner_case_large_denominators(self):
        self.assertEqual(moddiv_list([10, 20, 30], [10**9, 20**9, 30**9]), [0, 0, 0])

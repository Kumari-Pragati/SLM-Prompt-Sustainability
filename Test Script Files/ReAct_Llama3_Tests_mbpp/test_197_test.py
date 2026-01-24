import unittest
from mbpp_197_code import find_exponentio

class TestFindExponentio(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_exponentio((1, 2, 3), (4, 5, 6)), (1**4, 2**5, 3**6))

    def test_edge_case_power_of_0(self):
        self.assertEqual(find_exponentio((1, 2, 3), (0, 0, 0)), (1, 1, 1))

    def test_edge_case_power_of_negative(self):
        self.assertEqual(find_exponentio((1, 2, 3), (-1, -2, -3)), (1/1, 2/2, 3/3))

    def test_edge_case_power_of_1(self):
        self.assertEqual(find_exponentio((1, 2, 3), (1, 1, 1)), (1, 1, 1))

    def test_edge_case_power_of_large(self):
        self.assertEqual(find_exponentio((1, 2, 3), (100, 200, 300)), (1**100, 2**200, 3**300))

    def test_edge_case_power_of_zero_and_negative(self):
        self.assertEqual(find_exponentio((1, 2, 3), (0, -1, -2)), (1, 1/2, 1/3))

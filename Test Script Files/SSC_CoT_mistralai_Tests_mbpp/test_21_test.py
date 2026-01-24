import unittest
from mbpp_21_code import multiples_of_num

class TestMultiplesOfNum(unittest.TestCase):

    def test_typical_input(self):
        self.assertListEqual(multiples_of_num(10, 3), [3, 6, 9])
        self.assertListEqual(multiples_of_num(20, 5), [10, 15, 20])

    def test_edge_cases(self):
        self.assertListEqual(multiples_of_num(0, 2), [])
        self.assertListEqual(multiples_of_num(1, 1), [1])
        self.assertListEqual(multiples_of_num(2, 2), [2])
        self.assertListEqual(multiples_of_num(100, 1), [1])

    def test_boundary_conditions(self):
        self.assertListEqual(multiples_of_num(1, 2), [2])
        self.assertListEqual(multiples_of_num(2, 1), [2])
        self.assertListEqual(multiples_of_num(0, 0), [])

    def test_negative_input(self):
        self.assertRaises(ValueError, multiples_of_num, -1, 2)
        self.assertRaises(ValueError, multiples_of_num, 2, -1)

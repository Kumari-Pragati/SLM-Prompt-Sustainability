import unittest
from mbpp_21_code import multiples_of_num

class TestMultiplesOfNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiples_of_num(4, 3), [3, 6, 9])
        self.assertEqual(multiples_of_num(10, 5), [5, 10, 15, 20, 25])

    def test_edge_case_small_n(self):
        self.assertEqual(multiples_of_num(3, 2), [2])
        self.assertEqual(multiples_of_num(1, 1), [1])

    def test_edge_case_small_m(self):
        self.assertEqual(multiples_of_num(2, 3), [3])
        self.assertEqual(multiples_of_num(1, 4), [4])

    def test_edge_case_m_equals_n(self):
        self.assertEqual(multiples_of_num(5, 5), [5])

    def test_corner_case_zero(self):
        self.assertEqual(multiples_of_num(3, 0), [])

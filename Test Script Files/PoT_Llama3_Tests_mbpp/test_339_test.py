import unittest
from mbpp_339_code import find_Divisor

class TestFindDivisor(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Divisor(2, 2), 2)

    def test_edge_case_equal(self):
        self.assertEqual(find_Divisor(2, 2), 2)

    def test_edge_case_non_equal(self):
        self.assertEqual(find_Divisor(2, 3), 2)

    def test_edge_case_zero(self):
        with self.assertRaises(TypeError):
            find_Divisor(0, 2)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            find_Divisor(-1, 2)

    def test_edge_case_non_integer(self):
        with self.assertRaises(TypeError):
            find_Divisor(2.5, 2)

import unittest
from mbpp_339_code import find_Divisor

class TestFindDivisor(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Divisor(10, 5), 5)

    def test_edge_case(self):
        self.assertEqual(find_Divisor(1, 1), 1)

    def test_boundary_case(self):
        self.assertEqual(find_Divisor(0, 0), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Divisor("10", 5)

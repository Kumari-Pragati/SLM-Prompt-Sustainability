import unittest
from mbpp_199_code import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(highest_Power_of_2(16), 16)

    def test_edge_case_power_of_2(self):
        self.assertEqual(highest_Power_of_2(15), 8)

    def test_edge_case_power_of_1(self):
        self.assertEqual(highest_Power_of_2(1), 1)

    def test_edge_case_power_of_0(self):
        self.assertEqual(highest_Power_of_2(0), 0)

    def test_edge_case_negative(self):
        self.assertEqual(highest_Power_of_2(-1), 0)

    def test_edge_case_non_integer(self):
        with self.assertRaises(TypeError):
            highest_Power_of_2("a")

    def test_edge_case_non_positive(self):
        self.assertEqual(highest_Power_of_2(-8), 0)

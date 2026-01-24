import unittest
from mbpp_388_code import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(highest_Power_of_2(10), 8)

    def test_boundary_conditions(self):
        self.assertEqual(highest_Power_of_2(1), 1)
        self.assertEqual(highest_Power_of_2(2), 2)
        self.assertEqual(highest_Power_of_2(3), 2)
        self.assertEqual(highest_Power_of_2(4), 4)

    def test_edge_conditions(self):
        self.assertEqual(highest_Power_of_2(0), 0)
        self.assertEqual(highest_Power_of_2(1024), 1024)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            highest_Power_of_2("10")
        with self.assertRaises(ValueError):
            highest_Power_of_2(-10)

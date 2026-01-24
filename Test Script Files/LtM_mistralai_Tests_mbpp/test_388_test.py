import unittest
from mbpp_388_code import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(highest_Power_of_2(1), 1)
        self.assertEqual(highest_Power_of_2(2), 2)
        self.assertEqual(highest_Power_of_2(4), 4)
        self.assertEqual(highest_Power_of_2(8), 8)
        self.assertEqual(highest_Power_of_2(16), 16)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(highest_Power_of_2(0), 0)
        self.assertEqual(highest_Power_of_2(3), 2)
        self.assertEqual(highest_Power_of_2(5), 2)
        self.assertEqual(highest_Power_of_2(6), 6)
        self.assertEqual(highest_Power_of_2(7), 4)

    def test_complex_inputs(self):
        self.assertEqual(highest_Power_of_2(255), 255)
        self.assertEqual(highest_Power_of_2(256), 256)
        self.assertEqual(highest_Power_of_2(257), 256)
        self.assertEqual(highest_Power_of_2(258), 256)
        self.assertEqual(highest_Power_of_2(259), 256)
        self.assertEqual(highest_Power_of_2(260), 128)

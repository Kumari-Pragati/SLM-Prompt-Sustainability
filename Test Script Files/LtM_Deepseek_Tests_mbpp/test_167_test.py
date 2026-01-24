import unittest
from mbpp_167_code import next_Power_Of_2

class TestNextPowerOf2(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(next_Power_Of_2(8), 8)
        self.assertEqual(next_Power_Of_2(16), 16)
        self.assertEqual(next_Power_Of_2(32), 32)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(next_Power_Of_2(1), 2)
        self.assertEqual(next_Power_Of_2(0), 1)
        self.assertEqual(next_Power_Of_2(2), 4)
        self.assertEqual(next_Power_Of_2(3), 4)
        self.assertEqual(next_Power_Of_2(4), 4)
        self.assertEqual(next_Power_Of_2(5), 8)
        self.assertEqual(next_Power_Of_2(6), 8)
        self.assertEqual(next_Power_Of_2(7), 8)
        self.assertEqual(next_Power_Of_2(8), 8)

    # Test for more complex or corner cases
    def test_corner_cases(self):
        self.assertEqual(next_Power_Of_2(1023), 1024)
        self.assertEqual(next_Power_Of_2(1024), 1024)
        self.assertEqual(next_Power_Of_2(1025), 2048)
        self.assertEqual(next_Power_Of_2(2048), 2048)
        self.assertEqual(next_Power_Of_2(2049), 4096)

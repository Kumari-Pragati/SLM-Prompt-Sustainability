import unittest
from mbpp_107_code import count_Hexadecimal

class TestCountHexadecimal(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(count_Hexadecimal(10, 15), 2)
        self.assertEqual(count_Hexadecimal(16, 20), 1)
        self.assertEqual(count_Hexadecimal(100, 110), 1)

    # Test for edge and boundary conditions
    def test_boundary_conditions(self):
        self.assertEqual(count_Hexadecimal(0, 10), 1)
        self.assertEqual(count_Hexadecimal(15, 15), 1)
        self.assertEqual(count_Hexadecimal(16, 31), 2)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(count_Hexadecimal(1000, 1010), 0)
        self.assertEqual(count_Hexadecimal(32, 63), 2)
        self.assertEqual(count_Hexadecimal(1024, 1030), 1)

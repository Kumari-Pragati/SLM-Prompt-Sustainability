import unittest
from mbpp_406_code import find_Parity

class TestFindParity(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(find_Parity(1), "Odd Parity")
        self.assertEqual(find_Parity(2), "Even Parity")
        self.assertEqual(find_Parity(3), "Odd Parity")
        self.assertEqual(find_Parity(4), "Even Parity")

    # Test for edge and boundary conditions
    def test_boundary_conditions(self):
        self.assertEqual(find_Parity(0), "Even Parity")
        self.assertEqual(find_Parity(2**32 - 1), "Odd Parity")
        self.assertEqual(find_Parity(2**32), "Even Parity")

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(find_Parity(2**64 - 1), "Odd Parity")
        self.assertEqual(find_Parity(2**64), "Even Parity")

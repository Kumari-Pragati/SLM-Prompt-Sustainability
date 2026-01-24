import unittest
from mbpp_407_code import rearrange_bigger

class TestRearrangeBigger(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(rearrange_bigger(12345), 52341)
        self.assertEqual(rearrange_bigger(98765), 98765)
        self.assertEqual(rearrange_bigger(11223), 32211)

    # Test for edge and boundary conditions
    def test_edge_and_boundary_conditions(self):
        self.assertEqual(rearrange_bigger(10000), 10000)
        self.assertEqual(rearrange_bigger(1234567890), 9876543210)
        self.assertEqual(rearrange_bigger(11111), False)

    # Test for more complex or corner cases
    def test_more_complex_cases(self):
        self.assertEqual(rearrange_bigger(123321), 323121)
        self.assertEqual(rearrange_bigger(12321), False)
        self.assertEqual(rearrange_bigger(9876543210), 9876543210)

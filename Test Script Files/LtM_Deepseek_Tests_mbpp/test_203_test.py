import unittest
from mbpp_203_code import hamming_Distance

class TestHammingDistance(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(hamming_Distance(1, 4), 2)
        self.assertEqual(hamming_Distance(15, 11), 2)

    # Test for edge and boundary conditions
    def test_boundary_conditions(self):
        self.assertEqual(hamming_Distance(0, 0), 0)
        self.assertEqual(hamming_Distance(2147483647, 0), 31)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(hamming_Distance(2147483647, 2147483647), 0)
        self.assertEqual(hamming_Distance(1, 4294967295), 31)

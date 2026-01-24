import unittest
from mbpp_203_code import hamming_Distance

class TestHammingDistance(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(hamming_Distance(1, 1), 0)
        self.assertEqual(hamming_Distance(1, 2), 1)
        self.assertEqual(hamming_Distance(2, 2), 0)
        self.assertEqual(hamming_Distance(3, 3), 0)
        self.assertEqual(hamming_Distance(4, 4), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(hamming_Distance(0, 0), 0)
        self.assertEqual(hamming_Distance(0, 1), 1)
        self.assertEqual(hamming_Distance(1, 0), 1)
        self.assertEqual(hamming_Distance(2**31 - 1, 2**31 - 1), 0)
        self.assertEqual(hamming_Distance(2**31 - 1, 2**31), 31)

    def test_complex_and_corner_cases(self):
        self.assertEqual(hamming_Distance(2**31 - 1, 2**31 - 2), 1)
        self.assertEqual(hamming_Distance(2**31 - 1, 2**31 - 3), 2)
        self.assertEqual(hamming_Distance(2**31 - 1, 2**31 - 4), 3)

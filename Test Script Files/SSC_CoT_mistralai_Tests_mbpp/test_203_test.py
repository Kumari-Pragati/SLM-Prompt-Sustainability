import unittest
from mbpp_203_code import hamming_Distance

class TestHammingDistance(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(hamming_Distance(6, 3), 3)
        self.assertEqual(hamming_Distance(10, 2), 3)
        self.assertEqual(hamming_Distance(15, 7), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(hamming_Distance(0, 1), 1)
        self.assertEqual(hamming_Distance(1, 0), 1)
        self.assertEqual(hamming_Distance(1, 1), 0)
        self.assertEqual(hamming_Distance(2**31 - 1, 2**31), 1)
        self.assertEqual(hamming_Distance(2**31, 2**31 - 1), 1)

    def test_special_cases(self):
        self.assertEqual(hamming_Distance(1, 0), 1)
        self.assertEqual(hamming_Distance(0, 1), 1)
        self.assertEqual(hamming_Distance(1, 2), 2)
        self.assertEqual(hamming_Distance(2, 1), 2)
        self.assertEqual(hamming_Distance(1, 3), 3)
        self.assertEqual(hamming_Distance(3, 1), 3)

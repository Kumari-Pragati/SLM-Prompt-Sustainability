import unittest
from mbpp_203_code import hamming_Distance

class TestHammingDistance(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(hamming_Distance(1, 2), 1)
        self.assertEqual(hamming_Distance(5, 5), 0)
        self.assertEqual(hamming_Distance(10, 15), 3)

    def test_edge_cases(self):
        self.assertEqual(hamming_Distance(0, 0), 0)
        self.assertEqual(hamming_Distance(0, 1), 1)
        self.assertEqual(hamming_Distance(1, 1), 0)

    def test_corner_cases(self):
        self.assertEqual(hamming_Distance(0, 2**31 - 1), 31)
        self.assertEqual(hamming_Distance(2**31 - 1, 0), 31)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            hamming_Distance('a', 2)
        with self.assertRaises(TypeError):
            hamming_Distance(1, 'b')

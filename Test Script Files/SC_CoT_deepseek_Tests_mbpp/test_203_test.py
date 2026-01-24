import unittest

from mbpp_203_code import hamming_Distance

class TestHammingDistance(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(hamming_Distance(1, 4), 2)
        self.assertEqual(hamming_Distance(2147483647, 0), 31)

    def test_edge_cases(self):
        self.assertEqual(hamming_Distance(0, 0), 0)
        self.assertEqual(hamming_Distance(2147483647, 2147483647), 0)

    def test_corner_cases(self):
        self.assertEqual(hamming_Distance(18446744073709551615, 18446744073709551615), 0)
        self.assertEqual(hamming_Distance(18446744073709551615, 0), 64)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            hamming_Distance("1", 1)
        with self.assertRaises(TypeError):
            hamming_Distance(1, "1")
        with self.assertRaises(TypeError):
            hamming_Distance("1", "1")

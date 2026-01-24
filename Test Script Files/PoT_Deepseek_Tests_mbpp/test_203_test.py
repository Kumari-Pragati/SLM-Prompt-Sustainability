import unittest
from mbpp_203_code import hamming_Distance

class TestHammingDistance(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(hamming_Distance(0b1010, 0b1100), 2)
        self.assertEqual(hamming_Distance(0b1111, 0b0000), 4)
        self.assertEqual(hamming_Distance(0b10101010, 0b01010101), 4)

    def test_edge_cases(self):
        self.assertEqual(hamming_Distance(0, 0), 0)
        self.assertEqual(hamming_Distance(0b11111111, 0), 8)
        self.assertEqual(hamming_Distance(0, 0b11111111), 8)

    def test_boundary_cases(self):
        self.assertEqual(hamming_Distance(0b11111111, 0b11111110), 1)
        self.assertEqual(hamming_Distance(0b11111111, 0b11111111), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            hamming_Distance("1010", 0b1100)
        with self.assertRaises(TypeError):
            hamming_Distance(0b1010, "1100")
        with self.assertRaises(TypeError):
            hamming_Distance("1010", "1100")

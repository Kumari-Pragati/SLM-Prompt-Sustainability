import unittest
from mbpp_203_code import hamming_Distance

class TestHammingDistance(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(hamming_Distance(1, 4), 2)
        self.assertEqual(hamming_Distance(15, 10), 3)
        self.assertEqual(hamming_Distance(255, 0), 8)

    def test_edge_cases(self):
        self.assertEqual(hamming_Distance(0, 0), 0)
        self.assertEqual(hamming_Distance(255, 255), 0)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            hamming_Distance("1", 1)
        with self.assertRaises(TypeError):
            hamming_Distance(1, "1")

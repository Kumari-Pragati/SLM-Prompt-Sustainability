import unittest
from mbpp_203_code import hamming_Distance

class TestHammingDistance(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(hamming_Distance(9, 5), 2)

    def test_boundary_conditions(self):
        self.assertEqual(hamming_Distance(0, 0), 0)
        self.assertEqual(hamming_Distance(255, 0), 8)

    def test_edge_conditions(self):
        self.assertEqual(hamming_Distance(255, 255), 0)
        self.assertEqual(hamming_Distance(0, 255), 8)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            hamming_Distance("9", 5)
        with self.assertRaises(TypeError):
            hamming_Distance(9, "5")
        with self.assertRaises(TypeError):
            hamming_Distance("9", "5")

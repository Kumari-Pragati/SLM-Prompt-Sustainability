import unittest
from mbpp_688_code import len_complex

class TestLenComplex(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(len_complex(3, 4), 5.0)

    def test_zero_real_part(self):
        self.assertAlmostEqual(len_complex(0, 4), 4.0)

    def test_zero_imaginary_part(self):
        self.assertAlmostEqual(len_complex(3, 0), 3.0)

    def test_negative_real_and_imaginary_parts(self):
        self.assertAlmostEqual(len_complex(-3, -4), 5.0)

    def test_edge_case_zero(self):
        self.assertEqual(len_complex(0, 0), 0.0)

    def test_large_numbers(self):
        self.assertAlmostEqual(len_complex(1000, 2000), 2236.0682)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            len_complex("3", 4)

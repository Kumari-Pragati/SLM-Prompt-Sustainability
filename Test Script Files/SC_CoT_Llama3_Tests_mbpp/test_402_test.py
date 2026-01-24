import unittest
from mbpp_402_code import ncr_modp

class TestNcrModp(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(ncr_modp(10, 3, 7), 35)

    def test_edge_cases(self):
        self.assertEqual(ncr_modp(5, 0, 7), 1)
        self.assertEqual(ncr_modp(5, 5, 7), 1)
        self.assertEqual(ncr_modp(5, 6, 7), 0)

    def test_boundary_cases(self):
        self.assertEqual(ncr_modp(10, 10, 7), 1)
        self.assertEqual(ncr_modp(10, 9, 7), 1)
        self.assertEqual(ncr_modp(10, 8, 7), 0)

    def test_special_cases(self):
        self.assertEqual(ncr_modp(10, 2, 7), 21)
        self.assertEqual(ncr_modp(10, 4, 7), 35)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            ncr_modp('a', 3, 7)
        with self.assertRaises(TypeError):
            ncr_modp(10, 'b', 7)
        with self.assertRaises(TypeError):
            ncr_modp(10, 3, 'c')

import unittest
from mbpp_402_code import ncr_modp

class TestNcrModp(unittest.TestCase):
    def test_ncr_modp_typical(self):
        self.assertEqual(ncr_modp(10, 3, 7), 21)

    def test_ncr_modp_edge(self):
        self.assertEqual(ncr_modp(5, 0, 11), 1)
        self.assertEqual(ncr_modp(5, 5, 11), 1)

    def test_ncr_modp_boundary(self):
        self.assertEqual(ncr_modp(10, 10, 7), 1)
        self.assertEqual(ncr_modp(10, 1, 7), 10)

    def test_ncr_modp_error(self):
        with self.assertRaises(TypeError):
            ncr_modp('a', 3, 7)

    def test_ncr_modp_invalid_input(self):
        with self.assertRaises(ValueError):
            ncr_modp(-1, 3, 7)

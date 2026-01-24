import unittest
from mbpp_402_code import ncr_modp

class TestNcrModp(unittest.TestCase):
    def test_ncr_modp_typical(self):
        self.assertEqual(ncr_modp(5, 2, 7), 6)
        self.assertEqual(ncr_modp(10, 3, 11), 40)
        self.assertEqual(ncr_modp(15, 4, 13), 330)

    def test_ncr_modp_edge(self):
        self.assertEqual(ncr_modp(1, 1, 2), 1)
        self.assertEqual(ncr_modp(2, 1, 3), 2)
        self.assertEqual(ncr_modp(3, 2, 5), 3)

    def test_ncr_modp_invalid(self):
        with self.assertRaises(TypeError):
            ncr_modp('a', 2, 7)
        with self.assertRaises(TypeError):
            ncr_modp(5, 'b', 7)
        with self.assertRaises(TypeError):
            ncr_modp(5, 2, 'c')

import unittest
from mbpp_952_code import nCr_mod_p

class TestNCRModP(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(nCr_mod_p(5, 2, 13), 10)
        self.assertEqual(nCr_mod_p(10, 5, 101), 10)

    # Test for edge and boundary conditions
    def test_boundary_conditions(self):
        self.assertEqual(nCr_mod_p(0, 0, 101), 1)
        self.assertEqual(nCr_mod_p(1, 0, 101), 1)
        self.assertEqual(nCr_mod_p(1, 1, 101), 1)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(nCr_mod_p(10, 5, 1000), 252)
        self.assertEqual(nCr_mod_p(20, 10, 10000), 184756)

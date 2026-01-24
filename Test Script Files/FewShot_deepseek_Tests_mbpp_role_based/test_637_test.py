import unittest
from mbpp_637_code import noprofit_noloss

class TestNoProfitNoLoss(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(noprofit_noloss(100, 100))

    def test_edge_case(self):
        self.assertTrue(noprofit_noloss(0, 0))

    def test_boundary_case(self):
        self.assertTrue(noprofit_noloss(1, 1))
        self.assertFalse(noprofit_noloss(2, 1))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            noprofit_noloss("100", 100)
        with self.assertRaises(TypeError):
            noprofit_noloss(100, "100")

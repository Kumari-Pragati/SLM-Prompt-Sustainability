import unittest
from mbpp_637_code import noprofit_noloss

class TestNoProfitNoLoss(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(noprofit_noloss(100, 100))

    def test_typical_case_2(self):
        self.assertFalse(noprofit_noloss(200, 100))

    def test_edge_case_0(self):
        self.assertTrue(noprofit_noloss(0, 0))

    def test_edge_case_negative_numbers(self):
        self.assertTrue(noprofit_noloss(-100, -100))
        self.assertFalse(noprofit_noloss(-100, 0))
        self.assertFalse(noprofit_noloss(0, -100))
        self.assertFalse(noprofit_noloss(-100, 100))
        self.assertFalse(noprofit_noloss(100, -100))

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            noprofit_noloss("100", 100)
        with self.assertRaises(TypeError):
            noprofit_noloss(100, "100")
        with self.assertRaises(TypeError):
            noprofit_noloss("100", "100")

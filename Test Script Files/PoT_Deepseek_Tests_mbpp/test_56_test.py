import unittest
from mbpp_56_code import check

class TestCheckFunction(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(check(121))
        self.assertTrue(check(1221))
        self.assertTrue(check(12321))
        self.assertTrue(check(123321))

    def test_edge_cases(self):
        self.assertFalse(check(0))
        self.assertFalse(check(10))
        self.assertFalse(check(100))

    def test_boundary_conditions(self):
        self.assertTrue(check(11))
        self.assertTrue(check(121))
        self.assertTrue(check(12321))
        self.assertTrue(check(1234321))
        self.assertTrue(check(123454321))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check("121")
        with self.assertRaises(TypeError):
            check(121.0)
        with self.assertRaises(TypeError):
            check(None)

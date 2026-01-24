import unittest
from mbpp_56_code import check

class TestCheckFunction(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertTrue(check(1))
        self.assertTrue(check(2))
        self.assertTrue(check(3))

    def test_edge_cases(self):
        self.assertTrue(check(4))
        self.assertTrue(check(5))
        self.assertTrue(check(6))

    def test_special_cases(self):
        self.assertFalse(check(0))
        self.assertFalse(check(-1))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check("a")
        with self.assertRaises(TypeError):
            check(None)

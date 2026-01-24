import unittest
from mbpp_56_code import check

class TestCheckFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check(123))

    def test_edge_case(self):
        self.assertFalse(check(100))

    def test_boundary_case(self):
        self.assertTrue(check(1000))
        self.assertFalse(check(9999))

    def test_special_case(self):
        self.assertTrue(check(1221))
        self.assertFalse(check(12321))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check("123")

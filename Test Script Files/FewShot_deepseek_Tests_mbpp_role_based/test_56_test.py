import unittest
from mbpp_56_code import check

class TestCheckFunction(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check(121))

    def test_edge_case(self):
        self.assertFalse(check(123))

    def test_boundary_case(self):
        self.assertFalse(check(111))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check('121')

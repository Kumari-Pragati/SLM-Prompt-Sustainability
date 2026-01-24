import unittest
from mbpp_713_code import check_valid

class TestCheckValid(unittest.TestCase):

    def test_normal(self):
        self.assertTrue(check_valid((True, True)))
        self.assertTrue(check_valid((False, False)))

    def test_edge_and_boundary(self):
        self.assertTrue(check_valid((True, False)))
        self.assertTrue(check_valid((False, True)))
        self.assertFalse(check_valid((True,)))
        self.assertFalse(check_valid((),))
        self.assertFalse(check_valid((False,)))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, check_valid, 1)
        self.assertRaises(TypeError, check_valid, ('a', 'b'))

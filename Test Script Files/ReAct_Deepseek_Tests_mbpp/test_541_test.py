import unittest
from mbpp_541_code import check_abundant

class TestAbundantNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(check_abundant(12))
        self.assertFalse(check_abundant(8))
        self.assertTrue(check_abundant(18))
        self.assertFalse(check_abundant(28))

    def test_edge_cases(self):
        self.assertFalse(check_abundant(0))
        self.assertFalse(check_abundant(1))
        self.assertFalse(check_abundant(2))
        self.assertFalse(check_abundant(3))

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            check_abundant('12')
        with self.assertRaises(TypeError):
            check_abundant(None)
        with self.assertRaises(TypeError):
            check_abundant([])

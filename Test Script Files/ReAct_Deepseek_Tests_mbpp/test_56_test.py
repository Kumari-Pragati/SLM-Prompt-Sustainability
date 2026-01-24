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
        self.assertFalse(check(1))
        self.assertFalse(check(11))
        self.assertFalse(check(1001))
        self.assertFalse(check(100001))

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            check('121')
        with self.assertRaises(TypeError):
            check(121.0)

import unittest
from mbpp_752_code import jacobsthal_num

class TestJacobsthalNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(jacobsthal_num(0), 0)
        self.assertEqual(jacobsthal_num(1), 1)
        self.assertEqual(jacobsthal_num(5), 13)
        self.assertEqual(jacobsthal_num(10), 144)

    def test_edge_cases(self):
        self.assertEqual(jacobsthal_num(-1), 0)
        self.assertEqual(jacobsthal_num(20), 1048575)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            jacobsthal_num('a')
        with self.assertRaises(TypeError):
            jacobsthal_num(None)

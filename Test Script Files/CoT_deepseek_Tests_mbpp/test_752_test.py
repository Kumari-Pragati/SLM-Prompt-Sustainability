import unittest
from mbpp_752_code import jacobsthal_num

class TestJacobsthalNum(unittest.TestCase):

    def test_jacobsthal_num_typical_cases(self):
        self.assertEqual(jacobsthal_num(0), 0)
        self.assertEqual(jacobsthal_num(1), 1)
        self.assertEqual(jacobsthal_num(2), 2)
        self.assertEqual(jacobsthal_num(3), 5)
        self.assertEqual(jacobsthal_num(4), 10)
        self.assertEqual(jacobsthal_num(5), 21)

    def test_jacobsthal_num_edge_cases(self):
        self.assertEqual(jacobsthal_num(-1), 0)
        self.assertEqual(jacobsthal_num(-10), 0)
        self.assertEqual(jacobsthal_num(100), 1048575)

    def test_jacobsthal_num_invalid_inputs(self):
        with self.assertRaises(TypeError):
            jacobsthal_num('a')
        with self.assertRaises(TypeError):
            jacobsthal_num(None)
        with self.assertRaises(TypeError):
            jacobsthal_num([])
        with self.assertRaises(TypeError):
            jacobsthal_num({})

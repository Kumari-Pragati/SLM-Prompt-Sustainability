import unittest
from mbpp_752_code import jacobsthal_num

class TestJacobsthalNum(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(jacobsthal_num(0), 0)
        self.assertEqual(jacobsthal_num(1), 1)
        self.assertEqual(jacobsthal_num(2), 2)
        self.assertEqual(jacobsthal_num(3), 5)
        self.assertEqual(jacobsthal_num(4), 11)
        self.assertEqual(jacobsthal_num(5), 24)

    def test_edge_cases(self):
        self.assertEqual(jacobsthal_num(-1), 0)
        self.assertEqual(jacobsthal_num(-2), 0)
        self.assertEqual(jacobsthal_num(0), 0)
        self.assertEqual(jacobsthal_num(1), 1)

    def test_large_inputs(self):
        self.assertEqual(jacobsthal_num(10), 55)
        self.assertEqual(jacobsthal_num(15), 176)
        self.assertEqual(jacobsthal_num(20), 473)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            jacobsthal_num("a")
        with self.assertRaises(TypeError):
            jacobsthal_num(None)

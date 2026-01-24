import unittest
from mbpp_529_code import jacobsthal_lucas

class TestJacobsthalLucas(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(jacobsthal_lucas(0), 2)
        self.assertEqual(jacobsthal_lucas(1), 1)
        self.assertEqual(jacobsthal_lucas(5), 47)
        self.assertEqual(jacobsthal_lucas(10), 10947)

    def test_edge_cases(self):
        self.assertEqual(jacobsthal_lucas(-1), 2)
        self.assertEqual(jacobsthal_lucas(20), 1048575)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            jacobsthal_lucas('a')
        with self.assertRaises(TypeError):
            jacobsthal_lucas(None)

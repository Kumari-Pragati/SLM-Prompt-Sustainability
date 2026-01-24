import unittest
from mbpp_919_code import multiply_list

class TestMultiplyList(unittest.TestCase):

    def test_simple_multiplication(self):
        self.assertEqual(multiply_list([1, 2, 3]), 6)
        self.assertEqual(multiply_list([0, 0, 0]), 0)
        self.assertEqual(multiply_list([4, 4, 4]), 64)

    def test_edge_cases(self):
        self.assertEqual(multiply_list([]), 1)
        self.assertEqual(multiply_list([10, -2, 3]), 60)
        self.assertEqual(multiply_list([-1, -2, -3]), 6)

    def test_complex_scenarios(self):
        self.assertEqual(multiply_list([0, 1, 0, 1, 0, 1]), 1)
        self.assertEqual(multiply_list([1000000001, 1000000002, 1000000003]), 3)

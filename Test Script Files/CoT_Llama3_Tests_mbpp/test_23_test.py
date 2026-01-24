import unittest
from mbpp_23_code import maximum_Sum

class TestMaximumSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 18)

    def test_edge_case(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6]]), 9)

    def test_edge_case2(self):
        self.assertEqual(maximum_Sum([[1, 2, 3]]), 6)

    def test_edge_case3(self):
        self.assertEqual(maximum_Sum([[]]), 0)

    def test_edge_case4(self):
        self.assertEqual(maximum_Sum([[]]), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            maximum_Sum('not a list')

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            maximum_Sum([1, 2, 3, 'not a number'])

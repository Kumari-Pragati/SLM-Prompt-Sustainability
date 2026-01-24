import unittest
from mbpp_65_code import range
from 65_code import recursive_list_sum

class TestRecursiveListSum(unittest.TestCase):

    def test_recursive_list_sum_normal(self):
        self.assertEqual(recursive_list_sum([1, 2, 3]), 6)
        self.assertEqual(recursive_list_sum([[1, 2, 3], [4, 5, 6]]), 21)
        self.assertEqual(recursive_list_sum([[1, 2, 3], [[4, 5, 6]]]), 21)
        self.assertEqual(recursive_list_sum([[1, 2, 3], [[4, 5, 6]], [[7, 8, 9]]]), 31)

    def test_recursive_list_sum_edge_cases(self):
        self.assertEqual(recursive_list_sum([]), 0)
        self.assertEqual(recursive_list_sum([0]), 0)
        self.assertEqual(recursive_list_sum([-1, -2, -3]), -6)
        self.assertEqual(recursive_list_sum([[0], [0]]), 0)
        self.assertEqual(recursive_list_sum([[0, 0], [0]]), 0)
        self.assertEqual(recursive_list_sum([[0], [0, 0]]), 0)
        self.assertEqual(recursive_list_sum([[0, 0], [0, 0]]), 0)

    def test_recursive_list_sum_boundary(self):
        for i in range(100):
            self.assertEqual(recursive_list_sum([i] * i), i * (1 + i) // 2)

    def test_recursive_list_sum_invalid_inputs(self):
        self.assertRaises(TypeError, recursive_list_sum, 123)
        self.assertRaises(TypeError, recursive_list_sum, (1, 2, 3))
        self.assertRaises(TypeError, recursive_list_sum, {1: 2})

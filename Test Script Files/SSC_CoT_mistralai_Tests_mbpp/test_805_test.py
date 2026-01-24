import unittest
from mbpp_805_code import max_sum_list

class TestMaxSumList(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(max_sum_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[7, 8, 9]])
        self.assertEqual(max_sum_list([[1], [2], [3]])), [[1], [2], [3]])
        self.assertEqual(max_sum_list([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), [[-1, -2, -3]])

    def test_edge_cases(self):
        self.assertEqual(max_sum_list([[0, 0, 0]]), [[0, 0, 0]])
        self.assertEqual(max_sum_list([[1], [2], [3], [4]]), [[4]])
        self.assertEqual(max_sum_list([[-1], [-2], [-3], [-4]]), [[-1]])
        self.assertEqual(max_sum_list([[1, 0, 3], [0, 2, 0], [0, 4, 0]]), [[1, 0, 3]])
        self.assertEqual(max_sum_list([[1, 2, 3], [0, 0, 0], [0, 0, 0]]), [[1, 2, 3]])

    def test_empty_list(self):
        self.assertIsNone(max_sum_list([]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_sum_list(123)
        with self.assertRaises(TypeError):
            max_sum_list("abc")

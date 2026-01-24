import unittest
from mbpp_974_code import min_sum_path

class TestMinSumPath(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(min_sum_path([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 1 + min(2, 4) + min(1, min(2, 3)) + min(min(4, 5), min(5, 6)) + min(min(1, min(2, 3)), min(2, 3)) + min(min(4, 5), min(5, 6)))
        self.assertEqual(min_sum_path([[1], [2], [3]]) , 1 + min(2, 2) + min(1, 2))
        self.assertEqual(min_sum_path([[1000000000], [1000000001], [1000000002]]) , 1000000000 + min(1000000001, 1000000002))

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(min_sum_path([[1], [2]]) , 1 + min(2, 2))
        self.assertEqual(min_sum_path([[1], [2, 3]]) , 1 + min(2, 3))
        self.assertEqual(min_sum_path([[1, 2], [3], [4]]) , min(1 + min(2, 3), 3 + min(1, 4)) )
        self.assertEqual(min_sum_path([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) , 1 + min(2, 4) + min(1, min(2, 3)) + min(min(4, 5), min(5, 6)) + min(min(1, min(2, 3)), min(2, 3)) + min(min(4, 5), min(5, 6)) + min(min(1, min(2, 3)), min(2, 3)) + min(min(4, 5), min(5, 6)) + min(min(1, min(2, 3)), min(2, 3)) + min(min(4, 5), min(5, 6)))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_sum_path(123)
        with self.assertRaises(TypeError):
            min_sum_path('abc')

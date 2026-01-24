import unittest
from mbpp_314_code import max_sum_rectangular_grid

class TestMaxSumRectangularGrid(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(max_sum_rectangular_grid([[1, 2], [3, 4]], 2), 10)

    def test_edge_case_1(self):
        self.assertEqual(max_sum_rectangular_grid([[1], [2]], 2), 2)

    def test_edge_case_2(self):
        self.assertEqual(max_sum_rectangular_grid([[1, 2], [3]], 2), 7)

    def test_edge_case_3(self):
        self.assertEqual(max_sum_rectangular_grid([[1, 2], [3, 4], [5, 6]], 3), 20)

    def test_edge_case_4(self):
        self.assertEqual(max_sum_rectangular_grid([[1], [2]], 1), 2)

    def test_edge_case_5(self):
        self.assertEqual(max_sum_rectangular_grid([[1, 2], [3, 4], [5, 6]], 1), 7)

    def test_invalid_input_1(self):
        with self.assertRaises(TypeError):
            max_sum_rectangular_grid(1, 2)

    def test_invalid_input_2(self):
        with self.assertRaises(TypeError):
            max_sum_rectangular_grid([1], '2')

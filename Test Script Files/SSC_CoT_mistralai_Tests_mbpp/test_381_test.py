import unittest
from mbpp_381_code import index_on_inner_list

class TestIndexOnInnerList(unittest.TestCase):

    def test_normal_input(self):
        data = [([1, 2, 3], 0), ([['a', 'b', 'c'], 1), ([([1, 2], [3, 4]), 0)]
        for inner_list, index in data:
            self.assertEqual(index_on_inner_list(inner_list, index), sorted(inner_list, key=lambda x: x[index]))

    def test_edge_and_boundary_conditions(self):
        data = [
            ([[1, 2, 3], 3], [3, 2, 1]),
            ([[1, 2, 3], -1], [1, 2, 3]),
            (([[1, 2], [3, 4]], -1), [ [1, 2], [3, 4] ]),
            (([[1, 2], [3, 4]], 2), [ [3, 4], [1, 2] ]),
            (([], 0), []),
            (([], 1), []),
            (([1], 0), [1]),
            (([1], 1), [1]),
            (([1, 1], 0), [1, 1]),
            (([1, 1], 1), [1, 1]),
        ]
        for inner_list, index in data:
            self.assertEqual(index_on_inner_list(inner_list, index), sorted(inner_list, key=lambda x: x[index]))

    def test_invalid_input(self):
        data = [
            ([1, 2, 3], -2),
            ([1, 2, 3], 3.5),
            ([1, 2, 3], 'a'),
        ]
        for inner_list, index in data:
            with self.assertRaises(TypeError):
                index_on_inner_list(inner_list, index)

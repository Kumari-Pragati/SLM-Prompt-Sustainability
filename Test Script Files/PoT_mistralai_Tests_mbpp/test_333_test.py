import unittest
from mbpp_333_code import Sort

class TestSort(unittest.TestCase):

    def test_sort_typical(self):
        data = [([1, 2], [2, 1]), ([(-1, 2), (0, 1), (1, -1)], [([-1, 2], [0, 1], [1, -1])]), ([([3, 'a'], [2, 'b']), ([1, 'z'], [0, 'y'])], [([[3, 'a'], [0, 'y']], [1, 'z'], [[2, 'b'], [])])]
        for test_data in data:
            self.assertEqual(Sort(test_data), test_data[1])

    def test_sort_edge_and_boundary(self):
        data = [([], []), ([([0, 0]], [([0, 0]]))]
        for test_data in data:
            self.assertEqual(Sort(test_data), test_data[1])

        data = [([[0, 1], [1, 0]], [([[0, 1], [1, 0]]]))]
        for test_data in data:
            self.assertNotEqual(Sort(test_data), test_data[1])

import unittest
from mbpp_50_code import min_length_list

class TestMinLengthList(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(min_length_list([1, 2, 3]), (1, [1]))
        self.assertEqual(min_length_list([4, 4, 4]), (1, [4]))
        self.assertEqual(min_length_list([1, 'a', 3]), (2, ['a']))

    def test_edge_cases(self):
        self.assertEqual(min_length_list([]), (0, []))
        self.assertEqual(min_length_list([None]), (1, [None]))
        self.assertEqual(min_length_list([1, None]), (1, [1]))
        self.assertEqual(min_length_list([1, 'a', None]), (2, ['a']))

    def test_complex_cases(self):
        self.assertEqual(min_length_list([[1, 2], [3, 4], [5, 6, 7]]), (2, [[1, 2]]))
        self.assertEqual(min_length_list([{'a': 1}, {'b': 2}, {'c': 3}]), (1, {'a': 1}))
        self.assertEqual(min_length_list([[1, 2], [3, 4], [5, 6, 7], [8, 9, 10, 11]]), (2, [[1, 2]]))

import unittest
from mbpp_240_code import replace_list

class TestReplaceList(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(replace_list([1, 2, 3], [4, 5]), [1, 2, 4, 5])
        self.assertEqual(replace_list([], [1]), [1])
        self.assertEqual(replace_list([1], []), [1])

    def test_edge_cases(self):
        self.assertEqual(replace_list([1, 2, 3], [4]), [1, 2, 4])
        self.assertEqual(replace_list([1, 2, 3], [4, 5, 6]), [1, 2, 4, 5, 6])
        self.assertEqual(replace_list([1], [2, 3]), [2, 3])
        self.assertEqual(replace_list([1, 2], []), [1, 2])

    def test_complex(self):
        self.assertEqual(replace_list([1, 2, 3], [4, [5, 6]]), [1, 2, 4, [5, 6]])
        self.assertEqual(replace_list([[1], [2], [3]], [[4], [5], [6]]), [[1], [2], [4], [5], [6]])

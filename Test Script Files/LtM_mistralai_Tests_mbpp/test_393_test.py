import unittest
from mbpp_393_code import max_length_list

class TestMaxLengthList(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(max_length_list([1, 2, 3]), (3, [1, 2, 3]))
        self.assertEqual(max_length_list(['a', 'b', 'c']), (3, ['a', 'b', 'c']))
        self.assertEqual(max_length_list([1, 2, 3, 4]), (4, [1, 2, 3, 4]))

    def test_edge_input(self):
        self.assertEqual(max_length_list([]), (0, []))
        self.assertEqual(max_length_list([1]), (1, [1]))
        self.assertEqual(max_length_list([1, 1]), (1, [1, 1]))

    def test_complex_input(self):
        self.assertEqual(max_length_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), (3, [[1, 2, 3]]))
        self.assertEqual(max_length_list([[1], [2], [3]]), (1, [[1]]))
        self.assertEqual(max_length_list([[1, 2], [1, 2, 3], [1, 2, 3, 4]]), (4, [[1, 2, 3, 4]]))

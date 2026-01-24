import unittest
from mbpp_611_code import max_of_nth

class TestMaxOfNth(unittest.TestCase):
    def test_typical_case(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 2
        self.assertEqual(max_of_nth(test_list, N), 9)

    def test_edge_case(self):
        test_list = [[1, 2, 3], [4, 5, 6]]
        N = 2
        self.assertEqual(max_of_nth(test_list, N), 6)

    def test_edge_case2(self):
        test_list = [[1, 2, 3]]
        N = 2
        self.assertEqual(max_of_nth(test_list, N), 3)

    def test_edge_case3(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        N = 2
        self.assertEqual(max_of_nth(test_list, N), 12)

    def test_invalid_input(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 'a'
        with self.assertRaises(TypeError):
            max_of_nth(test_list, N)

    def test_invalid_input2(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = -1
        with self.assertRaises(IndexError):
            max_of_nth(test_list, N)

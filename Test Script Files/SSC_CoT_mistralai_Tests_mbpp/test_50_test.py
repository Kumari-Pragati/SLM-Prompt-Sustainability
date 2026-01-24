import unittest
from mbpp_50_code import min_length_list

class TestMinLengthList(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(min_length_list([[1], [2], [3], [4]]), (1, [1]))
        self.assertEqual(min_length_list([[1], [], [2], [3], [4]]) , (1, [1]))
        self.assertEqual(min_length_list([[1], [2], [], [3], [4]]) , (0, []))

    def test_edge_cases(self):
        self.assertEqual(min_length_list([[1], [2, 2], [3], [4]]) , (1, [1]))
        self.assertEqual(min_length_list([[1], [2], [2], [3], [4]]) , (1, [1]))
        self.assertEqual(min_length_list([[1], [2], [2, 2], [3], [4]]) , (2, [2, 2]))
        self.assertEqual(min_length_list([[1], [2], [2], [3, 3], [4]]) , (2, [2]))
        self.assertEqual(min_length_list([[1], [2], [2], [3, 3, 3], [4]]) , (3, [3, 3, 3]))

    def test_empty_list(self):
        self.assertEqual(min_length_list([]), (0, []))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_length_list(123)
        with self.assertRaises(TypeError):
            min_length_list("abc")

import unittest
from mbpp_60_code import max_len_sub

class TestMaxLenSub(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(max_len_sub([1, 2, 3, 2, 1], 5), 3)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(max_len_sub([5, 4, 3, 2, 1], 5), 2)

    def test_edge_case_1(self):
        self.assertEqual(max_len_sub([1, 2, 2, 3, 4], 5), 3)

    def test_edge_case_2(self):
        self.assertEqual(max_len_sub([1, 2, 2, 2, 3], 5), 3)

    def test_edge_case_3(self):
        self.assertEqual(max_len_sub([1, 1, 2, 2, 3], 5), 3)

    def test_edge_case_4(self):
        self.assertEqual(max_len_sub([1, 2, 3, 2, 1], 1), 1)

    def test_edge_case_5(self):
        self.assertEqual(max_len_sub([1, 2, 3, 2, 1], 0), 0)

    def test_invalid_input_1(self):
        with self.assertRaises(TypeError):
            max_len_sub(["1", "2", "3", "2", "1"], 5)

    def test_invalid_input_2(self):
        with self.assertRaises(TypeError):
            max_len_sub([1, 2, 3, "2", 1], 4)

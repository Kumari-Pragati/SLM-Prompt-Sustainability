import unittest
from mbpp_393_code import max_length_list

class TestMaxLengthList(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(max_length_list([[1, 2], [3, 4, 5], [6]]), (3, [3, 4, 5]))
        self.assertEqual(max_length_list([[1], [2, 3], [4, 5, 6, 7]]), (4, [4, 5, 6, 7]))

    def test_edge_conditions(self):
        self.assertEqual(max_length_list([]), (0, []))
        self.assertEqual(max_length_list([[]]), (0, []))

    def test_complex_cases(self):
        self.assertEqual(max_length_list([[1, 2, 3], [4, 5, 6, 7], [8], [9, 10]]), (4, [4, 5, 6, 7]))
        self.assertEqual(max_length_list([[1, 2, 3], [4, 5, 6, 7], [], [9, 10]]), (4, [4, 5, 6, 7]))

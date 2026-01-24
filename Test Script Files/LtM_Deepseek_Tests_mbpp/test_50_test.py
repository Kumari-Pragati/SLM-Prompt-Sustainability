import unittest
from mbpp_50_code import min_length_list

class TestMinLengthList(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(min_length_list([[1, 2, 3], [4, 5], [6]]), (2, [6]))
        self.assertEqual(min_length_list([[1], [2, 3, 4], [5, 6, 7, 8, 9]]), (1, [1]))

    def test_edge_conditions(self):
        self.assertEqual(min_length_list([]), (0, []))
        self.assertEqual(min_length_list([[]]), (0, []))
        self.assertEqual(min_length_list([[1, 2, 3], [], [4, 5, 6]]), (0, []))

    def test_complex_cases(self):
        self.assertEqual(min_length_list([[1, 2, 3], [4, 5, 6, 7, 8, 9], [10]]), (1, [10]))
        self.assertEqual(min_length_list([[1, 2, 3], [4, 5, 6, 7, 8, 9], [10, 11]]), (2, [10, 11]))

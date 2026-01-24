import unittest
from mbpp_290_code import max_length

class TestMaxLength(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(max_length([1, 2, 3, 4, 5]), (5, 5))
        self.assertEqual(max_length(["hello", "world", "Python"]), (6, "world"))

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(max_length([1, 2, 3, 4, 5, 6]), (6, 6))
        self.assertEqual(max_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), (20, 20))
        self.assertEqual(max_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, "", ""]), (20, 20))
        self.assertEqual(max_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, None]), (20, 20))

    def test_special_cases(self):
        self.assertEqual(max_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, [1], [2], [3]]), (20, 20))
        self.assertEqual(max_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, {"key": "value"}]), (20, 20))
        self.assertEqual(max_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, (1, 2, 3)]), (20, 20))

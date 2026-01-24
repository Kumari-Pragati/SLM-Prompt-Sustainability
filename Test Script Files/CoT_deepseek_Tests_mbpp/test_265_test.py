import unittest
from mbpp_265_code import list_split

class TestListSplit(unittest.TestCase):

    def test_typical_case(self):
        S = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        step = 3
        expected_output = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertEqual(list_split(S, step), expected_output)

    def test_single_element(self):
        S = [1]
        step = 1
        expected_output = [[1]]
        self.assertEqual(list_split(S, step), expected_output)

    def test_empty_list(self):
        S = []
        step = 2
        expected_output = []
        self.assertEqual(list_split(S, step), expected_output)

    def test_step_greater_than_list_length(self):
        S = [1, 2, 3, 4, 5]
        step = 10
        expected_output = [[1, 2, 3, 4, 5]]
        self.assertEqual(list_split(S, step), expected_output)

    def test_step_equal_to_one(self):
        S = [1, 2, 3, 4, 5]
        step = 1
        expected_output = [[1], [2], [3], [4], [5]]
        self.assertEqual(list_split(S, step), expected_output)

    def test_negative_step(self):
        S = [1, 2, 3, 4, 5]
        step = -1
        with self.assertRaises(ValueError):
            list_split(S, step)

    def test_zero_step(self):
        S = [1, 2, 3, 4, 5]
        step = 0
        with self.assertRaises(ValueError):
            list_split(S, step)

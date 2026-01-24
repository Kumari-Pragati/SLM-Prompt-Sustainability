import unittest
from mbpp_154_code import specified_element

class TestSpecifiedElement(unittest.TestCase):

    def test_typical_input(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 1
        result = specified_element(nums, N)
        self.assertEqual(result, [1, 4, 7])

    def test_edge_case(self):
        nums = [[1, 2, 3], [4, 5, 6]]
        N = 2
        result = specified_element(nums, N)
        self.assertEqual(result, [3, 6])

    def test_edge_case2(self):
        nums = [[1, 2, 3]]
        N = 0
        result = specified_element(nums, N)
        self.assertEqual(result, [1])

    def test_edge_case3(self):
        nums = [[1, 2, 3]]
        N = 3
        result = specified_element(nums, N)
        self.assertEqual(result, [3])

    def test_invalid_input(self):
        nums = [[1, 2, 3]]
        N = 'a'
        with self.assertRaises(TypeError):
            specified_element(nums, N)

    def test_empty_input(self):
        nums = []
        N = 1
        result = specified_element(nums, N)
        self.assertEqual(result, [])

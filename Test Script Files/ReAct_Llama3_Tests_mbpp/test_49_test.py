import unittest
from mbpp_49_code import specified_element

class TestSpecifiedElement(unittest.TestCase):
    def test_typical_case(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 1
        result = specified_element(nums, N)
        self.assertEqual(result, [1, 4, 7])

    def test_edge_case(self):
        nums = [[1, 2, 3], [4, 5, 6]]
        N = 2
        result = specified_element(nums, N)
        self.assertEqual(result, [3])

    def test_edge_case2(self):
        nums = [[1, 2, 3]]
        N = 0
        result = specified_element(nums, N)
        self.assertEqual(result, [])

    def test_edge_case3(self):
        nums = []
        N = 1
        result = specified_element(nums, N)
        self.assertEqual(result, [])

    def test_error_case(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 'a'
        with self.assertRaises(TypeError):
            specified_element(nums, N)

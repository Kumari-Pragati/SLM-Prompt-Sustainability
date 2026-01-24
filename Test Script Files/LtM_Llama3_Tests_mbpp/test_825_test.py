import unittest
from mbpp_825_code import access_elements

class TestAccessElements(unittest.TestCase):
    def test_simple_input(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [0, 1, 2]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [1, 2, 3])

    def test_empty_input(self):
        nums = []
        list_index = [0, 1, 2]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [])

    def test_single_element_input(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [0]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [1])

    def test_edge_case_input(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [4]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [5])

    def test_invalid_input(self):
        nums = [1, 2, 3, 4, 5]
        list_index = 'invalid'
        with self.assertRaises(TypeError):
            access_elements(nums, list_index)

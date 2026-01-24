import unittest
from mbpp_825_code import access_elements

class TestAccessElements(unittest.TestCase):
    def test_typical_use_case(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [0, 2, 4]
        self.assertEqual(access_elements(nums, list_index), [1, 3, 5])

    def test_edge_condition(self):
        nums = [1, 2, 3, 4, 5]
        list_index = []
        self.assertEqual(access_elements(nums, list_index), [])

    def test_boundary_condition(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [0, 5]
        self.assertEqual(access_elements(nums, list_index), [1, None])

    def test_invalid_input(self):
        nums = [1, 2, 3, 4, 5]
        list_index = 'a'
        with self.assertRaises(TypeError):
            access_elements(nums, list_index)

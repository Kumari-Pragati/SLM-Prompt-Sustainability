import unittest
from mbpp_415_code import max_Product

class TestMax_Product(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        expected_result = (4, 5)
        self.assertEqual(max_Product(arr), expected_result)

    def test_edge_case_single_element(self):
        arr = [1]
        expected_result = ("No pairs exists")
        self.assertEqual(max_Product(arr), expected_result)

    def test_edge_case_two_elements(self):
        arr = [1, 2]
        expected_result = (1, 2)
        self.assertEqual(max_Product(arr), expected_result)

    def test_edge_case_empty_array(self):
        arr = []
        expected_result = ("No pairs exists")
        self.assertEqual(max_Product(arr), expected_result)

    def test_edge_case_array_with_duplicates(self):
        arr = [1, 2, 2, 3, 4]
        expected_result = (4, 4)
        self.assertEqual(max_Product(arr), expected_result)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            max_Product("Invalid input")

import unittest
from mbpp_753_code import min_k

class TestMinK(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(min_k([], 1), [])

    def test_single_element_list(self):
        self.assertEqual(min_k([[1, 2]], 1), [[1, 2]])

    def test_multiple_elements_list(self):
        self.assertEqual(min_k([[1, 2], [3, 4], [5, 6]], 2), [[1, 2], [3, 4]])

    def test_k_greater_than_list_length(self):
        self.assertEqual(min_k([[1, 2], [3, 4], [5, 6]], 5), [[1, 2], [3, 4], [5, 6]])

    def test_k_equal_to_list_length(self):
        self.assertEqual(min_k([[1, 2], [3, 4], [5, 6]], 3), [[1, 2], [3, 4], [5, 6]])

    def test_k_less_than_list_length(self):
        self.assertEqual(min_k([[1, 2], [3, 4], [5, 6]], 1), [[1, 2]])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            min_k('test', 1)

    def test_invalid_input_value(self):
        with self.assertRaises(TypeError):
            min_k([1, 2, 3], 'test')

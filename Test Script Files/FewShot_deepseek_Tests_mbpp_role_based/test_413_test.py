import unittest
from mbpp_413_code import extract_nth_element

class TestExtractNthElement(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 1
        self.assertEqual(extract_nth_element(list1, n), [2, 5, 8])

    def test_edge_condition(self):
        list1 = [[1], [2], [3]]
        n = 0
        self.assertEqual(extract_nth_element(list1, n), [1, 2, 3])

    def test_boundary_condition(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 3
        self.assertEqual(extract_nth_element(list1, n), [3, 6, 9])

    def test_invalid_input(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 'a'
        with self.assertRaises(TypeError):
            extract_nth_element(list1, n)

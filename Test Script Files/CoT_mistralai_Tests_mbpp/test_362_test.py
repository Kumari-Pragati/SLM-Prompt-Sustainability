import unittest
from mbpp_362_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_occurrences([]), None)

    def test_single_element_list(self):
        for num in range(10):
            self.assertEqual(max_occurrences([num]), num)

    def test_multiple_elements_same_value(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3, 3]), 3)

    def test_multiple_elements_different_values(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 4, 4, 4, 5]), 4)

    def test_edge_case_single_max_value(self):
        self.assertEqual(max_occurrences([1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 1000000000)

    def test_edge_case_multiple_max_values(self):
        self.assertEqual(max_occurrences([1, 1, 1, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]), 1000000000)

    def test_invalid_input_non_iterable(self):
        self.assertRaises(TypeError, max_occurrences, "not a list")

import unittest
from mbpp_815_code import sort_by_dnf

class TestSortByDnf(unittest.TestCase):

    def test_typical_case(self):
        arr = [2, 1, 0, 2, 1, 0]
        expected_output = [0, 0, 1, 1, 2, 2]
        self.assertEqual(sort_by_dnf(arr, len(arr)), expected_output)

    def test_all_zeros(self):
        arr = [0, 0, 0]
        expected_output = [0, 0, 0]
        self.assertEqual(sort_by_dnf(arr, len(arr)), expected_output)

    def test_all_ones(self):
        arr = [1, 1, 1]
        expected_output = [1, 1, 1]
        self.assertEqual(sort_by_dnf(arr, len(arr)), expected_output)

    def test_all_twos(self):
        arr = [2, 2, 2]
        expected_output = [2, 2, 2]
        self.assertEqual(sort_by_dnf(arr, len(arr)), expected_output)

    def test_mixed_elements(self):
        arr = [0, 1, 2, 0, 1, 2]
        expected_output = [0, 0, 1, 1, 2, 2]
        self.assertEqual(sort_by_dnf(arr, len(arr)), expected_output)

    def test_empty_array(self):
        arr = []
        expected_output = []
        self.assertEqual(sort_by_dnf(arr, len(arr)), expected_output)

    def test_single_element(self):
        arr = [1]
        expected_output = [1]
        self.assertEqual(sort_by_dnf(arr, len(arr)), expected_output)

    def test_negative_elements(self):
        arr = [-1, 0, 1, 2]
        self.assertRaises(ValueError, sort_by_dnf, arr, len(arr))

    def test_non_integer_elements(self):
        arr = [0.5, 1.5, 2.5]
        self.assertRaises(ValueError, sort_by_dnf, arr, len(arr))

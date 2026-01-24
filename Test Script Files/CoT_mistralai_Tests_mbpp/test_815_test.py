import unittest
from mbpp_815_code import sort_by_dnf

class TestSortByDNF(unittest.TestCase):
    def test_sort_empty_list(self):
        self.assertEqual(sort_by_dnf([], 0), [])

    def test_sort_single_element(self):
        self.assertEqual(sort_by_dnf([0], 1), [0])
        self.assertEqual(sort_by_dnf([1], 1), [1])
        self.assertEqual(sort_by_dnf([2], 1), [2])

    def test_sort_two_elements(self):
        self.assertEqual(sort_by_dnf([0, 1], 2), [0, 1])
        self.assertEqual(sort_by_dnf([1, 0], 2), [1, 0])
        self.assertEqual(sort_by_dnf([2, 1], 2), [2, 1])
        self.assertEqual(sort_by_dnf([1, 2], 2), [1, 2])
        self.assertEqual(sort_by_dnf([0, 2], 2), [0, 2])

    def test_sort_multiple_elements(self):
        data = [(sort_by_dnf([0, 1, 2, 0, 1, 2, 0, 1], 8), [0, 0, 0, 1, 1, 1, 2, 2]),
                (sort_by_dnf([2, 1, 0, 2, 1, 0, 2, 1], 8), [2, 2, 0, 1, 1, 0, 1, 1]),
                (sort_by_dnf([1, 2, 0, 1, 2, 0, 1, 2], 8), [1, 2, 1, 2, 0, 0, 1, 2])]
        for test_data in data:
            self.assertEqual(test_data[0], test_data[1])

    def test_invalid_input_list(self):
        self.assertRaises(TypeError, sort_by_dnf, 'abc', 3)
        self.assertRaises(TypeError, sort_by_dnf, [1, 2, 3, 'a'], 4)

    def test_invalid_input_n(self):
        self.assertRaises(ValueError, sort_by_dnf, [0, 1], -1)
        self.assertRaises(ValueError, sort_by_dnf, [0, 1], float('inf'))

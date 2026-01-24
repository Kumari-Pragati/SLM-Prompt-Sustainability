import unittest
from mbpp_815_code import sort_by_dnf

class TestSortByDNF(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sort_by_dnf([], 0), [])

    def test_single_element(self):
        self.assertEqual(sort_by_dnf([0], 1), [0])
        self.assertEqual(sort_by_dnf([1], 1), [1])

    def test_simple_list(self):
        self.assertEqual(sort_by_dnf([1, 0, 1, 0, 1, 0, 1, 0, 1, 0], 10), [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1])

    def test_reverse_list(self):
        self.assertEqual(sort_by_dnf([1, 0, 1, 0, 1, 0, 1, 0, 1, 0], 10), [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(sort_by_dnf([0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 10), [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1])

    def test_complex_list(self):
        self.assertEqual(sort_by_dnf([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1], 27),
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1])

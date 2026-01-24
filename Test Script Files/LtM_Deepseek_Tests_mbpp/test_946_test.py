import unittest
from mbpp_946_code import most_common_elem

class TestMostCommonElem(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(most_common_elem([1, 2, 2, 3, 3, 3], 1), [(3, 3)])

    def test_typical_input(self):
        self.assertEqual(most_common_elem([1, 2, 2, 3, 3, 3], 2), [(3, 3), (2, 2)])

    def test_empty_input(self):
        self.assertEqual(most_common_elem([], 1), [])

    def test_maximum_values(self):
        self.assertEqual(most_common_elem([1]*1000000, 1), [(1, 1000000)])

    def test_special_flag(self):
        self.assertEqual(most_common_elem([1, 2, 2, 3, 3, 3], 0), [])

    def test_more_complex_case(self):
        self.assertEqual(most_common_elem(['a', 'b', 'b', 'c', 'c', 'c'], 2), [('c', 3), ('b', 2)])

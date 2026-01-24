import unittest
from mbpp_456_code import reverse_string_list

class TestReverseStringList(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(reverse_string_list(['abc', 'def']), ['cba', 'fed'])
        self.assertEqual(reverse_string_list(['123', '456']), ['321', '654'])

    def test_edge_conditions(self):
        self.assertEqual(reverse_string_list([]), [])
        self.assertEqual(reverse_string_list(['']), [''])

    def test_complex_cases(self):
        self.assertEqual(reverse_string_list(['abcd', 'efgh']), ['dcba', 'hgfe'])
        self.assertEqual(reverse_string_list(['1234', '5678']), ['4321', '8765'])

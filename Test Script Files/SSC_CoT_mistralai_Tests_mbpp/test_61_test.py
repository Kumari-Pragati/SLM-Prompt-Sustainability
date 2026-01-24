import unittest
from mbpp_61_code import defaultdict
from six.moves import range

from61_code import count_Substrings

class TestCountSubstrings(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_Substrings('1234', 4), 3)
        self.assertEqual(count_Substrings('0123', 4), 2)
        self.assertEqual(count_Substrings('5678', 4), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Substrings('1', 1), 1)
        self.assertEqual(count_Substrings('12', 2), 2)
        self.assertEqual(count_Substrings('123', 3), 3)
        self.assertEqual(count_Substrings('1234', 5), 6)
        self.assertEqual(count_Substrings('12345', 6), 10)
        self.assertEqual(count_Substrings('123456', 7), 15)

        self.assertEqual(count_Substrings('1234567', 8), 22)
        self.assertEqual(count_Substrings('12345678', 9), 30)
        self.assertEqual(count_Substrings('123456789', 10), 42)

    def test_special_cases(self):
        self.assertEqual(count_Substrings('101', 3), 2)
        self.assertEqual(count_Substrings('1001', 4), 2)
        self.assertEqual(count_Substrings('1111', 4), 4)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, count_Substrings, '', 4)
        self.assertRaises(ValueError, count_Substrings, '123x', 4)
        self.assertRaises(ValueError, count_Substrings, '123', -1)
        self.assertRaises(ValueError, count_Substrings, '123', 0)

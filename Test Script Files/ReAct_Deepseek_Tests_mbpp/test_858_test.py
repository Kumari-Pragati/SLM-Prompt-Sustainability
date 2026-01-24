import unittest
from mbpp_858_code import count_list

class TestCountList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_list([1, 2, 3]), 9)

    def test_empty_list(self):
        self.assertEqual(count_list([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count_list([1]), 1)

    def test_large_list(self):
        self.assertEqual(count_list(list(range(1, 1001))), 1000000)

    def test_negative_numbers(self):
        self.assertEqual(count_list([-1, -2, -3]), 9)

    def test_zero(self):
        self.assertEqual(count_list([0]), 1)

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            count_list([1, 'two', 3.0])

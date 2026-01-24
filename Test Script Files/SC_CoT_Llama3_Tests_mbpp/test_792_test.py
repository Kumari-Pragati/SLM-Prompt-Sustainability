import unittest
from mbpp_792_code import count_list

class TestCountList(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(count_list([1, 2, 3, 4, 5]), 5)

    def test_empty_list(self):
        self.assertEqual(count_list([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count_list([1]), 1)

    def test_large_list(self):
        self.assertEqual(count_list([i for i in range(100)]), 100)

    def test_list_with_duplicates(self):
        self.assertEqual(count_list([1, 2, 2, 3, 3, 3, 4, 5, 5, 5]), 5)

    def test_list_with_negative_numbers(self):
        self.assertEqual(count_list([-1, -2, -3, 0, 1, 2, 3]), 7)

    def test_list_with_mixed_types(self):
        with self.assertRaises(TypeError):
            count_list([1, 'a', 2, 3.0, None])

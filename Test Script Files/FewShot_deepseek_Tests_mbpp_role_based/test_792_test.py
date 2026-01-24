import unittest
from mbpp_792_code import count_list

class TestCountList(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_list([1, 2, 3, 4, 5]), 5)

    def test_empty_list(self):
        self.assertEqual(count_list([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count_list([1]), 1)

    def test_large_list(self):
        self.assertEqual(count_list(list(range(1, 1001))), 1000)

    def test_list_with_duplicates(self):
        self.assertEqual(count_list([1, 2, 2, 3, 4]), 5)

    def test_list_with_non_integer_elements(self):
        self.assertEqual(count_list(['a', 'b', 'c']), 3)

    def test_list_with_mixed_elements(self):
        self.assertEqual(count_list([1, 'a', 2.0, None]), 4)

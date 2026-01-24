import unittest
from mbpp_792_code import count_list

class TestCountList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_list([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count_list([1]), 1)

    def test_multiple_element_list(self):
        self.assertEqual(count_list([1, 2, 3, 4, 5]), 5)

    def test_duplicate_elements_list(self):
        self.assertEqual(count_list([1, 1, 1, 1, 1]), 5)

    def test_mixed_type_list(self):
        self.assertEqual(count_list([1, 'a', True, None]), 4)

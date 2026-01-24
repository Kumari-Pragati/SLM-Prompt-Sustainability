import unittest
from mbpp_791_code import remove_nested

class TestRemoveNested(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_nested(()), ())

    def test_single_element(self):
        self.assertEqual(remove_nested((1,)), (1,))

    def test_single_nested_element(self):
        self.assertEqual(remove_nested((1, (2, 3))), (1,))

    def test_multiple_elements(self):
        self.assertEqual(remove_nested((1, 2, (3, 4))), (1, 2))

    def test_multiple_nested_elements(self):
        self.assertEqual(remove_nested((1, (2, (3, (4, 5))), 6)), (1, 2))

    def test_nested_with_non_tuple_elements(self):
        self.assertEqual(remove_nested((1, (2, '3'), 4)), (1, 2))

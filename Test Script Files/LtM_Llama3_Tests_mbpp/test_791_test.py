import unittest
from mbpp_791_code import remove_nested

class TestRemoveNested(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(remove_nested(()), ())

    def test_single_element(self):
        self.assertEqual(remove_nested((1,)), (1,))

    def test_nested_tuples(self):
        self.assertEqual(remove_nested((1, (2, 3), 4)), (1, 2, 3, 4))

    def test_non_nested_tuples(self):
        self.assertEqual(remove_nested((1, 2, 3)), (1, 2, 3))

    def test_mixed_input(self):
        self.assertEqual(remove_nested((1, (2, 3), 4, (5, 6))), (1, 2, 3, 4, 5, 6))

    def test_empty_input_list(self):
        self.assertEqual(remove_nested([]), ())

    def test_single_element_list(self):
        self.assertEqual(remove_nested([1]), [1])

    def test_nested_tuples_list(self):
        self.assertEqual(remove_nested([1, (2, 3), 4]), [1, 2, 3, 4])

    def test_non_nested_tuples_list(self):
        self.assertEqual(remove_nested([1, 2, 3]), [1, 2, 3])

    def test_mixed_input_list(self):
        self.assertEqual(remove_nested([1, (2, 3), 4, (5, 6)]), [1, 2, 3, 4, 5, 6])

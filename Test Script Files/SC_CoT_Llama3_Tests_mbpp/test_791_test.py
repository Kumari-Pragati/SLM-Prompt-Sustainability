import unittest
from mbpp_791_code import remove_nested

class TestRemoveNested(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(remove_nested((1, 2, 3, 4)), (1, 2, 3, 4))

    def test_nested_input(self):
        self.assertEqual(remove_nested((1, (2, 3), 4)), (1, 2, 3, 4))

    def test_empty_input(self):
        self.assertEqual(remove_nested(()), ())

    def test_single_tuple_input(self):
        self.assertEqual(remove_nested((1,)), (1,))

    def test_single_non_tuple_input(self):
        self.assertEqual(remove_nested([1]), (1,))

    def test_mixed_input(self):
        self.assertEqual(remove_nested((1, 2, (3, 4), 5)), (1, 2, 3, 4, 5))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            remove_nested('Invalid Input')

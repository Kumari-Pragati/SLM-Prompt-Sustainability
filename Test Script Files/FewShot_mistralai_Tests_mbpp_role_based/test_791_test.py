import unittest
from mbpp_791_code import remove_nested

class TestRemoveNested(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_nested(()), ())

    def test_single_element(self):
        self.assertEqual(remove_nested((1,)), (1,))

    def test_multiple_elements(self):
        self.assertEqual(remove_nested((1, 2, (3, 4))), (1, 2))

    def test_nested_tuples(self):
        self.assertEqual(remove_nested(((1,), (2, (3, 4))))), ((1,), (2,)))

    def test_mixed_types(self):
        self.assertEqual(remove_nested((1, 'a', (2, 3))), (1, 'a'))

    def test_empty_tuple(self):
        self.assertEqual(remove_nested((),), ())

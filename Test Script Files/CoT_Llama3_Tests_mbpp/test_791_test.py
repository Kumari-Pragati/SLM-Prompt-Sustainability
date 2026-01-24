import unittest
from mbpp_791_code import remove_nested

class TestRemoveNested(unittest.TestCase):
    def test_no_nested(self):
        self.assertEqual(remove_nested((1, 2, 3)), (1, 2, 3))

    def test_single_nested(self):
        self.assertEqual(remove_nested((1, (2, 3), 4)), (1, 2, 3, 4))

    def test_multiple_nested(self):
        self.assertEqual(remove_nested((1, (2, 3), (4, 5), 6)), (1, 2, 3, 4, 5, 6))

    def test_empty_input(self):
        self.assertEqual(remove_nested(()), ())

    def test_single_element(self):
        self.assertEqual(remove_nested((1,)), (1,))

    def test_no_elements(self):
        self.assertEqual(remove_nested(()), ())

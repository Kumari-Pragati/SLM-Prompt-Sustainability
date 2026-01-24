import unittest
from mbpp_791_code import remove_nested

class TestRemoveNested(unittest.TestCase):

    def test_typical_case(self):
        test_tup = (1, (2, 3), 4, (5, (6, 7), 8), 9)
        expected_result = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertEqual(remove_nested(test_tup), expected_result)

    def test_empty_tuple(self):
        test_tup = ()
        expected_result = ()
        self.assertEqual(remove_nested(test_tup), expected_result)

    def test_tuple_with_single_element(self):
        test_tup = (1,)
        expected_result = (1,)
        self.assertEqual(remove_nested(test_tup), expected_result)

    def test_tuple_with_all_nested_elements(self):
        test_tup = ((1,), (2,), (3,))
        expected_result = (1, 2, 3)
        self.assertEqual(remove_nested(test_tup), expected_result)

    def test_tuple_with_mixed_elements(self):
        test_tup = (1, 'a', (2, 3), 'b', (4,))
        expected_result = (1, 'a', 2, 3, 'b', 4)
        self.assertEqual(remove_nested(test_tup), expected_result)

    def test_tuple_with_nested_tuple_at_end(self):
        test_tup = (1, 2, 3, (4, 5))
        expected_result = (1, 2, 3, 4, 5)
        self.assertEqual(remove_nested(test_tup), expected_result)

import unittest
from mbpp_791_code import remove_nested

class TestRemoveNested(unittest.TestCase):

    def test_simple_single_element(self):
        self.assertEqual(remove_nested((1,)), (1,))

    def test_simple_multiple_elements(self):
        self.assertEqual(remove_nested((1, 2, 3)), (1, 2, 3))

    def test_simple_single_tuple(self):
        self.assertEqual(remove_nested(((1,),)), (1,))

    def test_simple_multiple_tuples(self):
        self.assertEqual(remove_nested(((1,), (2, 3)),), (1, 2, 3))

    def test_empty_input(self):
        self.assertEqual(remove_nested(()), ())

    def test_single_empty_tuple(self):
        self.assertEqual(remove_nested(((),)), ())

    def test_multiple_empty_tuples(self):
        self.assertEqual(remove_nested(((), (), ((1,),)),), ())

    def test_single_non_tuple_element(self):
        self.assertEqual(remove_nested((1, 'a')), (1,))

    def test_multiple_non_tuple_elements(self):
        self.assertEqual(remove_nested((1, 'a', 2)), (1, 'a'))

    def test_single_tuple_with_non_tuple_element(self):
        self.assertEqual(remove_nested(((1,), 'a')), (1,))

    def test_multiple_tuples_with_non_tuple_elements(self):
        self.assertEqual(remove_nested(((1,), 'a', (2,)),), (1, 'a'))

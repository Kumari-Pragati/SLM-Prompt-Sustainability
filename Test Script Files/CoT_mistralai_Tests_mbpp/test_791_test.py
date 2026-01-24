import unittest
from mbpp_791_code import remove_nested

class TestRemoveNested(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertTupleEqual(remove_nested(()), ())

    def test_single_element(self):
        self.assertTupleEqual(remove_nested((1)), (1,))

    def test_multiple_elements(self):
        self.assertTupleEqual(remove_nested((1, 2, 3)), (1, 2, 3))

    def test_tuple_with_single_element_tuple(self):
        self.assertTupleEqual(remove_nested(((1),)), (1,))

    def test_tuple_with_multiple_element_tuples(self):
        self.assertTupleEqual(remove_nested(((1, 2), (3, 4))), (1, 2, 3, 4))

    def test_nesting_levels(self):
        self.assertTupleEqual(remove_nested(((1, (2, (3, (4, (5,))))))), (1, 2, 3, 4, 5))

    def test_mixed_types(self):
        self.assertRaises(TypeError, remove_nested, (1, 'a', (2, 3)))

    def test_all_tuples(self):
        self.assertRaises(TypeError, remove_nested, (((),),))

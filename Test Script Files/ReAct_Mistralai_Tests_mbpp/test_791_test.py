import unittest
from mbpp_791_code import remove_nested

class TestRemoveNested(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertEqual(remove_nested(()), ())

    def test_single_element(self):
        self.assertEqual(remove_nested((1,)), (1,))
        self.assertEqual(remove_nested((1, 2)), (1, 2))

    def test_multiple_elements(self):
        self.assertEqual(remove_nested((1, (2, 3), 4)), (1, 4))
        self.assertEqual(remove_nested((1, (2,), 3)), (1, 3))
        self.assertEqual(remove_nested((1, (2, 3), (4, 5))), (1, (2, 3), (4, 5)))

    def test_nested_tuples_of_different_depths(self):
        self.assertEqual(remove_nested(((1,), (2, (3, 4)), (5, 6))), (1, (2, (3, 4)), (5, 6)))
        self.assertEqual(remove_nested(((1,), (2, (3,)), (4, 5))) , (1, (2, (3,)), (4, 5)))

    def test_empty_tuple_in_nested_tuple(self):
        self.assertEqual(remove_nested(((1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (), (10,))) , ((1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)))

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            remove_nested((1, 'a', (2,)))

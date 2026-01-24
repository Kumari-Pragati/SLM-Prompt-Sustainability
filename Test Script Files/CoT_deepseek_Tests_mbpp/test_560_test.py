import unittest
from mbpp_560_code import union_elements

class TestUnionElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(union_elements((1, 2, 3), (3, 4, 5)), (1, 2, 3, 4, 5))

    def test_empty_tuples(self):
        self.assertEqual(union_elements((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(union_elements((1,), (1,)), (1,))

    def test_duplicate_elements(self):
        self.assertEqual(union_elements((1, 2, 2), (2, 3, 3)), (1, 2, 3))

    def test_large_tuples(self):
        self.assertEqual(union_elements(tuple(range(1000)), tuple(range(500, 1500))), 
                         tuple(range(1000)) + tuple(range(500, 1500)))

    def test_negative_numbers(self):
        self.assertEqual(union_elements((-1, -2, -3), (-3, -4, -5)), (-1, -2, -3, -4, -5))

    def test_mixed_types(self):
        self.assertEqual(union_elements((1, 'a', 3.0), (3, 'b', 1.0)), (1, 'a', 3.0, 3, 'b'))

    def test_non_tuple_inputs(self):
        with self.assertRaises(TypeError):
            union_elements((1, 2, 3), 'not a tuple')

        with self.assertRaises(TypeError):
            union_elements('not a tuple', (1, 2, 3))

        with self.assertRaises(TypeError):
            union_elements('not a tuple', 'not a tuple')

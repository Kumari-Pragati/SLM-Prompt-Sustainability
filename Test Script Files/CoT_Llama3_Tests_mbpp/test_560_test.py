import unittest
from mbpp_560_code import union_elements

class TestUnionElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(union_elements((1, 2, 3), (4, 5, 6)), (1, 2, 3, 4, 5, 6))

    def test_empty_input(self):
        self.assertEqual(union_elements((), ()), ())

    def test_single_input(self):
        self.assertEqual(union_elements((1, 2, 3),()), (1, 2, 3))

    def test_duplicates(self):
        self.assertEqual(union_elements((1, 2, 2), (2, 3)), (1, 2, 3))

    def test_order_matters(self):
        self.assertEqual(union_elements((1, 2, 3), (3, 2, 1)), (1, 2, 3))

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            union_elements((1, 2, 3), ('a', 'b', 'c'))

    def test_mixed_input(self):
        self.assertEqual(union_elements((1, 2, 3), ('a', 'b')), (1, 2, 3, 'a', 'b'))

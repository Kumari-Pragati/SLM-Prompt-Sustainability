import unittest
from mbpp_560_code import union_elements

class TestUnionElements(unittest.TestCase):

    def test_empty_tuples(self):
        self.assertEqual(union_elements((), ()), ())

    def test_single_tuple(self):
        self.assertEqual(union_elements((1,), ()), (1,))
        self.assertEqual(union_elements((), (1,)), (1,))

    def test_multiple_tuples(self):
        self.assertEqual(union_elements((1, 2), (2, 3)), (1, 2, 3))
        self.assertEqual(union_elements((1, 2, 3), (2, 3, 4)), (1, 2, 3, 4))

    def test_duplicates(self):
        self.assertEqual(union_elements((1, 1, 2), (2, 2, 3)), (1, 2, 3))

    def test_order_matters(self):
        self.assertEqual(union_elements((1, 2), (2, 1)), (1, 2))

    def test_non_integer_elements(self):
        self.assertEqual(union_elements((1, 2, 'a'), (2, 3, 'b')), (1, 2, 3, 'a', 'b'))

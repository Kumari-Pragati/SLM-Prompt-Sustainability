import unittest
from mbpp_560_code import union_elements

class TestUnionElements(unittest.TestCase):

    def test_union_elements(self):
        self.assertEqual(union_elements((1, 2, 3), (2, 3, 4)), (1, 2, 3, 4))
        self.assertEqual(union_elements((1, 2, 3), (3, 4, 5)), (1, 2, 3, 4, 5))
        self.assertEqual(union_elements((1, 2, 3), (1, 2, 3)), (1, 2, 3))
        self.assertEqual(union_elements((1, 2, 3), ()), (1, 2, 3))
        self.assertEqual(union_elements((), (1, 2, 3)), (1, 2, 3))
        self.assertEqual(union_elements((1, 2, 3), (4, 5, 6)), (1, 2, 3, 4, 5, 6))
        self.assertEqual(union_elements((1, 2, 3), (1, 2, 3, 4, 5, 6)), (1, 2, 3, 4, 5, 6))

    def test_union_elements_empty(self):
        self.assertEqual(union_elements((), ()), ())

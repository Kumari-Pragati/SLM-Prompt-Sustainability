import unittest
from mbpp_560_code import union_elements

class TestUnionElements(unittest.TestCase):

    def test_simple_union(self):
        self.assertEqual(union_elements((1, 2, 3), (3, 4, 5)), (1, 2, 3, 4, 5))
        self.assertEqual(union_elements((), (1,)), (1,))
        self.assertEqual(union_elements((1,), ()), (1,))

    def test_edge_cases(self):
        self.assertEqual(union_elements((0,), (1,)), (0, 1))
        self.assertEqual(union_elements((1000000000,), (1,)), (1, 1000000000))
        self.assertEqual(union_elements((1,), (1000000000,)), (1, 1000000000))
        self.assertEqual(union_elements((1,), (1,)), (1,))
        self.assertEqual(union_elements((1,), (1, 1)), (1, 1))

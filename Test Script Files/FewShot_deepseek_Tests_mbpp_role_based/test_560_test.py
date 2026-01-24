import unittest
from mbpp_560_code import union_elements

class TestUnionElements(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(union_elements((1, 2, 3), (3, 4, 5)), (1, 2, 3, 4, 5))

    def test_empty_tuples(self):
        self.assertEqual(union_elements((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(union_elements((1,), (1,)), (1,))

    def test_duplicate_elements(self):
        self.assertEqual(union_elements((1, 2, 2), (2, 3, 3)), (1, 2, 3))

    def test_large_tuples(self):
        self.assertEqual(union_elements(tuple(range(1000)), tuple(range(1000, 2000))), 
                         tuple(range(1000, 2000)))

    def test_unordered_tuples(self):
        self.assertEqual(union_elements((3, 2, 1), (1, 2, 3)), (1, 2, 3))

import unittest
from mbpp_473_code import tuple_intersection

class TestTupleIntersection(unittest.TestCase):
    def test_empty_lists(self):
        self.assertListEqual(tuple_intersection([], []), [])

    def test_single_element_lists(self):
        self.assertListEqual(tuple_intersection([(1, 2)], []), [])
        self.assertListEqual(tuple_intersection([], [(1, 2)]), [])
        self.assertListEqual(tuple_intersection([(1, 2)], [(1, 2)]), [(1, 2)])

    def test_simple_intersection(self):
        self.assertListEqual(tuple_intersection([(1, 2), (3, 4)], [(2, 3), (3, 4)]), [(3, 4)])

    def test_complex_intersection(self):
        self.assertListEqual(tuple_intersection([(1, 2), (3, 4), (5, 6)], [(2, 3), (3, 4), (4, 5)]), [(3, 4)])

    def test_duplicate_elements(self):
        self.assertListEqual(tuple_intersection([(1, 2), (1, 2)], [(1, 2)]), [(1, 2)])

    def test_sorted_elements(self):
        self.assertListEqual(tuple_intersection([(2, 1), (1, 2)], [(1, 2), (2, 1)]), [(1, 2)])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            tuple_intersection([1, 2], [(1, 2)])

import unittest
from mbpp_487_code import sort_tuple

class TestSortTuple(unittest.TestCase):

    def test_sort_ascending(self):
        self.assertEqual(sort_tuple((1, 2, 3)), ((1, 2, 3)))
        self.assertEqual(sort_tuple((5, 3, 1)), ((1, 3, 5)))
        self.assertEqual(sort_tuple((-1, 0, 2)), ((-1, 0, 2)))

    def test_sort_descending(self):
        self.assertEqual(sort_tuple((3, 2, 1)), ((3, 2, 1), reversed=True))
        self.assertEqual(sort_tuple((5, 3, 1)), ((5, 3, 1), reversed=True))
        self.assertEqual(sort_tuple((-1, 0, 2)), ((-1, 0, 2), reversed=True))

    def test_empty_list(self):
        self.assertEqual(sort_tuple([]), [])

    def test_single_element(self):
        self.assertEqual(sort_tuple((1,)), (1,))
        self.assertEqual(sort_tuple((-1,)), (-1,))

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            sort_tuple((1, "a", 2))
        with self.assertRaises(TypeError):
            sort_tuple((1, 2, "a"))

    def test_duplicate_elements(self):
        self.assertEqual(sort_tuple((1, 1, 2)), (1, 1, 2))
        self.assertEqual(sort_tuple((-1, -1, 1)), (-1, -1, 1))

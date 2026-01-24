import unittest
from mbpp_243_code import sort_on_occurence

class TestSortOnOccurence(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(sort_on_occurence([(1, 2), (1, 3), (2, 2), (2, 3), (3, 1), (3, 2)]), [((1,), [2, 3], 2), ((2,), [2, 3], 2), ((3,), [1, 2], 2)])

    def test_edge_cases(self):
        self.assertEqual(sort_on_occurence([(1, 2), (1, 2), (1, 2)]), [((1,), [2], 3), ((2,), [], 0)])
        self.assertEqual(sort_on_occurence([(1, 2), (1, 2, 3)]), [((1,), [2], 2), ((1, 2, 3), [], 1)])
        self.assertEqual(sort_on_occurence([(1, 2), (1, 2, 3), (1,)]), [((1,), [2], 2), ((1, 2, 3), [], 1)])
        self.assertEqual(sort_on_occurence([(1, 2), (1, 2, 3), (1, 2)]), [((1,), [2], 2), ((1, 2), [3], 1), ((1, 2, 3), [], 1)])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_on_occurence(1)
        with self.assertRaises(TypeError):
            sort_on_occurence([1])
        with self.assertRaises(TypeError):
            sort_on_occurence([(1,), 2])

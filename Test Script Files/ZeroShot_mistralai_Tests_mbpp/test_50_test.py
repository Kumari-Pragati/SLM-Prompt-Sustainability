import unittest
from mbpp_50_code import min_length_list

class TestMinLengthList(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(min_length_list([]))

    def test_single_element_list(self):
        self.assertEqual(min_length_list([1]), (1, [1]))

    def test_multiple_elements_with_same_length(self):
        self.assertEqual(min_length_list([[1, 2], [3, 4], [1, 2]]), (2, [[1, 2]]))

    def test_multiple_elements_with_different_lengths(self):
        self.assertEqual(min_length_list([[1, 2], [3], [1, 2, 3, 4]]), ((2,), [ [1, 2] ]))

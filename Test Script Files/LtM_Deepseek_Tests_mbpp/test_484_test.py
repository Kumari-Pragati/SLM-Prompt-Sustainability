import unittest
from mbpp_484_code import remove_matching_tuple

class TestRemoveMatchingTuple(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_input(self):
        self.assertEqual(remove_matching_tuple([1, 2, 3], [2, 3]), [1])

    # Test for edge and boundary conditions
    def test_empty_input(self):
        self.assertEqual(remove_matching_tuple([], []), [])
        self.assertEqual(remove_matching_tuple([], [1, 2, 3]), [])
        self.assertEqual(remove_matching_tuple([1, 2, 3], []), [1, 2, 3])

    def test_single_element(self):
        self.assertEqual(remove_matching_tuple([1], [1]), [])
        self.assertEqual(remove_matching_tuple([1], [2]), [1])

    # Test for more complex or corner cases
    def test_duplicates(self):
        self.assertEqual(remove_matching_tuple([1, 2, 2, 3], [2]), [1, 3])
        self.assertEqual(remove_matching_tuple([1, 2, 2, 3], [2, 2]), [1, 3])

    def test_no_match(self):
        self.assertEqual(remove_matching_tuple([1, 2, 3], [4, 5, 6]), [1, 2, 3])

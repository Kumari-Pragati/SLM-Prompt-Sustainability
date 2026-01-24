import unittest
from mbpp_259_code import maximize_elements

class TestMaximizeElements(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(maximize_elements([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(maximize_elements([1], [2]), [1])
        self.assertEqual(maximize_elements([2], [1]), [2])

    def test_equal_length_lists(self):
        self.assertEqual(maximize_elements([1, 2, 3], [4, 5, 6]), [2, 5, 6])
        self.assertEqual(maximize_elements([4, 5, 6], [1, 2, 3]), [4, 5, 3])

    def test_unequal_length_lists(self):
        self.assertEqual(maximize_elements([1, 2, 3], [4, 5]), [2, 5])
        self.assertEqual(maximize_elements([4, 5], [1, 2, 3, 4]), [5, 2, 3, 4])

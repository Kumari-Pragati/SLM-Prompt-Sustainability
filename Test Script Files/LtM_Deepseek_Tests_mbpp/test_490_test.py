import unittest
from mbpp_490_code import extract_symmetric

class TestExtractSymmetric(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_input(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 1)]), {(1, 2)})

    # Test for edge and boundary conditions
    def test_empty_input(self):
        self.assertEqual(extract_symmetric([]), set())

    def test_single_element_input(self):
        self.assertEqual(extract_symmetric([(1, 1)]), set())

    # Test for more complex or corner cases
    def test_duplicate_pairs(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 1), (1, 2)]), {(1, 2)})

    def test_unsorted_pairs(self):
        self.assertEqual(extract_symmetric([(2, 1), (1, 2)]), {(1, 2)})

    def test_same_elements(self):
        self.assertEqual(extract_symmetric([(1, 1)]), set())

    def test_large_input(self):
        large_input = [(i, i+1) for i in range(1, 1000)]
        self.assertEqual(extract_symmetric(large_input), {(i, i+1) for i in range(1, 500)})

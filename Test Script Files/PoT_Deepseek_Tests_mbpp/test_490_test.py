import unittest
from mbpp_490_code import extract_symmetric

class TestExtractSymmetric(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 1), (3, 4)]), {(1, 2)})

    def test_empty_list(self):
        self.assertEqual(extract_symmetric([]), set())

    def test_single_element(self):
        self.assertEqual(extract_symmetric([(1, 1)]), set())

    def test_duplicate_pairs(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 1), (1, 2)]), {(1, 2)})

    def test_same_elements(self):
        self.assertEqual(extract_symmetric([(1, 1)]), set())

    def test_reverse_pairs(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 1)]), {(1, 2)})

    def test_unordered_pairs(self):
        self.assertEqual(extract_symmetric([(2, 1), (1, 2)]), {(1, 2)})

    def test_negative_numbers(self):
        self.assertEqual(extract_symmetric([(-1, 1), (1, -1)]), {(-1, 1)})

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            extract_symmetric([(1, '2'), ('2', 1)])

import unittest
from mbpp_898_code import extract_elements

class TestExtractElements(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 1, 1], 2), [1, 1, 2, 2, 3, 3])

    def test_edge_condition(self):
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 1, 1], 1), [1, 1, 2, 2, 3, 3, 1, 1])

    def test_boundary_condition(self):
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 1, 1], 0), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_elements("1, 1, 2, 2, 3, 3, 1, 1", 2)

        with self.assertRaises(TypeError):
            extract_elements([1, 1, 2, 2, 3, 3, 1, 1], "2")

        with self.assertRaises(ValueError):
            extract_elements([1, 1, 2, 2, 3, 3, 1, 1], -1)

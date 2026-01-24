import unittest
from mbpp_760_code import unique_Element

class TestUniqueElement(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(unique_Element([1, 2, 3, 4, 5], 5), 'YES')

    def test_edge_condition(self):
        self.assertEqual(unique_Element([1], 1), 'YES')

    def test_boundary_condition(self):
        self.assertEqual(unique_Element([1, 2], 2), 'NO')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            unique_Element("1, 2, 3, 4, 5", 5)

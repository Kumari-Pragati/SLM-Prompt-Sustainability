import unittest
from mbpp_361_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_empty(['', 'a', '', 'b', '']), ['a', 'b'])

    def test_edge_condition(self):
        self.assertEqual(remove_empty(['']), [])

    def test_boundary_condition(self):
        self.assertEqual(remove_empty(['', '']), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_empty(123)

    def test_empty_list(self):
        self.assertEqual(remove_empty([]), [])

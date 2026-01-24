import unittest
from mbpp_502_code import find

class TestFindFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find(10, 3), 1)

    def test_boundary_case(self):
        self.assertEqual(find(0, 5), 0)
        self.assertEqual(find(10, 1), 0)

    def test_edge_case(self):
        self.assertEqual(find(10, 0), None)  # Assuming the function returns None for zero division

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find('10', 3)
        with self.assertRaises(TypeError):
            find(10, '3')
        with self.assertRaises(TypeError):
            find('10', '3')

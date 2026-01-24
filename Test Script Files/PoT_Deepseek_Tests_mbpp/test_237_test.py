import unittest
from mbpp_237_code import check_occurences

class TestCheckOccurences(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check_occurences([[1, 2], [2, 1], [1, 1]]), {(1, 2): 1, (2, 1): 1})

    def test_edge_case(self):
        self.assertEqual(check_occurences([[]]), {})

    def test_boundary_case(self):
        self.assertEqual(check_occurences([[1], [1]]), {(1,): 2})

    def test_corner_case(self):
        self.assertEqual(check_occurences([[1, 2, 3], [3, 2, 1]]), {(1, 2, 3): 1, (3, 2, 1): 1})

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_occurences(123)

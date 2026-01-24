import unittest
from mbpp_715_code import str_to_tuple

class TestStrToTuple(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(str_to_tuple('1, 2, 3, 4, 5'), (1, 2, 3, 4, 5))

    def test_edge_case(self):
        self.assertEqual(str_to_tuple(''), ())

    def test_boundary_case(self):
        self.assertEqual(str_to_tuple('1'), (1,))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            str_to_tuple('1, 2, 3, a, 5')

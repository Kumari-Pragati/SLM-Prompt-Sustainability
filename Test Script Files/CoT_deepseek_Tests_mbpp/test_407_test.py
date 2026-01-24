import unittest
from mbpp_407_code import rearrange_bigger

class TestRearrangeBigger(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rearrange_bigger(12345), 12435)

    def test_edge_case(self):
        self.assertEqual(rearrange_bigger(54321), False)

    def test_boundary_case(self):
        self.assertEqual(rearrange_bigger(11111), 11111)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rearrange_bigger('12345')

        with self.assertRaises(ValueError):
            rearrange_bigger(-12345)

        with self.assertRaises(TypeError):
            rearrange_bigger(123456789101112131415)

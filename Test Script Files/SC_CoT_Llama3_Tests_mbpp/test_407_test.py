import unittest
from mbpp_407_code import rearrange_bigger

class TestRearrangeBigger(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(rearrange_bigger(12345), 54321)

    def test_edge_case1(self):
        self.assertEqual(rearrange_bigger(11111), 11111)

    def test_edge_case2(self):
        self.assertEqual(rearrange_bigger(12321), 12321)

    def test_edge_case3(self):
        self.assertEqual(rearrange_bigger(55555), 55555)

    def test_edge_case4(self):
        self.assertEqual(rearrange_bigger(123456), 654321)

    def test_edge_case5(self):
        self.assertEqual(rearrange_bigger(1234567), 7654321)

    def test_edge_case6(self):
        self.assertEqual(rearrange_bigger(123456789), 987654321)

    def test_invalid_input1(self):
        self.assertFalse(rearrange_bigger('abc'))

    def test_invalid_input2(self):
        self.assertFalse(rearrange_bigger(None))

    def test_invalid_input3(self):
        self.assertFalse(rearrange_bigger(-12345))

    def test_invalid_input4(self):
        self.assertFalse(rearrange_bigger(12345.67))

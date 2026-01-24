import unittest
from mbpp_944_code import num_position

class TestNumPosition(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(num_position("Hello123World"), 4)

    def test_edge_case(self):
        self.assertEqual(num_position("123HelloWorld"), 0)

    def test_edge_case2(self):
        self.assertEqual(num_position("HelloWorld123"), 6)

    def test_edge_case3(self):
        self.assertEqual(num_position("123456"), 0)

    def test_edge_case4(self):
        self.assertEqual(num_position("Hello123World456"), 4)

    def test_edge_case5(self):
        self.assertEqual(num_position("HelloWorld"), -1)

    def test_edge_case6(self):
        self.assertEqual(num_position(""), -1)

    def test_edge_case7(self):
        self.assertEqual(num_position("HelloWorld123"), -1)

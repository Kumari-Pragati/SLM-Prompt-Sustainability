import unittest
from mbpp_305_code import start_withp

class TestStartWithp(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(start_withp(["Pete is a programmer"]), ('Pete', 'programmer'))

    def test_edge_case1(self):
        self.assertIsNone(start_withp(["Pete is a programmer", "Not a match"]))

    def test_edge_case2(self):
        self.assertIsNone(start_withp(["Not a match", "Pete is a programmer"]))

    def test_edge_case3(self):
        self.assertIsNone(start_withp(["Not a match", "Not a match"]))

    def test_error_case(self):
        with self.assertRaises(TypeError):
            start_withp(123)

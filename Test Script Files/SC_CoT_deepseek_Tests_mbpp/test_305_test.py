import unittest
from mbpp_305_code import start_withp

class TestStartsWithP(unittest.TestCase):

    def test_typical_case(self):
        words = ["Python programming is fun", "Panda is cute", "Penguin is cold"]
        self.assertEqual(start_withp(words), ('Python', 'Panda'))

    def test_edge_case(self):
        words = ["P"]
        self.assertEqual(start_withp(words), ('P',))

    def test_boundary_case(self):
        words = ["P", ""]
        self.assertIsNone(start_withp(words))

    def test_corner_case(self):
        words = ["PP", "P P"]
        self.assertEqual(start_withp(words), ('PP', 'P'))

    def test_invalid_input(self):
        words = ["123", "!@#"]
        self.assertIsNone(start_withp(words))

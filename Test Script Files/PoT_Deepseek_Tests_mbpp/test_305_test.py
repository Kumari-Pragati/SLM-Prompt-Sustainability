import unittest
from mbpp_305_code import start_withp

class TestStartsWithP(unittest.TestCase):

    def test_typical_case(self):
        words = ["Python programming is fun", "Panda is cute", "Penguin is cold"]
        self.assertEqual(start_withp(words), ('Python', 'Panda'))

    def test_edge_case(self):
        words = ["Programming is fun", "Panda is cute", "Penguin is cold"]
        self.assertIsNone(start_withp(words))

    def test_corner_case(self):
        words = ["", "Panda is cute", "Penguin is cold"]
        self.assertIsNone(start_withp(words))

    def test_invalid_input(self):
        words = ["Programming is fun", "Panda is cute", 123]
        with self.assertRaises(TypeError):
            start_withp(words)

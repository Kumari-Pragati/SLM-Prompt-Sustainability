import unittest
from mbpp_305_code import start_withp

class TestStartsWithP(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(start_withp(["Panda loves pizza", "Penguin is cool"]), None)

    def test_edge_conditions(self):
        self.assertEqual(start_withp(["P"]), None)
        self.assertEqual(start_withp(["Panda"]), None)
        self.assertEqual(start_withp(["Panda loves pizza", "Panda loves pizza"]), None)

    def test_complex_cases(self):
        self.assertEqual(start_withp(["Panda loves pizza", "Penguin is cool", "Penguin loves ice cream"]), None)
        self.assertEqual(start_withp(["Panda loves pizza", "Penguin is cool", "Penguin loves ice cream", "Penguin loves pizza"]), None)

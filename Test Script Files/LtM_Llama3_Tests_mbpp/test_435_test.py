import unittest
from mbpp_435_code import last_Digit

class TestLastDigit(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(last_Digit(10), 0)
        self.assertEqual(last_Digit(20), 0)
        self.assertEqual(last_Digit(30), 0)
        self.assertEqual(last_Digit(1), 1)
        self.assertEqual(last_Digit(2), 2)
        self.assertEqual(last_Digit(3), 3)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(last_Digit(0), 0)
        self.assertEqual(last_Digit(9), 9)
        self.assertEqual(last_Digit(-10), 0)
        self.assertEqual(last_Digit(-20), 0)
        self.assertEqual(last_Digit(100), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            last_Digit("a")
        with self.assertRaises(TypeError):
            last_Digit(None)

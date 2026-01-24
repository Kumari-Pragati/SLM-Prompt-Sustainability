import unittest
from mbpp_714_code import count_Fac

class TestCountFac(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(count_Fac(1), 0)
        self.assertEqual(count_Fac(2), 1)
        self.assertEqual(count_Fac(3), 2)
        self.assertEqual(count_Fac(4), 2)
        self.assertEqual(count_Fac(5), 3)
        self.assertEqual(count_Fac(6), 3)
        self.assertEqual(count_Fac(7), 4)
        self.assertEqual(count_Fac(8), 3)
        self.assertEqual(count_Fac(9), 4)
        self.assertEqual(count_Fac(10), 4)

    # Test for edge and boundary conditions
    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Fac(0), 0)
        self.assertEqual(count_Fac(1), 0)
        self.assertEqual(count_Fac(2), 1)
        self.assertEqual(count_Fac(100), 21)
        self.assertEqual(count_Fac(1000), 33)
        self.assertEqual(count_Fac(10000), 46)

    # Test for more complex or corner cases
    def test_more_complex_cases(self):
        self.assertEqual(count_Fac(17), 5)
        self.assertEqual(count_Fac(23), 6)
        self.assertEqual(count_Fac(31), 7)
        self.assertEqual(count_Fac(37), 8)
        self.assertEqual(count_Fac(43), 9)
        self.assertEqual(count_Fac(47), 10)
        self.assertEqual(count_Fac(53), 11)
        self.assertEqual(count_Fac(59), 12)
        self.assertEqual(count_Fac(67), 13)
        self.assertEqual(count_Fac(73), 14)

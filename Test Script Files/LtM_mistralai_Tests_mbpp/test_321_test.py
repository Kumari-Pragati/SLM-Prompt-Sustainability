import unittest
from mbpp_321_code import find_demlo

class TestFindDemlo(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(find_demlo("123"), "123321")
        self.assertEqual(find_demlo("0"), "0")
        self.assertEqual(find_demlo("987"), "9876789")

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_demlo(""), "")
        self.assertEqual(find_demlo("a"), "A123456789")
        self.assertEqual(find_demlo("1"), "1")
        self.assertEqual(find_demlo("10"), "109")
        self.assertEqual(find_demlo("123456789"), "987654321")

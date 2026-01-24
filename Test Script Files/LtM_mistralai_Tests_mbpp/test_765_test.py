import unittest
from mbpp_765_code import is_polite

class TestIsPolite(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(is_polite(1), 3)
        self.assertEqual(is_polite(2), 4)
        self.assertEqual(is_polite(10), 12)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(is_polite(0), 1)
        self.assertEqual(is_polite(math.inf), math.inf)
        self.assertEqual(is_polite(-1), math.ceil(math.log(-1, 2)))

    def test_complex_cases(self):
        self.assertEqual(is_polite(math.e), math.floor(math.e + math.log(math.e, 2)))
        self.assertEqual(is_polite(math.pi), math.floor(math.pi + math.log(math.pi, 2)))

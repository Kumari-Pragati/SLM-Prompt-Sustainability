import unittest
from mbpp_590_code import polar_rect

class TestPolarRect(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(polar_rect(1, 2), (complex(1, 2), complex(2, 3.14159265359)))
        self.assertEqual(polar_rect(-1, 2), (complex(-1, 2), complex(-2, 3.14159265359)))
        self.assertEqual(polar_rect(0, 0), (complex(0, 0), complex(0, 3.14159265359)))

    def test_edge_cases(self):
        self.assertEqual(polar_rect(0, 0), (complex(0, 0), complex(0, 3.14159265359)))
        self.assertEqual(polar_rect(1, 0), (complex(1, 0), complex(1, 0)))
        self.assertEqual(polar_rect(0, 1), (complex(0, 1), complex(0, 3.14159265359)))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            polar_rect('a', 2)
        with self.assertRaises(TypeError):
            polar_rect(1, 'b')

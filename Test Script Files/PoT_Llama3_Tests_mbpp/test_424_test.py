import unittest
from mbpp_424_code import extract_rear

class TestExtractRear(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(extract_rear((('a', 'b'), ('c', 'd'), ('e', 'f'))), ['f', 'd', 'b'])

    def test_edge(self):
        self.assertEqual(extract_rear(()), [])

    def test_edge2(self):
        self.assertEqual(extract_rear([('a', 'b')]), ['b'])

    def test_edge3(self):
        self.assertEqual(extract_rear([('a', 'b'), ('c', 'd')]), ['b', 'd'])

    def test_edge4(self):
        self.assertEqual(extract_rear([('a', 'b'), ('c', 'd'), ('e', 'f')]), ['f', 'd', 'b'])

    def test_invalid(self):
        with self.assertRaises(TypeError):
            extract_rear('not a tuple')

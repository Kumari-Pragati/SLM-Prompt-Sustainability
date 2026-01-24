import unittest
from mbpp_239_code import get_total_number_of_sequences

class TestGetTotalNumberOfSequences(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_total_number_of_sequences(3, 2), 6)
        self.assertEqual(get_total_number_of_sequences(4, 3), 20)
        self.assertEqual(get_total_number_of_sequences(5, 4), 40)

    def test_edge_cases(self):
        self.assertEqual(get_total_number_of_sequences(0, 1), 0)
        self.assertEqual(get_total_number_of_sequences(1, 0), 0)
        self.assertEqual(get_total_number_of_sequences(0, 0), 0)

    def test_boundary_conditions(self):
        self.assertEqual(get_total_number_of_sequences(1, 1), 1)
        self.assertEqual(get_total_number_of_sequences(2, 1), 2)
        self.assertEqual(get_total_number_of_sequences(3, 1), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_total_number_of_sequences("3", 2)
        with self.assertRaises(TypeError):
            get_total_number_of_sequences(3, "2")
        with self.assertRaises(TypeError):
            get_total_number_of_sequences("3", "2")
        with self.assertRaises(ValueError):
            get_total_number_of_sequences(-1, 2)
        with self.assertRaises(ValueError):
            get_total_number_of_sequences(3, -2)

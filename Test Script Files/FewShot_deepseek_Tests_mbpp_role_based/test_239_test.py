import unittest
from mbpp_239_code import get_total_number_of_sequences

class TestGetTotalNumberOfSequences(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(get_total_number_of_sequences(3, 2), 5)

    def test_boundary_conditions(self):
        self.assertEqual(get_total_number_of_sequences(0, 0), 0)
        self.assertEqual(get_total_number_of_sequences(1, 1), 1)
        self.assertEqual(get_total_number_of_sequences(2, 1), 2)

    def test_edge_conditions(self):
        self.assertEqual(get_total_number_of_sequences(2, 2), 0)
        self.assertEqual(get_total_number_of_sequences(3, 3), 0)

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

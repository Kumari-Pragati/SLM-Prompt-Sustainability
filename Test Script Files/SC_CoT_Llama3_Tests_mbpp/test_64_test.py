import unittest
from mbpp_64_code import subject_marks

class TestSubjectMarks(unittest.TestCase):

    def test_typical_input(self):
        subjectmarks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        result = subject_marks(subjectmarks)
        self.assertEqual(result, sorted(subjectmarks, key=lambda x: x[1]))

    def test_empty_input(self):
        subjectmarks = []
        result = subject_marks(subjectmarks)
        self.assertEqual(result, [])

    def test_single_element_input(self):
        subjectmarks = [('English', 88)]
        result = subject_marks(subjectmarks)
        self.assertEqual(result, subjectmarks)

    def test_multiple_elements_input(self):
        subjectmarks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82), ('History', 85)]
        result = subject_marks(subjectmarks)
        self.assertEqual(result, sorted(subjectmarks, key=lambda x: x[1]))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            subject_marks('Invalid Input')

    def test_invalid_input_structure(self):
        with self.assertRaises(TypeError):
            subject_marks([1, 2, 3])

    def test_invalid_input_length(self):
        with self.assertRaises(TypeError):
            subject_marks({'a': 1, 'b': 2})

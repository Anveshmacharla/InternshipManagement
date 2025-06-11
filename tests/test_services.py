import unittest
from app.services import validate_application

class TestApplicationValidation(unittest.TestCase):

    def test_valid_input(self):
        data = {
            'name': 'Alice',
            'age': '22',
            'domain': 'AI',
            'duration': '3'
        }
        valid, errors = validate_application(data)
        self.assertTrue(valid)
        self.assertEqual(errors, {})

    def test_missing_name(self):
        data = {
            'name': '',
            'age': '22',
            'domain': 'AI',
            'duration': '3'
        }
        valid, errors = validate_application(data)
        self.assertFalse(valid)
        self.assertIn('name', errors)

    def test_invalid_age(self):
        data = {
            'name': 'Bob',
            'age': '17',
            'domain': 'AI',
            'duration': '3'
        }
        valid, errors = validate_application(data)
        self.assertFalse(valid)
        self.assertIn('age', errors)

    def test_invalid_domain(self):
        data = {
            'name': 'Charlie',
            'age': '25',
            'domain': '',
            'duration': '3'
        }
        valid, errors = validate_application(data)
        self.assertFalse(valid)
        self.assertIn('domain', errors)

    def test_invalid_duration(self):
        data = {
            'name': 'Daisy',
            'age': '25',
            'domain': 'AI',
            'duration': '0'
        }
        valid, errors = validate_application(data)
        self.assertFalse(valid)
        self.assertIn('duration', errors)

if __name__ == '__main__':
    unittest.main()
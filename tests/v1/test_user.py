import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from app import create_app


class UserTestCase(unittest.TestCase):
    """User Test Case"""

    def setUp(self):
        """Initialize tes variables"""
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client
        self.user = {
            'id': 1,
            'user_name': 'User 1',
            'password': "test123",
            'user_type': 'Attendant'
        }

    def test_attendant_creation(self):
        """Test User Creation POST"""
        response = self.client().post('/users/', data=self.user)
        self.assertEqual(response.status_code, 201)
        self.assertIn('User 1', str(response.data))


if __name__ == '__main__':
    unittest.main()

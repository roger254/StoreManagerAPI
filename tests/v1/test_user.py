import json
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
            'user_name': 'testUser1',
            'password': "test1234"
        }

    def test_attendant_creation(self):
        """Test User Creation POST"""
        response = self.client().post('/users/register', data=self.user)
        self.assertEqual(response.status_code, 201)
        self.assertIn('User Registered', str(response.data))

    def test_user_already_registered(self):
        """Test User cannot register twice"""
        response = self.client().post('/users/register', data=self.user)
        self.assertEqual(response.status_code, 202)
        self.assertIn('User Exists. Please Log in!', str(response.data))

    def test_user_login(self):
        """Test user can log in"""
        result = self.client().post('/users/login', data=self.user)
        login_response = json.loads(result.data.decode())
        self.assertIn(str(login_response['message']), "You've logged in successfully.")
        self.assertEqual(result.status_code, 200)
        self.assertTrue(login_response['access_token'])

    def test_non_registered_user_login(self):
        """Test non registered users cannot login."""
        non_user = {
            'user_name': 'unknown',
            'password': '1234'
        }
        result = self.client().post('/users/login', data=non_user)
        response = json.loads(result.data.decode())
        self.assertEqual(result.status_code, 401)
        self.assertEqual(
            response['message'], "Invalid username or password, Please try again")


if __name__ == '__main__':
    unittest.main()

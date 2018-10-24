import os
import sys
import unittest

from flask import json

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from app import create_app


class SaleTestCase(unittest.TestCase):
    """Product Test Case"""

    def setUp(self):
        """Initialize tes variables"""
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client
        self.sale = {
            'id': 1,
            's_name': 'Test Sale 1',
            's_price': 50.5,
            's_quantity': 3,
            'sold_by': 'User 1'
        }

    def register_user(self, user_name="test user 1", password="test1234"):
        user_data = {
            'user_name': user_name,
            'password': password
        }
        return self.client().post('/users/register', data=user_data)

    def login_user(self, user_name="test user 1", password="test1234"):
        user_data = {
            'user_name': user_name,
            'password': password
        }
        return self.client().post('/users/login', data=user_data)

    def test_sale_creation(self):
        """Test creation with POST"""

        self.register_user()
        results = self.login_user()
        access_token = json.loads(results.data.decode())['access_token']

        response = self.client().post(
            '/sales/',
            headers=dict(Authorization="Bearer " + access_token),
            data=self.sale
        )
        self.assertEqual(response.status_code, 202)
        # TODO: fix this bug
        self.assertIn('Item', str(response.data))

    def test_get_all_sales(self):
        """Test can get all sales GET"""

        self.register_user()
        results = self.login_user()
        access_token = json.loads(results.data.decode())['access_token']

        response = self.client().post(
            '/sales/',
            headers=dict(Authorization="Bearer " + access_token),
            data=self.sale
        )
        self.assertEqual(response.status_code, 201)
        get_req = self.client().get(
            '/sales/',
            headers=dict(Authorization="Bearer " + access_token)
        )
        self.assertEqual(get_req.status_code, 201)
        self.assertIn('Sale 1', str(get_req.data))

    def test_get_specific_sales(self):
        """Test can get all sales GET"""

        self.register_user()
        results = self.login_user()
        access_token = json.loads(results.data.decode())['access_token']

        response = self.client().post(
            '/sales/',
            headers=dict(Authorization="Bearer " + access_token),
            data=self.sale
        )
        self.assertEqual(response.status_code, 202)
        get_req = self.client().get(
            '/sales/1',
            headers=dict(Authorization="Bearer " + access_token)
        )
        self.assertEqual(get_req.status_code, 200)
        self.assertIn('Sale 1', str(get_req.data))


if __name__ == '__main__':
    unittest.main()

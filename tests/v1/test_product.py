import os
import sys
import unittest

from flask import json

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from app import create_app


class ProductTestCase(unittest.TestCase):
    """Product Test Case"""

    def setUp(self):
        """Initialize tes variables"""
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client
        self.product = {
            'id': 1,
            'p_name': 'Product 1',
            'p_price': 50.5,
            'p_quantity': 34
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

    def test_product_creation(self):
        """Test creation with POST"""
        self.register_user()
        results = self.login_user()
        access_token = json.loads(results.data.decode())['access_token']

        response = self.client().post(
            '/products/',
            headers=dict(Authorization="Bearer " + access_token),
            data=self.product
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn('Product 1', str(response.data))

    def test_get_all_products(self):
        """Test can get all products GET"""

        self.register_user()
        results = self.login_user()
        access_token = json.loads(results.data.decode())['access_token']

        response = self.client().post(
            '/products/',
            headers=dict(Authorization="Bearer " + access_token),
            data=self.product
        )
        self.assertEqual(response.status_code, 201)
        get_req = self.client().get(
            '/products/',
            headers=dict(Authorization="Bearer " + access_token)
        )
        self.assertEqual(get_req.status_code, 200)
        self.assertIn('Product 1', str(get_req.data))

    def test_get_specific_item(self):
        """Test can get specific product GET <int: id>"""

        self.register_user()
        results = self.login_user()
        access_token = json.loads(results.data.decode())['access_token']

        response = self.client().post(
            '/products/',
            headers=dict(Authorization="Bearer " + access_token),
            data=self.product
        )
        self.assertEqual(response.status_code, 201)
        response_in_json = json.loads(response.data)
        get_req = self.client().get(
            '/products/1',
            headers=dict(Authorization="Bearer " + access_token),
        )
        self.assertEqual(get_req.status_code, 200)
        self.assertIn('Product 1', str(get_req.data))


if __name__ == '__main__':
    unittest.main()

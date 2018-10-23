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
            's_name': 'Sale 1',
            's_price': 50.5,
            's_quantity': 3,
            'sold_by': 'User 1'
        }

    def test_sale_creation(self):
        """Test creation with POST"""
        response = self.client().post('/sales/', data=self.sale)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Sale 1', str(response.data))

    def test_get_all_sales(self):
        """Test can get all sales GET"""
        response = self.client().post('/sales/', data=self.sale)
        self.assertEqual(response.status_code, 201)
        get_req = self.client().get('/sales/')
        self.assertEqual(get_req.status_code, 200)
        self.assertIn('Sale 1', str(get_req.data))

    def test_get_specific_sales(self):
        """Test can get all sales GET"""
        response = self.client().post('/sales/', data=self.sale)
        self.assertEqual(response.status_code, 201)
        response_in_json = json.loads(response.data)
        get_req = self.client().get('/sales/{}'.format(response_in_json['id']))
        self.assertEqual(get_req.status_code, 200)
        self.assertIn('Sale 1', str(get_req.data))


if __name__ == '__main__':
    unittest.main()

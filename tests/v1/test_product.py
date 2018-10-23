import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from app import create_app


class ProductTestCase(unittest.TestCase):
    """Product Test Case"""

    def setUp(self):
        """Initialize tes variables"""
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client
        self.product = {
            'p_name': 'Product 1',
            'p_price': 50.5,
            'p_quantity': 34
        }

    def test_product_creation(self):
        """Test creation with POST"""
        response = self.client().post('/products/', data=self.product)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Product 1', str(response.data))

    def test_get_all_products(self):
        """Test can get all products GET"""
        response = self.client().post('/products/', data=self.product)
        self.assertEqual(response.status_code, 201)
        get_req = self.client().get('/products/')
        self.assertEqual(get_req.status_code, 200)
        self.assertIn('Product 1', str(get_req.data))


if __name__ == '__main__':
    unittest.main()

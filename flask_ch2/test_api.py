from unittest import TestCase
import requests
import storemanager_api

class Test(TestCase):

	def setUp(self):
		self.app = storemanager_api.app.test_client() 

	def test_hello_world(self):
		response = self.app.get('/hello')
		self.assertEqual(response.status_code, 200)
	
	def test_get_all_products(self):
		response = self.app.get('/api/v1/all_products')
		self.assertEqual(response.status_code, 200)

	def test_attendants(self):
		response = self.app.get('/api/v1/attendants')
		self.assertEqual(response.status_code, 200)

	def test_sale_order(self):
		response = self.app.get('/api/v1/g/sale_order/')
		self.assertEqual(response.status_code, 200)

	def test_get_one_products(self):
		response = self.app.get('/api/v1/one_product/1')
		self.assertEqual(response.status_code, 200)

	def test_delete_one_attendants(self):
		response = self.app.delete('/api/v1/del_one_attendant/1')
		self.assertEqual(response.status_code, 200)

	def test_delete_one_product(self):
		response = self.app.delete('/api/v1/del_one_product/1')
		self.assertEqual(response.status_code, 200)
	

	

    
        


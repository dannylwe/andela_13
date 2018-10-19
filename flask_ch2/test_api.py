from unittest import TestCase
import requests

class Test(TestCase):

	def test_sanity(self):
		response = requests.get('http://localhost:5000/hello')
		self.assertEqual(response.status_code, 200)

	def test_sanity_1(self):
		response = requests.get('http://localhost:5000/hello')
		self.assertEqual(response.ok, True)

	def test_get_all_products(self):
		response = requests.get('http://localhost:5000/api/v1/all_products')
		self.assertEqual(response.ok, True)

	def test_attendants(self):
		response = requests.get('http://localhost:5000/api/v1/attendants')
		self.assertEqual(response.ok, True)

	def test_sale_order(self):
		response = requests.get('http://localhost:5000/api/v1/g/sale_order/')
		self.assertEqual(response.ok, True)

	def test_get_one_products(self):
		response = requests.get('http://localhost:5000/api/v1/one_product/1')
		self.assertEqual(response.ok, True)

	def test_delete_one_attendants(self):
		response = requests.delete('http://localhost:5000/api/v1/del_one_attendant/1')
		self.assertEqual(response.ok, True)

	def test_delete_one_product(self):
		response = requests.delete('http://localhost:5000/api/v1/del_one_product/1')
		self.assertEqual(response.ok, True)


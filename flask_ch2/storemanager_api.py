from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.1', title='Store Manager Api', 
	description='An Api that supplies data to the store manager app')

base_url= "/api/v1"

attendant = [
	{
	"id": 1,
	"name": "Tony Stark",
	"email": "tony@gmail.com",
	"password": "iamironman",
	"contact": "1800-TONY-STARK",
	},

	{
	"id": 2,
	"name": "Peter Parker",
	"email": "peter@gmail.com",
	"password": "auntmay",
	"contact": "0758123456",
	},

	{
	"id": 3,
	"name": "Hulk",
	"email": "hulk@gmail.com",
	"password": "banner",
	"contact": None,
	},
]

products = [
	{
	"id": 0, "name": None, "quantity": None
	},

	{
	"id": 1, "name": "Kitchen towels", "quantity": 15, "price": 4000
	},

	{
	"id": 2, "name": "blue band", "quantity": 5, "price": 1000
	},
]

"""should use OOP to create these"""

sale_order = [
	{
	"order_id": 123456,
	"name": ['Kitchen towels', 'blue band'],
	"quantity": 3,
	"price": 6000,
	"attendant": "Tony Stark",
	"attendant_id": 1,
	"category": "Households"
	},
]

#Products.append(products)

"""for i in attendant:
	print(i['id'])
"""
#print(products[0])

a_product = api.model('product', {
	"id": fields.Integer('Id of item'),
	"name": fields.String('name of product'), 
	"quantity": fields.Integer('Number of products'),
	"price": fields.Integer('Retail price'),
	})

a_sale_order = api.model('sale_order', {
	"order_id": fields.Integer('Unique order Id'),
	"name": fields.String('Name of product(s)'),
	"quantity": fields.Integer('Numerical quantity of products'),
	"price": fields.Integer('Cumulative price'),
	"attendant": fields.String('Name of attendant'),
	"attendant_id": fields.String('Unique Id of attendant'),
	"category": fields.String('category of product if any'),
	})

@api.route('/hello')
class HelloWorld(Resource):

    def get(self):
    	"sanity check"

        return {'hello': 'world'}

@api.route(base_url + '/attendants')
class get_attendants(Resource):

	def get(self):
		"Get all records of attendants"

		return {"attendants": attendant}

@api.response(204, 'successfully deleted.')
@api.route(base_url + '/del_one_attendant/<int:id>')
class delete_attendant(Resource):

	def delete(self, id):
		"Delete one attendant by Id"

		attendant.pop(id)

		return {"attendant": attendant}

@api.route(base_url + '/all_products')
class All_products(Resource):
	@api.doc('Method that returns all products')
	def get(self):
		"Get all products"

		return {"products": products}

@api.route(base_url + '/one_product/<int:id>')
class One_product(Resource):

	def get(self, id):
		"Get one product by Id"

		return {"product": products[id]}

@api.response(204, 'successfully deleted.')
@api.route(base_url + '/del_one_product/<int:id>')
class Del_product(Resource):

	def delete(self, id):
		"Delete one product by Id"

		products.pop(id)
		return {"products": products}

@api.expect(a_product)
@api.route(base_url + '/add_product/')
class post_product(Resource):

	def post(self):
		"Add a single product"

		new_product = api.payload
		products.append(new_product)
		return {"successfully added product": new_product}, 201


@api.route(base_url + '/g/sale_order/')
class Sale_order(Resource):

	def get(self):
		"Get all records of sale orders"

		return {"sale_orders": sale_order}

@api.route(base_url + '/sale_order')	
@api.expect(a_sale_order)
class Sale_order_post(Resource):
	def post(self):
		"Post a sale order"

		new_sale_order = api.payload
		sale_order.append(new_sale_order)
		return {"successfully added new sale order": new_sale_order}, 201
	
if __name__ == '__main__':
    app.run(debug=True)
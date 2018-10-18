from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Store Manager Api', 
	description='An Api that supplies data to the store manager app')

base_url= "/api/v1"

attendant = [

	{
	"id": 1,
	"name": "Tony Story",
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
	}
]

Products= {}
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

#Products.append(products)

"""for i in attendant:
	print(i['id'])
"""
#print(products[0])

a_product = api.model('product', {
	"id": fields.Integer('Id of item'),
	"name": fields.String('name of product'), 
	"quantity": fields.Integer('Number of products'),
	"price": fields.Integer('Retail')
	})

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@api.route(base_url + '/all_products')
class All_products(Resource):
	@api.doc('Method that returns all products')
	def get(self):
		return {"products": products}

@api.route(base_url + '/one_product/<int:id>')
class One_product(Resource):
	def get(self, id):
		return {"product": products[id]}

@api.response(204, 'successfully deleted.')
@api.route(base_url + '/del_one_product/<int:id>')
class Del_product(Resource):
	def delete(self, id):
		products.pop(id)
		return {"products": products}


@api.expect(a_product)
@api.route(base_url + '/add_product/')
class post_product(Resource):
	
	def post(self):
		new_product = api.payload
		products.append(new_product)
		return {"successfully added product": new_product}, 201

if __name__ == '__main__':
    app.run(debug=True)
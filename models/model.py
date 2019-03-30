from pymongo import MongoClient

client = MongoClient()
db = client['mini_amazon']

def user_exists(username):

	query = {'username' : username}
	result = db['users'].find(query)

	if result.count() > 0 :
		return True
	return False

def create_user(user_info):
	db['users'].insert_one(user_info)


def login_user(username):
	query = {'username':username}
	result = db['users'].find_one(query)
	return result

def add_product(product):
	db['products'].insert_one(product)

def product_exists(product_name):
	query = {'name':product_name}
	result = db['products'].find(query)

	if result.count() > 0:
		return True
	return False

def buyer_products():
	result = db['products'].find({})
	return result

def seller_products(username):
	result = db['products'].find({'seller':username})
	return result

def add_to_cart(product_id,username):
	db['users'].update({'username':username},{"$addToSet":{"cart":{"$each":[product_id]}}})
	

# db.inventory.update(
#    { _id: 2 },
#    { $addToSet: { tags: { $each: [ "camera", "electronics", "accessories" ] } } }
#  )
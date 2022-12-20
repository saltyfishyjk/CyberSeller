# 用于计算商品推荐商品排序
class GoodGoodClass(object):
	def __init__(self, id, name, price, seller_id, maker, picture, description, date, shelf_life, value):
		self.id = id
		self.name = name
		self.price = price
		self.seller_id = seller_id
		self.maker = maker
		self.picture = picture
		self.description = description
		self.date = date
		self.shelf_life = shelf_life
		self.value = value
	def __lt__(self, other):
		return self.value > other.value

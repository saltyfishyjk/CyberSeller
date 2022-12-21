# 用于计算用户推荐商品排序
class UserGoodClass(object):
	# id为编号，like为是否收藏，num为购物车中数量（没有加入购物车即为0）
	def __init__(self, id, name, price, seller_id, maker, picture, description, date, shelf_life, like, num):
		self.id = id
		self.name = name
		self.price = price
		self.seller_id = seller_id
		self.maker = maker
		self.picture = picture
		self.description = description
		self.date = date
		self.shelf_life = shelf_life
		self.like = like
		self.num = num
		self.value = 5 * self.num + 3 * like
		# print('name : ' + self.name + ' value : ' + str(self.value))

	def __lt__(self, other):
		return self.value > other.value

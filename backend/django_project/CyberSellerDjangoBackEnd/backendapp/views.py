import json
import os.path

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from backendapp.models import Account, Good, ShopCart, Star
from django.views.decorators.csrf import csrf_exempt  # 用于忽略scrf攻击
from CyberSellerDjangoBackEnd.settings import IMG_UPLOAD

# 合法身份identity列表
legal_identity = ["admin", "customer", "seller"]

# Create your views here.
def index(request):
	return HttpResponse("Hello!<br/>Welcome to CyberSeller!\n")

test_signup = False
test_json = False

@csrf_exempt
def signup(request):
	# response = HttpResponse()  # 返回HttpResponse对象
	response = {}
	if (request.method == 'POST'):
		if test_signup:
			# return HttpResponse(request.body)
			receive_data = json.loads(request.body)
			ret_name = receive_data['name']
			ret_password = receive_data['password']
			ret_identity = receive_data['identity']
			return HttpResponse("name : " + ret_name + "\npassword:" + ret_password + "\nidentity:" + ret_identity)
		receive_data = json.loads(request.body)  # 解析传入的HttpRequest对象
		if test_json:
			print("ARRIVE HERE")
		name = receive_data['name']  # 注册用户名
		password = receive_data['password']  # 注册密码
		identity = receive_data['identity']  # 注册身份
		if test_json:
			print("name : " + name)
			print("password : " + password)
			print("identity : " + identity)
		if name is None or password is None or identity is None or len(name) == 0 or len(password) == 0:
			response['succeed'] = False
			response['code'] = "010000"  # 空用户名/密码/身份
			response['message'] = "ERROR! Empty name, password or identity, make sure they are legal"
			response['id'] = -1
		if len(name) > 64:
			response['succeed'] = False
			response['code'] = "010002"  # 用户名过长
			response['message'] = "ERROR! Too long name, make sure len <= 64"
			response['id'] = -1
		elif len(password) > 64:
			response['succeed'] = False
			response['code'] = "010003"  # 密码过长
			response['message'] = "ERROR! Too long password, make sure len <= 64"
			response['id'] = -1
		else:
			if identity not in legal_identity:
				response['succeed'] = False
				response['code'] = "010004"  # 非法身份
				response['message'] = "ERROR! Illegal identity, make sure identity is admin, customer or seller"
				response['id'] = -1
			else:
				if test_json:
					print("ARRIVE HERE 2 ")
				accounts = Account.objects.all()  # Account对象列表，每一个元素是一个Account对象
				flag = True  # 标记用户名是否合法（不重名）
				for account in accounts:
					if name == account.name:
						flag = False
						break
				if not flag:
					response['succeed'] = False
					response['code'] = "010005"  # 重名用户名
					response['message'] = "ERROR! This name has been signed up, please choose another name"
					response['id'] = -1
				else:
					if test_json:
						print("ARRIVE HERE 3 ")
					account_new = Account(name=name, password=password, identity=identity, balance=0)  # 生成新的用户行
					account_new.save()  # 保存到数据库
					if test_json:
						print("ARRIVE HERE 4 ")
					account_id = Account.objects.get(name=name).id
					response['succeed'] = True
					response['code'] = "010101"  # 注册成功
					response['message'] = "SUCCESS! Sign up successfully"
					response['id'] = account_id
	else:
		response['succeed'] = False  # 表明请求失败
		response['code'] = "010001"  # 01代表signup方法，00代表错误，01代表错误类型
		response['message'] = "ERROR! This URL accepts POST ONLY!"  # 错误提示信息
		response['id'] = -1  # 用非法id -1 表征当前为错误情况
		# return HttpResponse("ERROR! This URL accepts POST ONLY!")
	# return response
	return JsonResponse({
		'succeed': response['succeed'],
		'code': response['code'],
		'message': response['message'],
		'id': response['id']
	})

try_cross = False
@csrf_exempt
def login(request):
	# response = HttpResponse()
	response = {}
	if request.method == "POST":
		if (try_cross) :
			return JsonResponse({'errno': 0, 'msg': "试验成功!"})
		receive_data = json.loads(request.body)  # 解析传入的HttpRequest对象
		name = receive_data['name']
		password = receive_data['password']
		if name is None or password is None or len(name) == 0 or len(password) == 0:
			response['succeed'] = False
			response['code'] = "020001"
			response['message'] = "ERROR! Empty name or password, make sure they are legal"
			response['id'] = -1
			response['balance'] = -1
			response['identity'] = "FAIL"
		else:
			account = Account.objects.get(name=name)
			if account is None:
				response['succeed'] = False
				response['code'] = "020002"
				response['message'] = "ERROR! Non-exist name, make sure the name is correct"
				response['id'] = -1
				response['balance'] = -1
				response['identity'] = "FAIL"
			else:
				account_id = account.id
				account_identity = account.identity
				if password != account.password:
					response['succeed'] = False
					response['code'] = "020003"
					response['message'] = "ERROR! Wrong password, make sure the password is correct"
					response['id'] = account_id
					response['balance'] = -1
					response['identity'] = account_identity
				else:
					account_balance = account.balance
					response['succeed'] = True
					response['code'] = "020101"
					response['message'] = "SUCCESS! Log in successfully"
					response['id'] = account_id
					response['balance'] = account_balance
					response['identity'] = account_identity
	else:
		response['succeed'] = False
		response['code'] = "020000"
		response['message'] = "ERROR! This URL accepts POST ONLY!"
		response['id'] = -1
		response['balance'] = -1
		response['identity'] = "FAIL"
	return JsonResponse({
		'succeed': response['succeed'],
		'code': response['code'],
		'message': response['message'],
		'id': response['id'],
		'balance': response['balance'],
		'identity': response['identity']
	})
	# return response

testAddGoods = False
DEFAULT_MAKER = 'bank'
DEFAULT_DESCRIPTION = 'This is a nice product'
DEFAULT_DATE = '2022-12-19'
DEFAULT_SHELF_LIFE = '0010-11-12-13'
# 添加商品
@csrf_exempt
def addGoods(request):
	if request.method == 'POST':
		# 获取除了文件之外的数据
		data = request.POST
		# 商品名
		name = data.get('name')
		if name is None:
			return JsonResponse({
				'succeed': False,
				'code': '030000',
				'message': 'ERROR! Need available good name!'
			})
		# 价格
		price = data.get('price')
		if price is None:
			return JsonResponse({
				'succeed': False,
				'code': '030001',
				'message': 'ERROR! Need available good price!'
			})
		# 卖家ID
		seller_id = data.get('seller_id')
		if seller_id is None:
			return JsonResponse({
				'succeed': False,
				'code': '030002',
				'message': 'ERROR! Need available seller id'
			})
		# 制造商名称
		maker = data.get('maker')
		if maker is None:
			maker = DEFAULT_MAKER
		# 商品描述
		description = data.get('description')
		if description is None:
			description = DEFAULT_DESCRIPTION
		# 生产日期
		date = data.get('date')
		if date is None:
			date = DEFAULT_DATE
		# 保质期
		shelf_life = data.get('shelfLife')
		if shelf_life is None:
			shelf_life = DEFAULT_SHELF_LIFE
		# 获取图片文件
		pic_file = request.FILES.get('picture')
		test_non_file = False
		if test_non_file:
			pic_file = data.get('picture')
			print('picfile : ' + str(pic_file) + ' type : ' + str(type(pic_file)))
		print('picfile : ' + str(pic_file) + ' type : ' + str(type(pic_file)))
		if pic_file is None:
			return JsonResponse({
				'succeed': False,
				'code': '030003',
				'message': 'ERROR! Need available pic file'
			})
		# 获取文件全名
		pic_name = pic_file.name
		# 获取文件名
		mobile = os.path.splitext(pic_name)[0]
		# 获取文件后缀
		ext = os.path.splitext(pic_name)[1]
		# 重定义文件名
		pic_name = f'avatar-{mobile}{ext}'
		# 从配置文件中加载图片保存路径
		pic_path = os.path.join(IMG_UPLOAD, pic_name)
		# 保存文件
		print('arrive here')
		with open(pic_path, 'wb') as fp:
			fp.write(pic_file.read())
		# 获取图片URL
		pic_url = 'http://43.143.179.158:8080/img/' + pic_name
		print('price : ' + str(price) + str(type(price)))
		good = Good(name=name, price=price, seller_id=seller_id,
					maker=maker, picture=pic_url, description=description,
					date=date, shelf_life=shelf_life)
		good.save()
		return JsonResponse({
			'succeed': True,
			'code': '030101',
			'message': 'SUCCESS! Add a good successfully!'
		})

# 添加商品到购物车
@csrf_exempt
def updateShopCart(request):
	if request.method == 'POST':
		data = request.POST
		user_id = data.get('user_id')
		if user_id is None:
			return JsonResponse({
				'succeed': False,
				'code': '040000',
				'message': 'ERROR! Need available user_id!'
			})
		good_id = data.get('good_id')
		if good_id is None:
			return JsonResponse({
				'succeed': False,
				'code': '040001',
				'message': 'ERROR! Need available good_id!'
			})
		new_num = data.get('new_num')
		if new_num is None:
			return JsonResponse({
				'succeed': False,
				'code': '040002',
				'message': 'ERROR! Need available new_num!'
			})
		shop_cart_ele = ShopCart.objects.filter(user_id=int(user_id), good_id=int(good_id))
		# print("arrive here")
		# print("shop cart ele type : " + str(type(shop_cart_ele)))
		if shop_cart_ele.count() == 0:
			shop_cart_ele = ShopCart(user_id=user_id, good_id=good_id, num=new_num)
		else:
			shop_cart_ele.num = new_num
			shop_cart_ele = ShopCart.objects.get(user_id=user_id, good_id=good_id)
		shop_cart_ele.save()
		return JsonResponse({
			'succeed': True,
			'code': '040101',
			'message': 'SUCCESS! Update ShopCart successfully!'
		})


def getRecommandGoods(user_id):
	# TODO : 待完善
	ret_list = []
	goods = Good.objects.all()
	cnt = 0
	for good in goods:
		ret_list.append(good)
	return goods

# 获取对用户的个性推荐
@csrf_exempt
def mainRecommendGoods(request):
	if request.method == 'POST':
		# 获取用户名
		id = request.POST.get('user_id')
		print("arrive here 1")
		if id is None:
			return JsonResponse({
				'succeed': False,
				'code': '050000',
				'message': 'ERROR! Need non-null userid!'
			})
		user = Account.objects.get(id=id)
		print("arrive here 2")
		if user is None:
			return JsonResponse({
				'succeed': False,
				'code': '050001',
				'message': 'ERROR! Need available userid!'
			})
		# goods = Good.objects.all()
		goods = getRecommandGoods(id)
		n = goods.count()
		ret_json = {'succeed': True,
					'code': '050101',
					'message': 'SUCCESS! Get goods recommended successfully!',
					'n': n}
		goods_json = []
		for good in goods:
			like = 0
			stars = Star.objects.filter(user_id=id, good_id=good.id)
			if stars.count() == 1:
				star = Star.objects.get(user_id=id, good_id=good.id)
				like = star.like
			good_json = {
				'id': good.id,
				'name': good.name,
				'price': good.price,
				'seller_id': good.seller_id,
				'seller_name': Account.objects.get(id=good.seller_id).name,
				'maker': good.maker,
				'picture': good.picture,
				'description': good.description,
				'date': good.date,
				'shelf_life': good.shelf_life,
				'like': like
			}
			goods_json.append(good_json)
		ret_json['goods'] = goods_json
		return JsonResponse(ret_json)

@csrf_exempt
def getGood(request):
	if request.method == 'POST':
		good_id = request.POST.get('good_id')
		good = Good.objects.get(id=good_id)
		return JsonResponse({
			'id': good.id,
			'name': good.name,
			'price': good.price,
			'seller_id': good.seller_id,
			'maker': good.maker,
			'picture': good.picture,
			'description': good.description,
			'date': good.date,
			'shelf_life': good.shelf_life
		})

@csrf_exempt
def searchShopCart(request):
	if request.method == 'POST':
		user_id = request.POST.get('user_id')
		user = Account.objects.get(id=user_id)
		goods = ShopCart.objects.filter(user_id=user_id)
		n = goods.count()
		goods_list = []
		for good_index in goods:
			good_id = good_index.good_id
			good = Good.objects.get(id=good_id)
			goods_list.append({
				'id': good.id,
				'name': good.name,
				'price': good.price,
				'seller_id': good.seller_id,
				'maker': good.maker,
				'picture': good.picture,
				'description': good.description,
				'date': good.date,
				'shelf_life': good.shelf_life,
				'num': good_index.num
			})
		return JsonResponse({
			'n': n,
			'goods': goods_list
		})

@csrf_exempt
def updateStar(request):
	if request.method == 'POST':
		user_id = request.POST.get('user_id')
		good_id = request.POST.get('good_id')
		like = request.POST.get('like')
		if user_id is None:
			return JsonResponse({
				'succeed': False,
				'code': '080000',
				'message': 'ERROR! Need available user_id!'
			})
		if good_id is None:
			return JsonResponse({
				'succeed': False,
				'code': '080001',
				'message': 'ERROR! Need available good_id!'
			})
		if like is None:
			return JsonResponse({
				'succeed': False,
				'code': '080002',
				'message': 'ERROR! Need available like!'
			})
	stars = Star.objects.filter(user_id=user_id, good_id=good_id)
	if stars.count() == 0:
		star = Star(user_id=user_id, good_id=good_id)
		star.like = like
		star.save()
	else:
		star = Star.objects.get(user_id=user_id, good_id=good_id)
		star.like = like
		star.save()
	return JsonResponse({
		'succeed': True,
		'code': '080101',
		'message': 'SUCCESS! Star a good successfully!'
	})

@csrf_exempt
def getSixPictures(request):
	if request.method == 'POST':
		user_id = request.POST.get('user_id')
		if user_id is None:
			return JsonResponse({
				'succeed': False,
				'code': '090000',
				'message': 'ERROR! Need available user_id!'
			})
		print('user_id : ' + str(user_id))
		goods = getRecommandGoods(user_id)
		n = 6
		pictures = []
		# print('goods : ' + goods)
		#for i in range(0, 6):
			#print("id : " + goods[i].id)
			#pictures.append(Good.objects.get(id=goods[i].id).picture)
		cnt = 0
		for good in goods:
			pictures.append(good.picture)
			if cnt >= 6:
				break
		return JsonResponse({
			'succeed': True,
			'code': '090101',
			'message': 'SUCCESS! Got 6 head pictures',
			'n': n,
			'pictures': pictures
		})

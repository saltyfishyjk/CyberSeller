import json
import os.path

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from backendapp.models import Account, Good, ShopCart
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
		with open(pic_path, 'wb+') as fp:
			fp.write(pic_file.read())
		# 获取图片URL
		pic_url = 'http://43.143.179.158:8080/img/' + pic_name
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
		shop_cart_ele = ShopCart.objects.get(user_id=user_id, good_id=good_id)
		print("arrive here")
		if shop_cart_ele is None:
			shop_cart_ele = ShopCart(user_id=user_id, good_id=good_id, num=new_num)
		else:
			shop_cart_ele.num = new_num
		shop_cart_ele.save()
		return JsonResponse({
			'succeed': True,
			'code': '040101',
			'message': 'SUCCESS! Update ShopCart successfully!'
		})


# 获取对用户的个性推荐
@csrf_exempt
def mainRecommendGoods(request):
	if request.method == 'POST':
		# 获取用户名
		id = request.POST.get('id')
		if id is None:
			return JsonResponse({
				'succeed': False,
				'code': '050000',
				'message': 'ERROR! Need non-null userid!'
			})
		user = Account.objects.get(id=id)
		if user is None:
			return JsonResponse({
				'succeed': False,
				'code': '050001',
				'message': 'ERROR! Need available userid!'
			})
		goods = Good.objects.all()
		n = goods.count()
		ret_json = {'succeed': True,
					'code': '050101',
					'message': 'SUCCESS! Get goods recommended successfully!',
					'n': n}
		goods_json = []
		for good in goods:
			good_json = {
				'id': good.id,
				'name': good.name,
				'price': good.price,
				'seller_id': good.seller_id,
				'maker': good.maker,
				'picture': good.picture,
				'description': good.description,
				'date': good.date,
				'shelf_life': good.shelf_life
			}
			goods_json.append(good_json)
		ret_json['goods'] = goods_json
		return JsonResponse(ret_json)
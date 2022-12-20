import json
import os.path

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from backendapp.models import Account
from backendapp.models import Good
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
		'succeed': response['response'],
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
@csrf_exempt
def addGoods(request):
	if request.method == 'POST':
		# 获取除了文件之外的数据
		data = request.POST
		# 商品名
		name = data.get('name')
		# 价格
		price = data.get('price')
		# 卖家ID
		seller_id = data.get('sellerId')
		# 制造商名称
		maker = data.get('maker')
		# 商品描述
		description = data.get('description')
		# 生产日期
		date = data.get('date')
		# 保质期
		shelfLife = data.get('shelfLife')
		# 获取图片文件
		pic_file = request.FILES.get('picture')
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
		print('pic_url : ' + pic_url)
		return JsonResponse({
			'message': 'success'
		})
		if testAddGoods:
			# 获取除了文件之外的数据
			data = request.POST
			name = data.get('name')
			print("name = " + str(name) + " name type : " + str(type(name)))
			price = data.get('price')
			print("price = " + str(price) + " price type : " + str(type(price)))
			seller = data.get('seller')
			print('seller = ' + str(seller) + ' seller type : ' + str(type(seller)))
			maker = data.get('maker')
			print('maker = ' + str(maker) + ' maker type : ' + str(type(maker)))
			# pic_file = request.FILES.get('picture')
			# 获取图片文件列表
			pic_files = request.FILES.getlist('picture')
			for pic_file in pic_files:
				# 获取文件全名
				pic_name = pic_file.name
				print("pic_name : " + str(pic_name))
				# 获取文件名
				mobile = os.path.splitext(pic_name)[0]
				print('mobile : ' + str(mobile))
				# 获取文件后缀
				ext = os.path.splitext(pic_name)[1]
				print('ext : ' + str(ext))
				# 重定义文件名
				pic_name = f'avatar-{mobile}{ext}'
				print('pic_name : ' + pic_name)
				# 从配置文件中加载图片保存路径
				pic_path = os.path.join(IMG_UPLOAD, pic_name)
				print('pic_path : ' + str(pic_path))
				# 保存文件
				with open(pic_path, 'wb+') as fp:
					fp.write(pic_file.read())
					# for chunk in pic_file.chunks():
						# fp.write(chunk)
				# print('picture file = ' + str(pic_file) + ' type : ' + str(type))
			return JsonResponse({
				'message': 'success'
			})
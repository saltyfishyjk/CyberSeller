from django.db import models

# Create your models here.

# 账户表
class Account(models.Model):
	id = models.AutoField(primary_key=True)  # 账户ID，由数据库自动分配并自增
	name = models.CharField(max_length=128)  # 用户名
	password = models.CharField(max_length=128)  # 密码，为了效果展示使用明文存储
	identity = models.CharField(max_length=128)  # 身份，区分不同权限用户
	balance = models.DecimalField(max_digits=20, decimal_places=6)  # 余额，精确到小数点后6位

# 商品表
class Good(models.Model):
	id = models.AutoField(primary_key=True)  # 商品ID，由数据库自动分配并自增
	name = models.CharField(max_length=128)  # 商品名称
	price = models.DecimalField(max_digits=20, decimal_places=2)  # 价格，精确到小数点后2位
	seller_id = models.IntegerField()  # 卖家ID，对应Account的id
	maker = models.CharField(max_length=128)  # 制造商名称
	picture = models.CharField(max_length=1024)  # 商品图片url
	description = models.CharField(max_length=1024)  # 商品描述
	date = models.CharField(max_length=128)  # 生产日期，形如yyyy-mm-dd
	shelf_life = models.CharField(max_length=128)  # 保质期，形如yyyy-mm-dd-hh

# 购物车表
class ShopCart(models.Model):
	id = models.AutoField(primary_key=True)  # 购物车元组ID，由数据库自动分配并自增
	user_id = models.IntegerField()  # 用户ID，和Account相对应
	good_id = models.IntegerField()  # 商品ID，和Good相对应
	num = models.IntegerField()  # 购物车内商品数量

# 收藏表
class Star(models.Model):
	id = models.AutoField(primary_key=True)  # 收藏元组ID，由数据库自动分配并自增
	user_id = models.IntegerField()  # 用户ID，和Account相对应
	good_id = models.IntegerField()  # 商品ID，和Good相对应
	like = models.IntegerField()  # 是否收藏，为1表示收藏，为0表示不收藏

# 库存表
class Repo(models.Model):
	id = models.AutoField(primary_key=True)  # 库存元组ID，由数据库自动分配并自增
	good_id = models.IntegerField()  # 商品ID，和Good相对应
	repo = models.IntegerField()  # 库存，为整数

# 地址表
class Address(models.Model):
	id = models.AutoField(primary_key=True)  # 地址元组ID，由数据库自动分配
	user_id = models.IntegerField()  # 用户ID，和Account相对应
	receiver_name = models.CharField(max_length=128)  # 收件人姓名，字符串
	phone = models.CharField(max_length=128)  # 收件人电话号码，字符串
	addr = models.CharField(max_length=256)  # 地址
	detailed_addr = models.CharField(max_length=1024)  # 详细地址
	comment = models.CharField(max_length=1024)  # 备注
	default = models.IntegerField()  # 整数，为1表示是默认地址，为0表示不是默认地址

# 订单表
class Sale(models.Model):
	id = models.AutoField(primary_key=True)  # 订单元组ID，由数据库自动分配
	user_id = models.IntegerField()  # 用户ID，和Account相对应
	address_id = models.IntegerField()  # 地址ID，和Address相对应
	price = models.IntegerField()  # 订单总价
	date = models.DateTimeField(auto_now=True)  # 由Django自动生成时间戳

# 订单商品表
class SaleGood(models.Model):
	id = models.AutoField(primary_key=True)  # 订单商品元组ID，由数据库自动分配
	sale_id = models.IntegerField()  # 订单ID，和Sale相对应
	good_id = models.IntegerField()  # 商品ID，和Good相对应
	num = models.IntegerField()  # 订单中该商品数量

# 商品详情表
class GoodDetail(models.Model):
	id = models.AutoField(primary_key=True)  # 商品详情元组ID，由数据库自动
	good_id = models.IntegerField()  # 商品ID，和Good相对应
	key = models.CharField(max_length=128)  # 字符串，键值
	value = models.CharField(max_length=128)  # 字符串，值

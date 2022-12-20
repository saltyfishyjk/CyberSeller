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

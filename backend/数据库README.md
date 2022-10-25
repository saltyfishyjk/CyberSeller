# 数据库README

> 绝大多数时候，前端开发人员**不需要**查阅本文件，通过URL API接口文档应当获得足够前端需要的信息；本文件更多是为后端开发者服务

## 数据库基本信息

| 属性     | 值               |
| -------- | ---------------- |
| Host     | 43.143.179.158   |
| Port     | 3306             |
| 数据库名 | CyberSeller_db1  |
| User     | root             |
| password | CyberSeller2022! |

> 上述用户名和密码是root权限，请谨慎操作！
>
> 如果忘记退出mysql就关闭服务器，会出现下一次无法登录mysql的错误，可以参考[这篇文章](https://blog.csdn.net/weixin_41004763/article/details/100139802)中的指令修复。

### 进入数据库

首先，你需要通过xshell等终端登入CyberSeller的Ubuntu服务器。

进入`root`账号：

```bash
mysql -uroot -p
`enter password`
```

## 表

### Account账户表

```python
class Account(models.Model):
	id = models.AutoField(primary_key=True)  # 账户ID，由数据库自动分配并自增
	name = models.CharField(max_length=128)  # 用户名
	password = models.CharField(max_length=128)  # 密码，为了效果展示使用明文存储
	identity = models.CharField(max_length=128)  # 身份，区分不同权限用户
	balance = models.DecimalField(max_digits=20, decimal_places=6)  # 余额，精确到小数点后6位
```

| 列       | 性质                         | 说明                                                         |
| -------- | ---------------------------- | ------------------------------------------------------------ |
| id       | autofield + primarykey + Int | 自增自动分配主键，是用户的唯一标识                           |
| name     | charfield                    | 用户名，字符串                                               |
| password | charfield                    | 明文存储的用户密码，字符串                                   |
| identity | charfield                    | 用户类别，有`admin, customer, seller`三种，**不能**出现其他值 |
| balance  | decimalfield                 | 用户余额，精确小数，至多14位整数+6位小数                     |

TODO : 应当设计**检查**，用于排查非法的identity插入


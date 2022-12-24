## 系统实现报告

##### `yjk`

### Part 1 实现环境

| 环境   | 版本  |
| ------ | ----- |
| Ubuntu | 20.04 |
| Python | 3.9.7 |
| Django | 3.2   |
| MySQL  | 8.0   |

### Part 2 系统功能结构图

/* TODO */

### Part 3 基本表的定义，主外码等完整性约束定义，索引的定义

#### Account用户表

| 属性名   | 中文名 | 数据类型 | 备注 |
| -------- | ------ | -------- | ---- |
| id       | 编号   | INT      | 主码 |
| name     | 用户名 | VARCHAR  |      |
| password | 密码   | VARCHAR  |      |
| identity | 身份   | VARCHAR  |      |
| balance  | 余额   | DECIMAL  |      |

#### Good商品表

| 属性名      | 中文名   | 数据类型 | 备注        |
| ----------- | -------- | -------- | ----------- |
| id          | 编号     | INT      | 主码        |
| name        | 商品名   | VARCHAR  |             |
| price       | 价格     | DECIMAL  |             |
| seller_id   | 卖家编号 | INT      | 外键        |
| maker       | 制造商   | VARCHAR  |             |
| picture     | 图片地址 | VARCHAR  | 存储图片URL |
| description | 详细描述 | VARCHAR  |             |
| date        | 生产日期 | VARCHAR  |             |
| shelf_life  | 保质期   | VARCHAR  |             |

#### ShopCart购物车表

| 属性名  | 中文名           | 数据类型 | 备注 |
| ------- | ---------------- | -------- | ---- |
| id      | 编号             | INT      | 主码 |
| user_id | 用户编号         | INT      | 外键 |
| good_id | 商品编号         | INT      | 外键 |
| num     | 购物车内商品数量 | INT      |      |

#### Star收藏表

| 属性名  | 中文名   | 数据类型 | 备注 |
| ------- | -------- | -------- | ---- |
| id      | 编号     | INT      | 主码 |
| user_id | 用户编号 | INT      | 外键 |
| good_id | 商品编号 | INT      | 外键 |
| like    | 是否收藏 | INT      |      |

#### Repo库存表

| 属性名  | 中文名   | 数据类型 | 备注 |
| ------- | -------- | -------- | ---- |
| id      | 编号     | INT      | 主码 |
| user_id | 用户编号 | INT      | 外键 |
| good_id | 商品编号 | INT      | 外键 |
| like    | 是否收藏 | INT      |      |

#### Address地址表

| 属性名        | 中文名         | 数据类型 | 备注 |
| ------------- | -------------- | -------- | ---- |
| id            | 编号           | INT      | 主码 |
| user_id       | 用户编号       | INT      | 外键 |
| receiver_name | 收件人姓名     | VARCHAR  |      |
| phone         | 收件人电话     | VARCHAR  |      |
| addr          | 地址           | VARCHAR  |      |
| detailed_addr | 详细地址       | VARCHAR  |      |
| comment       | 备注           | VARCHAR  |      |
| default       | 是否为默认地址 | VARCHAR  |      |

#### Sale订单表

| 属性名     | 中文名   | 数据类型 | 备注 |
| ---------- | -------- | -------- | ---- |
| id         | 编号     | INT      | 主码 |
| user_id    | 用户编号 | INT      | 外键 |
| address_id | 地址编号 | INT      | 外键 |
| price      | 价格     | INT      |      |
| date       | 日期     | DATETIME |      |

#### SaleGood订单商品表

| 属性名  | 中文名   | 数据类型 | 备注 |
| ------- | -------- | -------- | ---- |
| id      | 编号     | INT      | 主码 |
| sale_id | 订单编号 | INT      | 外键 |
| good_id | 商品ID   | INT      | 外键 |
| num     | 商品数量 | INT      |      |

#### GoodDetail商品详情表

| 属性名     | 中文名   | 数据类型 | 备注 |
| ---------- | -------- | -------- | ---- |
| id         | 编号     | INT      | 主码 |
| user_id    | 用户编号 | INT      | 外键 |
| address_id | 地址编号 | INT      | 外键 |
| price      | 价格     | INT      |      |
| date       | 日期     | DATETIME |      |

#### 索引

对查询常用的属性添加索引可以大大提高查询效率，码的查询频次高，外键多用于关系的连接操作，所以关系的索引设置在主码和外键上，以下加粗部分表示索引：

- 账户表（**编号**，**用户名**，**密码**，身份，余额）

- 商品表（**编号**，商品名，价格，**卖家编号**，制造商，图片地址，描述，生产日期，保质期）
- 购物车表（**编号**，**用户编号**，**商品编号**，数量）
- 收藏表（**编号**，**用户编号**，**商品编号**，收藏）
- 库存表（**编号**，**商品编号**，库存）
- 地址表（**编号**，**用户编号**，收件人姓名，收件人电话，地址，详细地址，备注，默认地址）
- 订单表（**编号**，**用户编号**，**地址编号**，价格，日期）
- 订单商品表（**编号**，**订单编号**，**商品编号**，数量）
- 商品详情表（**编号**，**商品编号**，键值，值）

### Part 4 系统的安全性设计，不同人员的外模式及相关权限

本系统后端采用Django+MySQL的方式来搭建，具有一定的安全性。

<table>
<tr>
	<td><img src="https://logos-download.com/wp-content/uploads/2019/06/Django_Logo.png" width="400"></td>
    <td><img src="https://ts1.cn.mm.bing.net/th/id/R-C.6b47d7fec15d3e1a5de086ac1c808f6d?rik=IIkC39481Md3Bw&riu=http%3a%2f%2flogos-download.com%2fwp-content%2fuploads%2f2016%2f05%2fMySQL_logo_logotype.png&ehk=aWHquyoObU%2fXSsDiw7VKaqGdBCxP2cRjipdNUO5Q6us%3d&risl=&pid=ImgRaw&r=0" width="400"></td>
<tr>
</table>

#### 数据库与控制程序隔离

Django框架将控制程序与数据库解耦，因此控制程序并不会直接产生并调用 SQL 语句来操作数据库，而是通过 OR Mapping 来间接操作数据库。因此安全性有一定的保障——可以防御诸如 SQL 注入的攻击

#### 防御 SQL 注入

SQL 注入能让恶意用户能在数据库中执行任意 SQL 代码。这将导致记录被删除或泄露。

Django 的 querysets 在被参数化查询构建出来时就被保护而免于 SQL 注入。查询的 SQL 代码与查询的参数是分开定义的。参数可能来自用户从而不安全，因此它们由底层数据库引擎进行转义。

#### 防御跨站脚本攻击（XSS）

XSS 攻击允许用户将客户端脚本注入到其他用户的浏览器中。这通常是通过将恶意脚本存储在数据库中，在那里它将被检索并显示给其他用户，或者通过让用户点击一个链接，使攻击者的 JavaScript 被用户的浏览器执行来实现。然而，XSS 攻击可以来自任何不受信任的数据源，如 cookie 或网络服务，只要数据在被纳入页面之前没有被充分净化。Django可以保护免受大多数XSS攻击。

#### 防御跨站点请求伪造（CSRF）

发起 CSRF 攻击的人可以使用其他用户的证书执行操作，且是在其不知情或不同意的情况下。Django 内置了保护措施来防御大多数 CSRF 攻击。

#### Host 头部验证

在某些情况下，Django 使用客户端提供的 `Host` 头部来构造 URLs。这些值虽被清理以阻止跨站脚本攻击，但伪造 `Host` 值还是可以用于跨站请求伪造，缓存毒化攻击，以及电子邮件中的有毒链接。

#### 按用户类别设置外模式与权限

本系统中有两种用户，`admin`和`customer`，其中`admin`作为超级账号对数据库有完全权限，并可以增删改查所有数据，对所有数据进行综合分析等；`customer`作为普通用户账号可以增删改查自己账户内数据，对自己数据进行统计分析等。

#### 数据加密
为了保证数据的安全性，我们对密码，密保问题答案等隐私数据进行加密。项目使用了对称加密方法 AES 进行数据加密。 AES Advanced Encryption Standart ，高级加密标准）是最为常见的对称加密算法。本项目中加密与解密均由服务端完成，所以采用对称的加密算法是既简单又高效的。 AES 是分组加密技术，具体的流程如下图所示：

![image-20221224101414894](系统实现报告/image-20221224101414894.png)



### Part 5 存储过程、触发器和函数的代码说明

#### 存储过程

我们的项目中对较为复杂的操作在 SQL 层面封装成过程，由于 SQL 中的函数与过程是预先编译并存入 DBMS 中的，调用的时候过程内部不需要解释执行，提高了 SQL 的执行效率，也简化了高级语言的处理逻辑。

根据实际需求，我们使用了如下存储过程：
##### 搜索相似后缀名商品

```sql
# 存储过程
use CyberSeller_db1;
drop procedure if exists searchGood;
delimiter $$
create procedure searchGood(in input varchar(255))
begin
    select *
        from backendapp_good
            where name like concat('%', input);
end $$
delimiter ;
```

根据用户输入的关键词可以检索和关键词相似的商品，根据数据统计和分析，相似商品往往可能拥有相似后缀，如“星巴克咖啡”和“瑞星咖啡”，用户检索“咖啡”时就会显示这两个商品。

#### 触发器

触发器对于保证数据一致性有很大帮助，而且有时候将数据更新在数据库层面完成，可以简化高级语言的处理逻辑。但是触发器的性能并不好，而且容易出现循环触发等问题，所以我们对于更新数据量为一条数据，与其他数据耦合度小，功能比较独立的操作才使用触发器。

##### 库存数管理

库存数的更新是一个局部细节问题，与其余问题耦合度小，涉及数据仅为一样商品库存信息，所以我们使用了触发器。

```sql
DELIMITER $$
CREATE TRIGGER 库存大于等于零 after update on backendapp_repo
    for each row
    begin
        if (new.repo < 0) then
            signal sqlstate '65666' set message_text = '库存不能小于0';
        end if;
    end $$
DELIMITER ;
```

#### 函数

用户时常关心商品的价格区间胜过具体价格，对于一般用户而言，其对商品价格的敏感度可以为大于`5000`元时认为昂贵，`2000-5000`元时认为一般，小于`2000`元时认为廉价，因此我们设计了查询函数来快速判断商品价格。

```sql
use CyberSeller_db1;
DELIMITER $$
CREATE FUNCTION getPrice(price integer) RETURNS varchar(3)
DETERMINISTIC
BEGIN
    case
        when (price >= 5000) then return '昂贵';
        when (price >= 2000) then return '一般';
        else return '廉价';
    end case;
END $$
DELIMITER ;
```

### Part 6 实现过程中主要技术和主要模块的论述

#### Django 框架

Django是由Python编写的开源Web应用框架，Python+Django+Vue是网站开发与部署的常见组合。

- 齐全的功能。自带大量常用工具和框架，可轻松、迅速开发出一一个功能齐全的Web应用。

- 完善的文档。Django已发展十余年，具有广泛的实践案例，同时Django提 供完善的在线文档，Django用户能够更容易地找到问题的解决方案。

- 强大的数据库访问组件。Django自带一个面向对象的、反映数据模型(以Python类的形式定义)与关系型数据库间的映射关系的映射器(ORM)，开发者无须学习SQL语言即可操作数据库。

- 灵活的URL映射。Django提供一个基于正则表达式的URL分发器，开发者可灵活地编写URL。

- 丰富的模板语言。Django模板语言功能丰富，支持自定义模板标签。Django也支持使用第三方模板系统，如jinja2等 。

- 健全的后台管理系统。Django内置了-一个后台数据管理系统，经简单配置后，再编写少量代码即可使用完整的后台管理功能。

- 完整的错误信息提示。Django提供 了非常完整的错误信息提示和定位功能，可在开发调试过程中快速定位错误或异常。

- 强大的缓存支持。Django内置了一个缓存框架，并提供了多种可选的缓存方式。

- 国际化。Django包含一个国际化系统，Django组件支持多种语言。

#### Django 模型映射数据库实体（OR Mapping）

Django 提供了 Model 映射数据库实体，在本项目中，`CyberSllerDjangoBackEnd/backendapp/models.py`中以Python类的形式记录了表单的结构，方便使用Django提供的OR Mapping API直接操作数据库。如下图中，左侧为`models.py`中的类结构，右侧为数据库中的对应表单。

<table>
<tr>
	<td><img src="系统实现报告/image-20221224111438670.png" width="400"></td>
    <td><img src="系统实现报告/image-20221224111507297.png" width="400"></td>
<tr>
</table>

##### 增删改查

在Django框架中，对数据库操作提供了良好的封装（相较于pymysql而言），增删改查变得更加面向对象。

###### 增

```python
good = Good(name=name, price=price, seller_id=seller_id,
					maker=maker, picture=pic_url, description=description,
					date=date, shelf_life=shelf_life)
good.save()
```

###### 删

```python
good_obj = Good.objects.get(id = 1)
good_obj.delete()
```

###### 改

```python
# 方法一
good = Good.get(did = 1) # 相当于SQL查询，good为Good对象
good.name = "new_name" # 修改内容
good.save() # 保存上传
```

###### 查

**获取全部数据**

```python
# objects是模型管理器，all()返回了所有数据行，某种程度上相当于SQL中的SELECT * FROM
# 其中，ls是一个列表，其中每一个元素是Good对象，这是比pymysql更优雅的地方
good = Goods.objects.all()
```

**按条件获取数据**

```python
goods = Good.objects.filter(seller_id=user_id)
```

#### MySQL 数据库

尽管Django自带了Sqlite3数据库，但这一数据库过于轻量级，不很符合本课程设计的要求。

相较而言，MySQL作为最流行的数据库之一，其功能完整，性能优良，表现稳定，适合本项目使用。

#### 路由 - 控制器 - 渲染

前端发送请求后，路由接收到前端的请求，随后根据`CyberSellerDjangoBackEnd/backendapp/urls.py`中定义的路由信息，找到`CyberSellerDjangoBackEnd/backendapp/views.py`对应的控制器（Controller）与动作（Action）。本项目的路由信息可由如下命令给出：

| 名称                   | URL                                               | 行为                           | 方式           |
| ---------------------- | ------------------------------------------------- | ------------------------------ | -------------- |
| `signup`               | `http://43.143.179.158:8080/signup`               | 注册                           | POST/JSON      |
| `login`                | `http://43.143.179.158:8080/login`                | 登录                           | POST/JSON      |
| `addGoods`             | `http://43.143.179.158:8080/addGoods`             | 添加售卖商品                   | POST/FORM-DATA |
| `updateShopCart`       | `http://43.143.179.158:8080/updateShopCart`       | 添加商品到购物车               | POST/FORM-DATA |
| `mainRecommendGoods`   | `http://43.143.179.158:8080/mainRecommendGoods`   | 为用户推荐商品                 | POST/FORM-DATA |
| `getGood`              | `http://43.143.179.158:8080/getGood`              | 获取指定商品所有信息           | POST/FORM-DATA |
| `searchShopCart`       | `http://43.143.179.158:8080/searchShopCart`       | 获取用户购物车内所有商品和数量 | POST/FORM-DATA |
| `updateStar`           | `http://43.143.179.158:8080/updateStar`           | 更新收藏关系                   | POST/FORM-DATA |
| `getSixPictures`       | `http://43.143.179.158:8080/getSixPictures`       | 获取首页六张滚播图             | POST/FORM-DATA |
| `updateRepo `          | `http://43.143.179.158:8080/updateRepo`           | 更新库存容量                   | POST/FORM-DATA |
| `getSellGoods `        | `http://43.143.179.158:8080/getSellGoods`         | 获取正在售卖的商品             | POST/FORM-DATA |
| `goodsRecommendGoods`  | `http://43.143.179.158:8080/goodsRecommendGoods ` | 为商品推荐商品                 | POST/FORM-DATA |
| `getStarGoods`         | `http://43.143.179.158:8080/getStarGoods `        | 获取收藏商品                   | POST/FORM-DATA |
| `deleteGood`           | `http://43.143.179.158:8080/deleteGood`           | 删除指定商品                   | POST/FORM-DATA |
| `analyseExcel`         | `http://43.143.179.158:8080/analyseExcel`         | 解析Excel文件                  | POST/FORM-DATA |
| `analyseShopCart`      | `http://43.143.179.158:8080/analyseShopCart`      | 分析用户购物车内商品信息       | POST/FORM-DATA |
| `addAddress`           | `http://43.143.179.158:8080/addAddress`           | 添加地址                       | POST/FORM-DATA |
| `addSale`              | `http://43.143.179.158:8080/addSale`              | 添加订单                       | POST/FORM-DATA |
| `addSaleGood`          | `http://43.143.179.158:8080/addSaleGood`          | 添加订单商品关系               | POST/FORM-DATA |
| `analyseSale`          | `http://43.143.179.158:8080/analyseSale`          | 分析订单商品信息               | POST/FORM-DATA |
| `getGoodDetail`        | `http://43.143.179.158:8080/getGoodDetail`        | 获取商品详情                   | POST/FORM-DATA |
| `getAddress`           | `http://43.143.179.158:8080/getAddress`           | 获取地址                       | POST/FORM-DATA |
| `deleteAddress`        | `http://43.143.179.158:8080/deleteAddress`        | 删除地址                       | POST/FORM-DATA |
| `updateDefaultAddress` | `http://43.143.179.158:8080/updateDefaultAddress` | 设置默认地址                   | POST/FORM-DATA |
| `analyseLike`          | `http://43.143.179.158:8080/analyseLike`          | 分析用户收藏商品信息           | POST/FORM-DATA |
| `updateShopCartNum`    | `http://43.143.179.158:8080/updateShopCartNum`    | 更新购物车商品数量             | POST/FORM-DATA |

随后落入当前请求对应的控制器动作中，由控制器来进行 ORM 操作，并发回前端。

#### 服务器

服务器端使用`conda`进行虚拟环境管理，使用`Django=3.2`



### Part 7 若干展示系统功能的运行实例

### Part 8 源程序简要说明

### Part 9 收获和体会
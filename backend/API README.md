# API

> 多数时候，前端开发人员只需阅览本API文档即可获取所有必要信息，无需查阅数据库README

## 用户注册与登录

### signup用户注册

#### 发送

- 使用`POST`方法向服务器提供注册数据申请

- 具体属性如下：

| 属性     | 说明   | 类型                                              |
  | -------- | ------ | ------------------------------------------------- |
  | name     | 用户名 | 字符串，非空，长度小于`64`                        |
  | password | 密码   | 字符串，非空，长度小于`64`                        |
  | identity | 身份   | 字符串，非空，为`admin, customer, seller`三种之一 |

#### 接收

返回一个`HttpResponse`对象，属性列表如下：

| 属性    | 说明               | 类型                                                         |
| ------- | ------------------ | ------------------------------------------------------------ |
| succeed | 请求是否被成功执行 | 布尔值                                                       |
| code    | 处理结果代码       | 六位字符串，标识不同正确/错误情况，前两位固定为`01`表示是`signup`的code；中间两位错误时为`00`，正确时为`01`；最后两位表明是正确/错误情况中的具体情形，可以查阅下方的表 |
| message | 提示信息           | 提供更多关于本次请求处理结果的信息                           |
| id      | 注册得到的用户id   | 只有成功注册时返回一个正数，注册失败返回-1                   |

- 正确情况

| succeed | code     | message                         | id                   |
| ------- | -------- | ------------------------------- | -------------------- |
| `True`  | `010101` | `SUCCESS! Sign up successfully` | <数据库自动赋予的id> |

- 错误情况：

| succeed | code     | message                                                      | id   | 说明                                       | 处理方案                       |
| ------- | -------- | ------------------------------------------------------------ | ---- | ------------------------------------------ | ------------------------------ |
| `False` | `010000` | `ERROR! Empty name, password or identity, make sure they are legal` | `-1` | `name,password,identity`中有空值或空字符串 | 不执行请求，对数据库不产生影响 |
| `False` | `010001` | `ERROR! This URL accepts POST ONLY!`                         | `-1` | 使用非POST方法发送请求                     | 不执行请求，对数据库不产生影响 |
| `False` | `010002` | `ERROR! Too long name, make sure len <= 64`                  | `-1` | 用户名过长                                 | 不执行请求，对数据库不产生影响 |
| `False` | `010003` | `ERROR! Too long password, make sure len <= 64`              | `-1` | 密码过长                                   | 不执行请求，对数据库不产生影响 |
| `False` | `010004` | `ERROR! Illegal identity, make sure identity is admin, customer or seller` | `-1` | 非法身份                                   | 不执行请求，对数据库不产生影响 |
| `False` | `010005` | `ERROR! This name has been signed up, please choose another name` | `-1` | 重名用户名                                 | 不执行请求，对数据库不产生影响 |

### login用户登录

#### 发送

- 使用`POST`方法向服务器提供注册数据申请
- 具体属性如下：

| 属性     | 说明   | 类型                       |
| -------- | ------ | -------------------------- |
| name     | 用户名 | 字符串，非空，长度小于`64` |
| password | 密码   | 字符串，非空，长度小于`64` |

#### 接收

返回一个`HttpResponse`对象，属性列表如下：

| 属性     | 说明             | 类型                                                         |
| -------- | ---------------- | ------------------------------------------------------------ |
| succeed  | 是否登陆成功     | 布尔值                                                       |
| code     | 处理结果代码     | 六位字符串，标识不同正确/错误情况，前两位固定为`02`表示是`login`的code；中间两位错误时为`00`，正确时为`01`；最后两位表明是正确/错误情况中的具体情形，可以查阅下方的表 |
| message  | 提示信息         | 提供更多关于本次请求处理结果的信息                           |
| id       | 登录得到的用户id | 返回数据库中该用户的唯一id，为`int`                          |
| balance  | 该用户账户余额   | 返回余额                                                     |
| identity | 用户身份         | 字符串                                                       |

- 正确情况

| succeed | code     | message                        | id                   | balance          | identity     |
| ------- | -------- | ------------------------------ | -------------------- | ---------------- | ------------ |
| `True`  | `020101` | `SUCCESS! Log in successfully` | <数据库自动赋予的id> | <该用户账户余额> | <该用户身份> |

- 错误情况

| succeed | code     | message                                                    | id   | balance | identity     | 说明                              |
| ------- | -------- | ---------------------------------------------------------- | ---- | ------- | ------------ | --------------------------------- |
| `False` | `020000` | `ERROR! This URL accepts POST ONLY! `                      | -1   | -1      | `FAIL`       | 使用非POST方法发送请求            |
| `False` | `020001` | `ERROR! Empty name or password, make sure they are legal`  | -1   | -1      | `FAIL`       | `name,password`中有空值或空字符串 |
| `False` | `020002` | `ERROR! Non-exist name, make sure the name is correct`     | -1   | -1      | `FAIL`       | 用户名错误                        |
| `False` | `020003` | `ERROR! Wrong password, make sure the password is correct` | -1   | -1      | <该用户身份> | 密码错误                          |


# backend

后端由[YJK](@saltyfishyjk)负责开发和维护，本文档是对其他开发者提供的说明文档。

## 环境与配置

基于稳定性等多方考虑，最终选择的配置如下：

| 环境   | 版本  | 备注                                               |
| ------ | ----- | -------------------------------------------------- |
| Ubuntu | 20.04 | 选购了腾讯云2核2G5M50GB服务器                      |
| Python | 3.9   | 使用`conda activate SyberSeller`进入本项目虚拟环境 |
| Django | 3.2   | 目前（2022.10）最新的LTS                           |
| MySQL  | 8.0   | 老师不推荐用SQLite，因此选用MySQL:cry:             |
|        |       |                                                    |

### 进入服务器与开发环境

使用xshell连接，配置如下：

| 属性   | 值               |
| ------ | ---------------- |
| 名称   | CyberSeller      |
| 主机   | 43.143.179.158   |
| 端口   | 22               |
| 用户名 | ubuntu           |
| 密码   | CyberSeller2022! |

> 上述用户名和密码是root权限，请谨慎操作！

### 远程连接数据库

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

***

以下介绍从零（刚购置的腾讯云服务器）开始进行的各项环境配置，以备查看。如果仅使用本服务器，则无需阅读。

### 安装conda

完全按照[这篇博客](https://zhuanlan.zhihu.com/p/459607806)操作。

### 创建本项目虚拟环境

```bash
conda create --name CyberSeller python=3.9
```

### 安装Django 3.2

```bash
pip install Django==3.2
```

### 安装MySQL

参考[这篇文章](https://cloud.tencent.com/developer/article/1622599)安装MySQL

### MySQL的启动/停止

- 启动：`service mysql start `
- 关闭：`service mysql stop`

### 配置MySQL root

参考[这篇文章](https://blog.csdn.net/weixin_44509186/article/details/119765206)及其评论，进行如下操作：

- cat默认用户名和密码：`sudo cat /etc/mysql/debian.cnf `，得到默认用户和密码：

  ```
  [client]
  host     = localhost
  user     = debian-sys-maint
  password = LjrLhREPwJmRO0qa
  socket   = /var/run/mysqld/mysqld.sock
  ```

- 使用默认user和password登录：`mysql -udebian-sys-maint -p`，然后输入密码`LjrLhREPwJmRO0qa`进入默认账户

- 由于我们的MySQL版本是8.0，因此使用`update mysql.user set authentication_string='', plugin='mysql_native_password' where user='root';`置空字段，然后使用`flush privileges;`刷新（注意这里原博客没有写明要刷新，但是评论有人指出需要刷新，不刷新会有问题）

- 然后修改密码`ALTER user 'root'@'localhost' IDENTIFIED BY 'root';`其中`root`是新密码，接着使用`flush privileges;`刷新

- 最后，`exit`退出当前MySQL账户并使用`root`和新密码登录。

### 创建项目用数据库

```bash
create database CyberSeller_db1 default charset=utf8;
```

### 设置允许远程连接数据库

- 参考[这篇文章](https://blog.csdn.net/ndjdi/article/details/113184194)进行操作，注意完成其中步骤后需要重启MySQL服务。
- 由于腾讯云的安全组限制，还需要在腾讯云服务器后台开放3306端口（数据库端口）

![image-20221019200916832](README/image-20221019200916832.png)

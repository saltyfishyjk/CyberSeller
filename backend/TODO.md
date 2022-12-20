# TODO

本文档记录后端待开发/填坑的内容。

同时，欢迎其他开发者在这里记录新需求，或通过issue等方式发出。

## Part 1 数据库

- 需要为Account表设计触发器（拒绝非法identity等）

## Part 2 Django

## Part 3 API

```json
//void addGoods(FormData goods)
//通过表单(FormData)格式定义商品,数据格式暂定如下
//tips:后端应为每个商品声明前端不提供但后端可见的商品id，卖家id等各种id
//来一个商品例子
{
    goods_id: 
	name: "百元大钞",//商品名称
    price: 100,//价格
    seller: "lr",//卖家
    maker: "bank",//制造商
    picture: ,//商品图片
    description: "",//商品描述
    date: "2022-12-19",//生产日期
    shelfLife: "10-0-0-0",//保质期 year-month-day-hour
}
```



```
List<goods> searchShopcart(String Username)
使用`用户名`查询购物车，返回该用户的购物车商品清单
```



```
List<goods> mainRecommendGoods(String Username)
使用`用户名(username)`查询为该用户推荐的商品，显示在主页

List<goods> goodsRecommendGoods(Goods goods)
使用`商品id(goods_id)`查询基于该商品的相关推荐商品
```



```
收藏
```



## Part 4 Other




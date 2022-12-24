<template >
  <div style="">
    <div class="goodsBox">
      <div class="goodsBox-img">
        <el-image
          style="position: absolute;width: 500px; height: 600px;left: 0px;border-radius: 14px;"
          :src="goodImg"
          :preview-src-list="goodImg">
        </el-image>
        <div class="goodsBox-store">

        </div>
        <div class="goodsBox-btn">
         <br><br>
          <h1>{{goodName}}</h1><br>
          <h2><span style="color: #777777">售价&ensp;</span><span style="color: #e4393c;font-family: simsun">&yen;<span></span>{{goodPrice}}</span></h2>
          <br><br>
          <h4 style="position: relative;left: -35%;"><span style="color: #777777">库存&ensp;</span><span style="color: #4D6530;font-family: simsun"><span></span>{{ goodRepo }}</span></h4>
          <el-input-number size="large" v-model="num" :min="1" :max="goodRepo" @change="handleChange" label="商品数量"></el-input-number>
          <el-button size="medium" type="danger" @click="add1">加入购物车</el-button>
          <el-button size="medium" type="warning" @click="add2">收藏</el-button>
          <p style="color: #777777">温馨提示·支持7天无理由退货</p>
        </div>
      </div>
    </div>
<!--    猜你喜欢-->
    <div class="goodsLikes" id="goodsLikes" style="text-align: center;">
      <hr />
      <h1 style="color: #777777">猜你喜欢</h1>
      <div style="margin-left: 10%">
        <div class="card" v-for="(item, index) in favouriteList.slice(0,5)" :key="item.id" v-on:mouseenter="showDialog(index)" v-on:mouseleave="hideDialog(index)">
          <div class="ribbon">
            <!--鼠标移入移出事件-->
            <div class="handleDialog" v-if="ishow && index==current">
              <p style="margin-left:5%;margin-top: 60%;">{{item.name}}</p>
              <el-button type="success" style="margin-left:5%;" size="medium" @click="goGoodsDesc(item.id)">查看详情</el-button>
            </div>
            <img :src="item.picture" style="height: 100%;width: 100%">
            <h2><span style="color: #e4393c;font-family: simsun">&yen;{{item.price}}</span></h2>
          </div>
        </div>
      </div>
     <div style="float: left;width: 23%;height: 1px;"></div>
      <br><br>
    </div>
<!--    详情图片-->
    <br><br>
    <div class="goodsDescImg" id="goodsDescImg" style="text-align: center;margin-top: 300px">
      <hr />
      <h1 style="color: #777777">商品详情</h1><br><br><br>
      <p>{{goodDescribtion}}</p>
    </div>
  </div>


</template>

<script>
  import { postForm } from '../../api';
export default {
        inject: ['reload'],
        name: "goodsDesc",
        data() {
          return {
            num: 1,
            value: 3.7,
            money:5999.00,
            prize:5999.00,
            sum:65,
            goodsId:'0',
            //隐形窗口
            ishow: false,
            current: 0,

            //按钮点击限制
            add1_can_press : true,
            add2_can_press : true,
            err_can_press : true,

            goodMaker:null,
            goodName:null,
            goodPrice: null,
            goodDescribtion: null,
            goodImg: null,
            favouriteList: null,
            goodRepo: 0,
          };
        },
        created() {
          if (this.$route.query.goods==null) {
            this.$router.push('/helloHome');
          }
          this.goodsId = this.$route.query.goods;
          this.getdate();
        }
        ,
        methods: {
          //数据更新
          getdate() {
            let fd = new FormData()
            fd.append('good_id', this.goodsId)
            postForm(`http://43.143.179.158:8080/getGood`, fd).then(res => {
              console.log(res)
              this.goodMaker = res.maker;
              this.goodName = res.name;
              this.goodPrice = res.price;
              this.goodDescribtion = res.description;
              this.goodImg = res.picture;
              this.goodRepo = res.repo;
            })
            .catch(function (error) {
            console.log(error);
            });
            console.log("get favourite")
            let nfd = new FormData()
            nfd.append('good_id', this.goodsId)
            postForm(`http://43.143.179.158:8080/goodsRecommendGoods`, nfd).then(res => {
            console.log(res)
              this.favouriteList = res.goods;
            })
            .catch(function (error) {
              console.log(error);
            });
          },
          //前往商品详情页
          goGoodsDesc(goods) {
            this.$router.push({
              path:'/goodsDesc',
              query:{
                goods:goods
              }
            });
            this.reload()
          },
          handleChange(value) {
            console.log(this.num);
          },
          //显示操作项
          showDialog(index, item) {
            this.ishow = true;
            this.current = index;
          },
          //隐藏蒙层
          hideDialog(index, item) {
            this.ishow = false;
            this.current = null;
          },
          //添加购物车
          add1() {
            if(this.add1_can_press==true)
            {
              this.$notify({
                title: '添加购物车',
                message: '商品已添加到你的购物车',
                type: 'success'
              });
              this.add1_can_press = false;
              console.log("添加购物车");
              let fd = new FormData()
              fd.append('user_id', localStorage.getItem('userId'))
              fd.append('good_id', this.goodsId)
              fd.append('new_num	', this.num)
              postForm(`http://43.143.179.158:8080/updateShopCart`, fd).then(res => {
                console.log(res)
              })
              .catch(function (error) {
              console.log(error);
              });
              setTimeout(()=>{
                this.add1_can_press = true;
              },2000)
            }else if(this.err_can_press==true){
              this.$notify.error({
                title: '错误',
                message: '请求过于频繁，2秒后重试'
              });
              this.err_can_press = false;
              setTimeout(()=>{
                this.err_can_press = true;
              },1000)
            }
          },
          //添加收藏
          add2() {
            if(this.add2_can_press==true)
            {
              this.$notify({
                title: '收藏',
                message: '收藏成功',
                type: 'success'
              });
              this.add2_can_press = false;
              let fd = new FormData()
              fd.append('user_id', localStorage.getItem('userId'))
              fd.append('good_id', this.goodsId)
              fd.append('like', 1)
              postForm(`http://43.143.179.158:8080/updateStar`, fd).then(res => {
              console.log(res)
              })
              .catch(function (error) {
              console.log(error);
              });
              setTimeout(()=>{
                this.add2_can_press = true;
              },2000)
            }else if(this.err_can_press==true){
              this.$notify.error({
                title: '错误',
                message: '请求过于频繁，2秒后重试'
              });
              this.err_can_press = false;
              setTimeout(()=>{
                this.err_can_press = true;
              },1000)
            }

          },
        }

    }
</script>

<style scoped>
  .goodsBox {
    /*box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);*/
    /*background: #F2F8FE;*/
    position: relative;
    width:1400px;
    height: 800px;
    margin: 0 auto;
    text-align: center;
  }

  .goodsBox-img {
    position: absolute;
    top: 5%;
    left: 15%;
    width: 75%;
    height: 75%;
    /*background-color: #409EFF;*/
     /*text-align: center; */
    /* vertical-align: middle; */
  }
  .goodsBox-btn {
    position: absolute;
    top: 15%;
    left: 55%;
    width: 40%;
    height: 20%;
    /*background-color: #409E1F;*/
     text-align: center;
     vertical-align: middle;
  }
  .goodsBox-store {
    position: absolute;
    top: 5%;
    left: 45%;
    width: 30%;
    height: 20%;
    /*background-color: #409E1F;*/
     text-align: center;
     vertical-align: middle;
  }

  /**
  卡片
   */

  .card{
    height: 170px;
    width: 170px;
    margin-left: 30px;
    margin-top: 30px;
    background-color: white;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    border-radius: 4px;
    float: left;
  }
  .card img {
    width: 100%;
    height: 100%;
  }
  .card span {
    font-size: 15px;
    color: #BFBFBF;
    display: block;
    letter-spacing: 2px;
    /*padding: 0px 20px;*/
  }
  /**
隐藏页
*/
  .handleDialog {
    position: absolute;
    background: rgba(0, 0, 0, 0.6);
    width: 100%;
    height: 100%;
  }
  /**
丝带
 */

  .ribbon {
    display: inline-block;
    width: 100%;
    height: 100%;
    position: relative;
    float: left;
    margin-bottom: 30px;
    background-size: cover;
    text-transform: uppercase;
    color: white;
  }
</style>

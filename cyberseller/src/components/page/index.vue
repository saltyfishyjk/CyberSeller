<template>
  <div>
    <el-carousel :interval="4000" type="card" height="200px" style="background: #F2F8FE">
      <el-carousel-item v-for="item in imageList" :key="item">
        <img :src="item" alt="" class="rightulliimg">
      </el-carousel-item>
    </el-carousel>
    <br>
    <el-container>
      <div style="float: left;width: 25%;">
        <!--左边栏空白占位  -->
      </div>
<!--      <el-cascader-panel :options="options" style="width: 19%;background: #F2F8FE;"></el-cascader-panel>-->
      <div style="float: left;width: 50%;">
        <el-input placeholder="查询商品" v-model="selectd" class="input-with-select" size="1000px">
          <el-button slot="append" icon="el-icon-search" @click="searchInputChange()"></el-button>
        </el-input>


      </div>
    </el-container>

    <br>
    <div>
      <el-container >
        <div style="float: left;width: 10%;background-color: #DCDFE6;">
          <!--左边栏空白占位  -->
        </div>
        <div style="float: left;width: 80%;">
              <div class="card"  v-for="(item, index) in currentGoods" :key="item.id" v-on:mouseenter="showDialog(index)" v-on:mouseleave="hideDialog(index)">
                  <div class="ribbon">
                    <!--鼠标移入移出事件-->
                    <div class="handleDialog" v-if="ishow && index==current">
                      <el-button type="success" style="margin-left:25%;margin-top: 70%;" size="medium" @click="goGoodsDesc(item.id)">查看详情</el-button>
                      <el-button type="warning" icon="el-icon-star-off" circle size="medium"  @click="addCollection(item.id)"></el-button>
                    </div>
                    <img :src="item.picture" style="height: 100%;width: 100%">
                    
                </div>
                <div style="text-align:center">
                  <span>{{item.name}}</span>
                  <span>&yen;{{item.price}}</span>
                  <span>{{item.seller_name}}</span>
                </div>
              </div>
        </div>
        <div style="float: left;width: 10%;background-color: #DCDFE6;">
          <!--右边栏空白占位  -->
        </div>

      </el-container>
      <br>
      <center>
        <el-pagination
          background
          @current-change="handleCurrentChange"
          layout="prev, pager, next"
          :page-size="12"
          :total="1000">
        </el-pagination>
      </center>
    </div>
  </div>
</template>

<script>
import { postForm } from '../../api';
export default {
  name: "index",
  data() {
    return {
      ishow: false,
      init_data: true,
      current: 0,
      selectd: '',
      currentDate: new Date(),
      imageList:null,
      goodsList:null,
      goodsRst: null,
      currentindex: 1,
      currentGoods: null
    };
  },
  methods:{
    searchInputChange() {
      console.log(1);
      this.goodsRst = []
      if (this.selectd.length == 0) {
          this.goodsRst = this.goodsList
          this.currentGoods = this.goodsRst.slice((this.currentindex-1)*12, this.currentindex*12)
      } else {
        let regStr =  '';
        // 初始化正则表达式
        for(let i=0; i<this.selectd.length; i++){
          regStr = regStr + '(' + this.selectd[i] + ')([\\s]*)'; //跨字匹配
        }

        let reg = new RegExp(regStr);
        console.log(reg);
        for(let i=0; i<this.goodsList.length; i++) {
          let name = this.goodsList[i].name; //按照名字匹配
          let regMatch = name.match(reg);
          if(null !== regMatch) {// 将匹配的数据放入结果列表中
             this.goodsRst.push(this.goodsList[i]);
          }
          let price = this.goodsList[i].price; //按照名字匹配
          regMatch = price.match(reg);
          if (null !== regMatch) {// 将匹配的数据放入结果列表中
            this.goodsRst.push(this.goodsList[i]);
          }
          let seller = this.goodsList[i].seller_name; //按照名字匹配
          regMatch = seller.match(reg);
          if (null !== regMatch) {// 将匹配的数据放入结果列表中
            this.goodsRst.push(this.goodsList[i]);
          }
        }
        this.currentGoods = this.goodsRst.slice((this.currentindex-1)*12, this.currentindex*12)
      }
    },

    addCollection(goodId) {
      let fd = new FormData()
      fd.append('user_id', localStorage.getItem('userId'))
      fd.append('good_id', goodId)
      fd.append('like', 1)
      postForm(`http://43.143.179.158:8080/updateStar`, fd).then(res => {
      console.log(res)
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
    handleCurrentChange(val) {
      this.currentindex = val;
      console.log(this.currentindex);
      this.currentGoods = this.goodsRst.slice((this.currentindex-1)*12, this.currentindex*12)
    }
  },
  beforeCreate() {
    console.log('Call Vue beforeCreate');
    let fd = new FormData()
    fd.append('user_id', localStorage.getItem('userId'))
    console.log('user_id' + localStorage.getItem('userId'))
    postForm(`http://43.143.179.158:8080/mainRecommendGoods`, fd).then(res => {
      console.log('get goods')
      console.log(res)
      this.goodsList = res.goods;
      this.goodsRst = this.goodsList;
      this.currentGoods = this.goodsRst.slice(0, 12)
    })
    .catch(function (error) {
      console.log(error);
    });
    postForm(`http://43.143.179.158:8080/getSixPictures`, fd).then(res => {
      console.log(res)
      this.imageList = res.pictures
    })
      .catch(function (error) {
        console.log(error);
    });
  }
}
</script>

<style scoped>
.el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
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
  卡片
   */

  .card{
    height: 350px;
    width: 266px;
    margin-left: 30px;
    margin-top: 30px;
    background-color: white;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    border-radius: 4px;
    float: left;
  }
  .card img {
    width: 100%;
    height: 70%;
  }
  .card span {
    font-size: 15px;
    color: #BFBFBF;
    display: block;
    letter-spacing: 2px;
    /*padding: 0px 20px;*/
  }
/**
丝带
 */

  .ribbon {
    display: inline-block;
    width: 100%;
    height: 70%;
    position: relative;
    float: left;
    margin-bottom: 30px;
    background-size: cover;
    text-transform: uppercase;
    color: white;
  }

  .wrap {
    width: 100%;
    height: 188px;
    position: absolute;
    top: -8px;
    left: 8px;
    overflow: hidden;
  }
  .wrap:before {
    content: "";
    display: block;
    border-radius: 8px 8px 0px 0px;
    width: 40px;
    height: 8px;
    position: absolute;
    right: 100px;
    background: #4D6530;
  }
  .wrap:after {
    content: "";
    display: block;
    border-radius: 0px 8px 8px 0px;
    width: 8px;
    height: 40px;
    position: absolute;
    right: 0px;
    top: 100px;
    background: #4D6530;
  }
  .ribbon6 {
    display: inline-block;
    text-align: center;
    width: 200px;
    height: 40px;

    line-height: 40px;
    position: absolute;
    top: 30px;
    right: -50px;
    z-index: 2;
    overflow: hidden;
    transform: rotate(45deg);
    -ms-transform: rotate(45deg);
    -moz-transform: rotate(45deg);
    -webkit-transform: rotate(45deg);
    -o-transform: rotate(45deg);
    border: 1px dashed;
    box-shadow: 0 0 0 3px #57DD43, 0px 21px 5px -18px rgba(0, 0, 0, 0.6);
    background: #57DD43;
  }
.rightullidiv {
  width: 100%;
  height: 200px;
  background: #f2f2f2;
  display: flex;
  justify-content: center;
  align-items: center;


}
    .rightulliimg {
      max-width: 100%;
      max-height: 200px;
      vertical-align: middle;
      text-align: center;
    }
</style>

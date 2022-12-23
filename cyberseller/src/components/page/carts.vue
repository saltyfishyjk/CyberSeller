<template>
  <div>

<!--头部-->
    <div style="width: 80%;margin-left: 20%;">
      <span>
<!--        <h1>购物车</h1>-->
      </span>
    </div>

    <!--表头-->
    <div class="title" style="width: 80%;margin-left: 10%;">
      <h3>购物车</h3>
      <el-table
        ref="multipleTable"
        :data="cartsData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
        @selection-change="handleSelectionChange"
        style="width: 100%;">

        <el-table-column
          width="35">
          <template slot-scope="scope">
            <el-checkbox v-model="scope.row.checked" :disabled="scope.row.repo==0?true:false"></el-checkbox> 
          </template>
        </el-table-column>

        <el-table-column label="商品" prop="img" width="110px" align="center">
          <template slot-scope="scope">
            
            <el-image style="width: 100px; height: 100px;" :src="scope.row.picture"/>
          </template>
        </el-table-column>
        <el-table-column label="商品名" prop="name" align="center"></el-table-column>
        <el-table-column label="状态"  prop="prize" width="110px" align="center">
          <template slot-scope="scope">
            <el-tag :type="goodsStatus(scope.row.repo)">{{scope.row.repo==0?"下架":"在售"}}</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="单价"  prop="prize" width="110px" align="center">
          <template slot-scope="scope">
            <span>&yen;</span>{{scope.row.price}}
          </template>
        </el-table-column>
        <el-table-column label="数量"  prop="num" width="140px" align="center">
          <template slot-scope="scope">
            <el-input-number size="mini" v-model="scope.row.num" :disabled="scope.row.repo==0?true:false"></el-input-number>
          </template>
        </el-table-column>
        <el-table-column label="小计"  prop="allPrize" width="110px" align="center">
          <template slot-scope="scope">
            <span>&yen;</span>{{parseFloat(scope.row.price*scope.row.num).toFixed(2)}}
          </template>
        </el-table-column>
        <el-table-column align="right">
          <template slot="header" slot-scope="scope">
            <el-input v-model="search" size="mini" placeholder="输入关键字搜索"/>
          </template>
          <template slot-scope="scope">
            <!-- <el-button size="mini" :disabled="scope.row.status==1?true:false" type="warning" @click="handleEdit(scope.$index, scope.row)">移到收藏</el-button> -->
            <!-- <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">移出购物车</el-button>
            <el-button size="mini" :disabled="scope.row.status==1?true:false" type="success" @click="selected">结算</el-button> -->
          </template>
        </el-table-column>
      </el-table>
    </div>
    <div style="width: 80%;margin-left: 10%;">

      <!--描述：商品结算开始-->
      <div class="balance">
        <ul class="balance_ul1">
          <!-- <el-button type="danger" size="medium" class="button1" plain>删除选中商品</el-button> -->
          <!-- <el-button type="danger" size="medium" class="button1" plain>清除下架商品</el-button> -->
          <!-- <el-button type="warning" size="medium" class="button1" plain>移到我的收藏</el-button> -->
          <el-button type="success" size="medium" class="button1" plain @click="transport()">结算选中商品</el-button>
          <span class="balance_ul2">
              <span>共<span class="spanText">{{total}}</span>件商品</span>
              <span>总价<span class="spanText">&yen;{{totalPrice}}</span></span>
          </span>
        </ul>
      </div>
      <!--描述：商品结算结束-->
    </div>
  </div>
</template>

<script>
    import { postForm } from '../../api';
    export default {
        name: "carts",
        data()
        {
          return{
            cartsData: null,
            search : '',
            //选中列表
            multipleSelection : [],
            chooseList : [],
            list:null
          }
        },
        created() {
            this.getData();
        },

        computed: {
          total() {
            return this.cartsData.filter(item => item.checked).reduce((t, item) => {return t += item.num}, 0)
          },
          totalPrice() {
            return this.cartsData.filter(item => item.checked).reduce((sum, item) => {return sum += item.num * item.price}, 0)
          },
        },  
        methods:{
          getData() {
            let fd = new FormData()
            fd.append('user_id', localStorage.getItem('userId'))
            postForm(`http://43.143.179.158:8080/searchShopCart`, fd).then(res => {
            this.cartsData = res.goods
            console.log(this.cartsData)
            })
            .catch(function (error) {
              console.log(error);
            });
          },
          canSelect(row) {
            if(row.status==1)
              return false;
            else return true;
          },
          goodsStatus(repo)
          {
              if(repo==0)
                return "danger";
              else 
                return "";
          },
          transport()
          {
              this.list = [];
              for (let i = 0; i < this.cartsData.length; i++) {
                if (this.cartsData[i].checked == true) {
                    let o = new Object();
                    o.name = this.cartsData[i].name
                    o.picture = this.cartsData[i].picture
                    o.price = this.cartsData[i].price
                    o.num = this.cartsData[i].num
                    this.list.push(o);
                }
              }
              console.log(this.list);
              
              let parObj = JSON.stringify(this.list)
              this.$router.push({
                path: '/makeSureOrder',
                query: {
                  'obj': parObj
                }
              })
          },
          // 多选操作
          handleSelectionChange(val) {
            this.multipleSelection = val;
          },
      }
    }
</script>

<style scoped>
  .title{
    margin-top: 50px;
  }
  .title h3{
    /*float: left;*/
    font-size: 23px;
    color: #c91623;
  }

  /*商品结算*/
  .balance{
    height: 50px;
    border: 1px solid gray;
    margin-top: 40px;
  }
  .balance li{
    float: left;
    line-height: 5px;
    margin-left: 22px;
  }
  .balance_ul2{
    float: right;
    margin-right: 10px;
  }
  .balance_ul1 .button1{
    margin-top: 5px;
  }
  .balance_ul2 .spanText{
    font-size: 25px;
    color: #C91623 ;
    font-weight: bold;
  }
  .balance_ul2 button{
    width: 100px;
    height: 50px;
    background-color: brown;
    border: 1px solid #c91623;
    font-weight: bold;
    font-size: 20px;
    color: white;
  }
  .balance_ul2 button:hover{
    background-color:#C91623 ;
  }
</style>
